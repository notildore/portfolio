from django.shortcuts import render
import requests



# Create your views here.

Projects = [
    {
        'title': 'Pcmd',
        'link':'https://j0fin.github.io/pcmd/',
        'image': 'pcmd-final.png', 
        'about': 'A terminal command shortener based on Python',
        'points':[
            '100% code coverage tested',
            'CI/CD built for documentation and package', 
            'Published in Pypi as a standalone package'
        ]
    },
    {
        'title': 'utile',
        'link': 'https://utile.readthedocs.io/en/latest/',
        'image': 'utile-final.png', 
        'about': 'A Python Package that eases your codeflow using @decorators',
        'points':[
            '95% code coverage tested', 
            'Publish in Pypi as a standalone package',
            'Intergration with Rust language for speed'
        ]
    },
    {
        'title': 'Medical Suitcase',
        'link': 'https://github.com/Yuthish/Medical_Suitcase',
        'image': 'med-sui-final.png', 
        'about': 'Medical Suitcase is a MVP of a government-aided healthcare-as-a-service platform',
        'points':[
            'Recognized Project in various arenas', 
            'Built with MERN and Flask Frameworks',
            'Multiple API intergrations on-the-fly'
        ]
    },
    {
        'title': 'Hyperdict',
        'link': 'https://pypi.org/project/hyperdict/',
        'image': 'hyperdict-final.png', 
        'about': 'Python dictionaries, but on steroids',
        'points':[
            'Various enhanced features added', 
            'Publish in Pypi as a standalone package',
            'Inspired from numpy'
        ]
    },
    {
        'title': 'Iris Says',
        'link': 'https://github.com/j0fiN/Iris-Says',
        'image': 'iris-final.png', 
        'about': 'Educational tool to encourage learning Iris Flower Classification',
        'points':[
            'ML models built for prediction', 
            'Interactive graphical visualizations',
            'Entire application is unittested'
        ]
    },
]

Certi = [
    {
        'title': 'Python for EveryBody Specialization', 
        'point': 'A Pythyon programming language course from beginner to advanced',
        'institute': 'University of Michigan',
        'link': 'https://www.coursera.org/account/accomplishments/specialization/certificate/FMZ8V9WTHZ85'
    },
    {
        'title': 'Mathematics for Machine Learning Specialization', 
        'point': 'A Mathematics-Python Programming course based on Machine Learning',
        'institute': 'Imperial College London',
        'link': 'https://www.coursera.org/account/accomplishments/specialization/certificate/7RADZ9PXX6JG'
    },
    {
        'title': 'Web Application Technologies and Django', 
        'point': 'Intro to Django and SQl',
        'institute': 'University of Michigan',
        'link': 'https://www.coursera.org/account/accomplishments/certificate/9S6PF84MJ6E5'
    },
    {
        'title': 'Algorithmic Toolbox', 
        'point': 'Algorithm Paradigms and Common Algorithms in Practice',
        'institute': 'University of California San Diego',
        'link': 'https://www.coursera.org/account/accomplishments/certificate/AJ3RRTH6EJV5'
    },
    {
        'title': 'Java Programming: Solving Problems with Software', 
        'point': 'Java Programming from Beginner to Advanced',
        'institute': 'Duke University',
        'link': 'https://www.coursera.org/account/accomplishments/certificate/89XDE6EX5D4N'
    },
    {
        'title': 'Foundations of Project Management', 
        'point': 'Foundations in Agile project management and workflows',
        'institute': 'Google',
        'link': 'https://www.coursera.org/account/accomplishments/certificate/JAJWYPVPN3FE'
    },
    {
        'title': 'Creative Thinking: Techniques and Tools for Success', 
        'point': 'Creative thinking Techniques, approaches for industrial innovation and purpose',
        'institute': 'Imperial College London',
        'link': 'https://www.coursera.org/account/accomplishments/certificate/72VJ885W4Y2A'
    },
]


def send_simple_message(message):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxf12ef57048c24f6d8a8787c9617006d8.mailgun.org/messages",
		auth=("api", "4108a54fc0010a5e48f33ab3f24456d8-8d821f0c-24891c6e"),
		data={"from": "Jofin F Archbald <mailgun@sandboxf12ef57048c24f6d8a8787c9617006d8.mailgun.org>",
			"to": ["jofinfab@gmail.com"],
			"subject": "PORTFOLIO FEEDBACK🚨",
			"text": message})

def index(request):
    page = 'Home'
    return render(request, 'index.html', {'page': page})

def about(request):
    page = 'About'
    return render(request, 'about.html', {'page': page})

def projects(request):
    page = 'Projects'
    
    return render(request, 'projects.html', {'page': page, 'projects': Projects})



def certificates(request):
    page = 'Certificates'
    return render(request, 'certificates.html', {'page': page, 'certificates': Certi})


def resume(request):
    page = 'Resume'
    return render(request, 'resume.html', {'page': page})


def contact(request):
    page = 'Contacts'
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        MESSAGE = f"NAME : {name}\nEMAIL : {email}\nSUBJECT : {subject}\nMESSAGE : {message}"
        
        send_simple_message(MESSAGE)
        message = 'Email sent! Will contact you soon!'
        print('Mail sent ', message)
        return render(request, 'contact.html', {'page': page, 'message': message})
        
    print('contact?')
    return render(request, 'contact.html', {'page': page, 'message': ''})
