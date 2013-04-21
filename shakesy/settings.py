import os
import sys
from os import environ

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
def _rel(*x):
    return os.path.join(PROJECT_ROOT, *x)

DATA_DIR = _rel("experiment_1/data")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Adam Duston', 'aduston@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = _rel("media")
MEDIA_URL = '/media/'
STATIC_ROOT = _rel("collected")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    _rel("static"),
    _rel("jstest/static")
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
)
SECRET_KEY = 'zke6l+5n^ru8m!dou6rl+u)*15ftku)4r!7$!-28o27w05_#u&amp;'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'shakesy.urls'

WSGI_APPLICATION = 'shakesy.wsgi.application'

TEMPLATE_DIRS = (
    _rel("templates"),
    _rel("jstest/templates")
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    "experiment_1",
    "compressor",
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propogate': True
        }
    }
}

INSTALLATION = "local"
DOMAIN = "localhost:8000"
ORIGIN = "http://localhost:8000"


env = environ.get("RACK_ENV", "dev")

if env == "production":
    DEBUG = False
    INSTALLED_APPS += ('gunicorn', 'storages')
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()
    ORIGIN = "http://www.shakesy.com"

    INSTALLATION = "production"

    STATICFILES_STORAGE = 'shakesy.s3utils.StaticS3BotoStorage'
    DEFAULT_FILE_STORAGE = "shakesy.s3utils.MediaS3BotoStorage"

    AWS_STORAGE_BUCKET_NAME = "shakesy"
    AWS_ACCESS_KEY_ID = "AKIAJDPMOLSYHWGM4NYQ"
    AWS_SECRET_ACCESS_KEY = environ.get("AWS_SECRET_ACCESS_KEY", "")

    S3_URL = 'http://s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL + '/static/'
    MEDIA_URL = S3_URL + '/media/'

    COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    COMPRESS_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
