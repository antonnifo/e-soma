import os
from .base import *

DEBUG = True
ALLOWED_HOSTS = []

SECRET_KEY = 'django-insecure-pu7p$-7^*o*3d_5s5^-x+(0pasg8#c&)p9x5_&cdhe-b-#4c8^'

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD':os.getenv('DB_PASSWORD'),
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
}
# python manage.py runserver --settings=engine.settings.local


import mimetypes

mimetypes.add_type('application/javascript', '.js', True)
mimetypes.add_type('text/css', '.css', True)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'