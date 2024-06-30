# Importing the Flask class from flask module
from flask import Flask, render_template, request,redirect,session, g, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


# let's see the content of the flask module
# print( dir(flask) )

# let's create the object of the Flask class
app = Flask(__name__)



app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
database = SQLAlchemy(app)

class Visitor(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    ip_address = database.Column(database.String(100))
    user_agent = database.Column(database.String(200))
    is_download = database.Column(database.Boolean, default=False)

@app.before_request
def track_visitor():
    if 'visited' not in session:
        session['visited'] = True
        visitor = Visitor(
            ip_address=request.remote_addr,
            user_agent=request.user_agent.string,
            is_download=False
        )
        database.session.add(visitor)
        database.session.commit()



@app.route('/download')
def download_resume():
    visitor = Visitor(
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        is_download=True
    )
    database.session.add(visitor)
    database.session.commit()
    return redirect(url_for('static', filename='resume.pdf'))


# First route: Index route/default route
@app.route('/')
def index():

    
    
   # return render_template('index.html')
    return render_template('index.html')

# Second route: Contact us
@app.route('/contact')
def contact():
    
    # returning the response
    return render_template('contact.html')


# Third route: About us
@app.route('/about')
def about():
    
    # returning the response
    return render_template('about.html')

#  fourth route:project.html
@app.route('/project')
def project():
    
    # returning the response
    return render_template('project.html')


@app.route('/report')
def report():
    total_visits = Visitor.query.count()
    total_downloads = Visitor.query.filter_by(is_download=True).count()
    unique_visitors = Visitor.query.distinct(Visitor.ip_address).count()
    frequent_visitors = database.session.query(
        Visitor.ip_address, database.func.count(Visitor.ip_address).label('count')
    ).group_by(Visitor.ip_address).order_by(database.desc('count')).all()
    
    frequent_visitor_details = [
        {
            'ip_address': visitor.ip_address,
            'count': visitor.count,
            'last_visit': Visitor.query.filter_by(ip_address=visitor.ip_address).order_by(database.desc(Visitor.visit_time)).first().visit_time
        } for visitor in frequent_visitors
    ]

    return render_template('report.html', total_visits=total_visits, total_downloads=total_downloads,
                           unique_visitors=unique_visitors, frequent_visitor_details=frequent_visitor_details)



# let's run the flask application
if __name__ == "__main__":
    app.run(debug=True)
app.run(debug=True, host='0.0.0.0')







