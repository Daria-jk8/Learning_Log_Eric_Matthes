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
