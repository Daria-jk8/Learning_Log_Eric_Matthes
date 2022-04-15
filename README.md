# :star: Eric Matthes 

### Python Crash Course,  2nd Edition: A Hands-On, Project-Based Introduction To Programming 

## Project 3  :fire: --> Learning Log
 - Python, Django, apps, superuser, URL, .html, GET, POST, @login_required, Bootstrap, 404, 500, Heroku
 - topic, entry 
-------
## RESULT: 
 > You can visit --> [learning-log-2227.herokuapp.com/](https://learning-log-2227.herokuapp.com/)

###  ACTION PLAN:

>> additional source of information https://www.djangoproject.com/

Project architecture:
```bash
Learning_Log_Eric_Matthes/     # root directory is a container for your project
│
├── learning_log/              # with your virtual environment set up and activated and Django installed, you can create a project
│   ├── __init__.py            # an empty file that tells Python that this directory should be considered a Python package
│   ├── asgi.py                # an entry-point for ASGI-compatible web servers to serve your project
│   ├── settings.py            # settings/configuration for this Django project
│   ├── urls.py                # the URL declarations for this Django project; a “table of contents” of your Django-powered site. 
│   └── wsgi.py                # an entry-point for WSGI-compatible web servers to serve your project
│ 
├── learning_logs/             # directory is the actual Python package for your 1st app
│   │
│   ├── migrations/            # Migrations are Django’s way of propagating changes you make to your models          
│   │   └── __init__.py          # (adding a field, deleting a model, etc.) into your database schema. 
│   │
│   ├── __init__.py            # Python uses this file to declare a folder as a package, which allows Django to use code from different apps 
│   │                            # to compose the overall functionality of your web application. won’t have to touch this file
│   ├── admin.py               # file is used to display your models in the Django admin panel. You can also customize your admin panel.
│   ├── apps.py                # file is created to help the user include any application configuration for the app. 
│   ├── models.py              # declare your app’s models in this file, which allows Django to interface with the database of your web application
│   ├── tests.py               # When you’re writing new code, you can use tests to validate your code works as expected.
│   └── views.py               # the code logic of your app in this file
│   └── urls.py                # the URL declarations for app
│   └── forms.py               # preparing and restructuring data to make it ready for rendering; 
│   │                            # creating HTML forms for the data;
│   │                            # receiving and processing submitted forms and data from the client;
│   │
│   │
│   ├── templates/             # Templates - being a web framework, Django needs a convenient way to generate HTML dynamically.                         
│       │                         # The most common approach relies on templates.
│       ├──learning_logs/
│          └── base.html             
│          └── index.html
│          └── topics.html
│          └── topic.html
│          └── new_topic.html
│          └── new_entry.html
│          └── edit_entry.html
│
├── templates/                 # for error 
│   └── 404.html               # to indicate that the browser was able to communicate with a given server, but couldn`t find what was requested. 
│   └── 500.html               # the server not knowing what to do
│ 
│
│
├── users/                     # directory is the actual Python package for your 2nd app
│   │
│   ├── migrations/                   
│   │   └── __init__.py          
│   │
│   ├── __init__.py                                
│   ├── admin.py               
│   ├── apps.py                
│   ├── models.py              
│   ├── tests.py               
│   └── views.py               
│   └── urls.py                                                        
│   │
│   ├── templates/                                  
│       │                        
│       ├──registration/
│          └── login.html             
│          └── logged_out.html
│          └── register.html
│
│
└── manage.py                  # a command-line utility that lets you interact with this Django project in various ways
│   
└── requirements.txt           # pip freeze > requirements.txt in the command line to generate a requirements.txt file for your project
│                                 # keep existing version specifier if it matches the current version
│                                
└──Procfile                   # Heroku apps include a Procfile that specifies the commands that are executed by the app on startup... app’s web server
│                                
└──runtime.txt                # Heroku -  to specify the Python runtime environment, the exact version number to use is announced
│                                
└──README.md                  # instruction, notes 










