import os
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
ALLOWD_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'myapp'
]

# MIDDLEWARE = [...]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}