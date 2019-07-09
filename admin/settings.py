import os
import logging

# Env's
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'uakari')
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'uakari_user')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS', None)
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = int(os.environ.get('POSTGRES_PORT', '5432'))
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))
REDIS_PASS = os.environ.get('REDIS_PASS', None)
SENTRY_DSN = os.environ.get('SENTRY_DSN', '')
LOGGING_LEVEL = os.environ.get('DJANGO_LOGGING_LEVEL', 'INFO')
LOGGING_HANDLER = os.environ.get('LOGGING_HANDLER', 'console')
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'amqp://')

# Base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'q84cil#_6g7w4a5h-s2eimms$k-r^r*1^b1g=s5y6*yc5bszz%'
DEBUG = True
ALLOWED_HOSTS = ['*']
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
RAVEN_CONFIG = {'dsn': SENTRY_DSN}

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASS,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT
    }
}

# WEBDAV Settings
DEFAULT_WORKDIR = 'uakari'
WEBDAV_URL = os.environ.get('WEBDAV_URL', 'https://en1suzv3mklsy.x.pipedream.net/')
WEBDAV_PUBLIC_URL = WEBDAV_URL

# Web
WSGI_APPLICATION = 'uakari.wsgi.application'
ROOT_URLCONF = 'uakari.urls'

# Static
STATIC_URL = '/static/'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': False,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader'
        ],
    },
}]

# Apps and middleware
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uakari',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Logging

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'full_info',
        },
    },
    'formatters': {
        'full_info': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'loggers': {
        'uakari': {
            'handlers': [LOGGING_HANDLER],
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
        'celery': {
            'handlers': [LOGGING_HANDLER],
            'level': LOGGING_LEVEL,
            'propagate': True,
        }
    }
}

