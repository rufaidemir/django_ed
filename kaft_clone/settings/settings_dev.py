from .settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


if os.environ.get('DJANGO_DEBUG')==True:
    INSTALLED_APPS+=  ['django-extensions',]