document.addEventListener('DOMContentLoaded', () => {
    const skills = document.querySelectorAll('.skill');
    const detailedView = document.getElementById('detailed-view');
    const skillName = document.getElementById('skill-name');
    const skillDetails = document.getElementById('skill-details');

    skills.forEach(skill => {
        skill.addEventListener('dblclick', (event) => {
            const skillId = skill.id;
            showDetailView(skillId);
        });
    });

    function showDetailView(skillId) {
        let name = '';
        let details = '';

        switch(skillId) {
            case 'skill-html':
                name = 'HTML';
                details = 'HTML (HyperText Markup Language) is the backbone of any website, used for structuring content such as text, images, and links.';
                break;
            case 'skill-css':
                name = 'CSS';
                details = 'CSS (Cascading Style Sheets) adds style and visual appeal by controlling layout, colors, fonts, and positioning, allowing you to design visually engaging websites.';
                break;
            case 'skill-js':
                name = 'JavaScript';
                details = 'JavaScript adds interactivity, enabling features like form validation, dynamic content updates, animations, and user engagement without needing to reload the page. With these three technologies combined, you can build anything from basic websites to complex, feature-rich web applications that provide seamless user experiences.';
                break;
            case 'skill-c':
                name = 'C';
                details = 'C is a general-purpose, procedural computer programming language supporting structured programming.';
                break;
            case 'skill-python':
                name = 'Python';
                details = 'Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability.';
                break;
            case 'skill-backend development':
                name = 'Backend Development';
                details = 'A backend developer using Flask with SQLAlchemy ORM builds efficient web applications by managing databases through object-relational mapping. This ensures smooth data handling, secure operations, and scalable backend solutions.';
                break;
            default:
                name = 'Unknown';
                details = 'No details available.';
        }

        skillName.textContent = name;
        skillDetails.textContent = details;
        detailedView.style.display = 'block';
    }

    window.closeDetailView = function() {
        detailedView.style.display = 'none';
    }
});
