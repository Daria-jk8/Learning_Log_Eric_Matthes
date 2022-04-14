:star: Eric Matthes 

### Python Crash Course,  2nd Edition: A Hands-On, Project-Based Introduction To Programming 
--------
## Project 3  :fire: --> Learning Log
-------
 - Python, Django
 - ....
-------
## Result :
-------
##  ACTION PLAN:
```bash
python3 -m venv ll_env
source ll_env/bin/activate
pip install django
python3 -m pip install --upgrade pip
django-admin startproject learning_log . # don't use django-admin.py
ls learning_log     # __init__.py  asgi.py  settings.py  urls.py  wsgi.py
python manage.py migrate # creat db.sqlite
python manage.py runserver # check project in your system
```
### start work with APP...
```bash
python manage.py startapp learning_logs
ls learning_logs 
""" __init__.py  admin.py  apps.py  migrations  models.py  tests.py  views.py"""
```
### add info to models.py class Topic. 
### add app to settings.py
```bash
python manage.py makemigrations learning_logs
python manage.py migrate
```
### create superuser
```bash
python manage.py createsuperuser
```
### add info to admin.py: register model in the site TOPIC
### add info to models.py class Entry
```
python manage.py makemigrations learning_logs
```
### add info to admin.py: register model in the site TOPIC, ENTRY 
### add info to urls.py path('', include('learning_logs.urls'))
### create new file urls.py in the app, and add info 
## add files to folder templates
<<<<<<< HEAD
# --> start chapter 19:
- create forms.py for topic, entry
- urls.py --> new_topic, new_entry
- views.py --> new_topic, new_entry
- html --> create new_topic, new_entry 
- html --> topics - add href a new topic, topic - add href a new entry
- urls.py --> edit_entry
- views.py --> create def edit_entry
- html --> create edit_entry
- html --> topic - add href a edit_entry
### CREATE user`s page
```bash
python manage.py startapp users 
```
### settings.py - add to APPS - 'users'
### urls.py - add 'users.urls'
- create new file in users: urls.py and add info
- create new folders templates, registration
- html - login, logged_out
### create PAGE FOR registration
- urls.py  - add register
- vies.py - create def register
- html - create register.html
- add href to register in  base.html
### data editing with decorators @login_required
- add learning_logs - views.py -@login_required
- settings.py - add LOGIN_URL = '/users/login/'
- add learning_logs - models.py --> User
```bash
python manage.py shell
>>> from django.contrib.auth.models import User 
>>> User.objects.all()
>>> for user in User.objects.all():
...   print(user.username, user.id)
>>> exit()
python manage.py makemigrations learning_logs
>>> 1
>>> 1
python manage.py migrate
=======
>>>>>>> 497dc63f40e0af7ff6e1cd5e32dab1c8093b71d7
