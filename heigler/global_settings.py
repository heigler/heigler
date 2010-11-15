# Django settings for heigler project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Heigler', 'heigler@heigler.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'heigler',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MODPATH = os.path.abspath(os.path.dirname(__file__))
abspath = lambda directory: os.path.join(MODPATH, directory)

MEDIA_ROOT = abspath('media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media-admin/'

SECRET_KEY = 'i5k%0wro3v+@2+n*b2)18%#m!c%_m@f6xl$ii4hadr6=u08g4r'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#   'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'heigler.urls'

TEMPLATE_DIRS = (
    abspath('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
)
