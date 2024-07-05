from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create the Flask application
app = Flask(__name__)

# Configure the application
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Visitor model
class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(100))
    user_agent = db.Column(db.String(200))
    is_download = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    message = db.Column(db.Text)
    visit_time = db.Column(db.DateTime, default=datetime.now)

#
# Track visitors before each request
@app.before_request
def track_visitor():
    if 'visited' not in session:
        session['visited'] = True
        visitor = Visitor(
            ip_address=request.remote_addr,
            user_agent=request.user_agent.string,
            is_download=False
        )
        db.session.add(visitor)
        db.session.commit()

# Route to handle downloading resume
@app.route('/download')
def download_resume():
    visitor = Visitor(
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        is_download=True
    )
    db.session.add(visitor)
    db.session.commit()
    return redirect(url_for('static', filename='resume.pdf'))

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for contact form
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        sendername = request.form.get('Sendername')
        senderemail = request.form.get('Senderemail')
        sendermessage = request.form.get('Sendermessage')

        # Create a new Visitor instance and add to database
        new_visitor = Visitor(name=sendername, email=senderemail, message=sendermessage)
        db.session.add(new_visitor)
        db.session.commit()

        return redirect('/contact')  # Redirect after form submission

    else:
        alldetails = Visitor.query.all()
        return render_template('contact.html', alldetails=alldetails)

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for project page
@app.route('/project')
def project():
    return render_template('project.html')

# Route for report page
@app.route('/report')
def report():
    total_visits = Visitor.query.count()
    total_downloads = Visitor.query.filter_by(is_download=True).count()
    unique_visitors = Visitor.query.distinct(Visitor.ip_address).count()
    frequent_visitors = db.session.query(
        Visitor.ip_address, db.func.count(Visitor.ip_address).label('count')
    ).group_by(Visitor.ip_address).order_by(db.desc('count')).all()
    
    frequent_visitor_details = [
        {
            'ip_address': visitor.ip_address,
            'count': visitor.count,
            'last_visit': Visitor.query.filter_by(ip_address=visitor.ip_address).order_by(db.desc(Visitor.visit_time)).first().visit_time
        } for visitor in frequent_visitors
    ]

    return render_template('report.html', total_visits=total_visits, total_downloads=total_downloads,
                           unique_visitors=unique_visitors, frequent_visitor_details=frequent_visitor_details)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, port=8000)
