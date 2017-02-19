# django-practice
Practicing Django

# Installing the django
`pip install django==1.8`

# Check if django is installed
`django-admin --version`

# Create the first project
`django-admin startproject <projectname>`

# Create the first application
`python manage.py startapp <appname>`

# Create a first migration - This also takes the current database snapshot without data.
`python manage.py makemigrations` 

# Migrate the database
`python manage.py migrate`