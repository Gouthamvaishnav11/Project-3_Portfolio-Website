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
                details = 'HyperText Markup Language (HTML) is the standard markup language for creating web pages and web applications.';
                break;
            case 'skill-css':
                name = 'CSS';
                details = 'Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language like HTML.';
                break;
            case 'skill-js':
                name = 'JavaScript';
                details = 'JavaScript is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.';
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
                details = 'Backend development with Flask involves creating server-side logic for web applications, handling requests and responses, interacting with databases, and ensuring secure and efficient data processing.';
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
