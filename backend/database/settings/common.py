import os
import sys

from database import __version__
from raven.transport.requests import RequestsHTTPTransport


SITE_PACKAGE_NAME = 'database'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = __version__
LOCAL = os.getenv('DJANGO_LOCAL', default=False)

INSTALLED_APPS = [
    SITE_PACKAGE_NAME,
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_extensions',
    'rest_framework',
    'webpack_loader',
    'raven.contrib.django.raven_compat',
    'dejavu_base',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEBUG = False

ROOT_URLCONF = '{}.urls'.format(SITE_PACKAGE_NAME)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dejavu_base.wsgi.application'

LANGUAGES = [
  ('ca', 'Català'),
  ('es', 'Español'),
  ('en', 'English'),
]


LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = os.getenv('DJANGO_STATIC_URL', default='/static/')
MEDIA_URL = os.getenv('DJANGO_MEDIA_URL', default='/uploads/')
MEDIA_ROOT = os.getenv(
    'DJANGO_MEDIA_ROOT', default=os.path.join(BASE_DIR, 'uploads'))

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    'COERCE_DECIMAL_TO_STRING': False,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'spa'
LOGOUT_REDIRECT_URL = 'spa'
CSRF_USE_SESSIONS = True

JET_DEFAULT_THEME = 'light-gray'
JET_SIDE_MENU_COMPACT = True

EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', default='localhost')
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER', default='admin@calidae')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD', default='pwd')
EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT', default=587)
EMAIL_USE_TLS = os.getenv('DJANGO_EMAIL_USE_TLS', default=False)
EMAIL_USE_SSL = os.getenv('DJANGO_EMAIL_USE_SSL', default=False)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'syslog': {
            'format': (
                '[Django] %(process)d - '
                '%(levelname)s:%(name)s:%(message)s'
            ),
        },
        'debug': {
            'format':
                '%(asctime)s.%(msecs)03d %(levelname)s '
                '[%(name)s:%(funcName)s #%(lineno)s] %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class':
                'raven.contrib.django.raven_compat.'
                'handlers.SentryHandler',
        },
        'syslog': {
            'level': 'NOTSET',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'syslog',
            'address': '/dev/log',
        },
        'stdout': {
            'formatter': 'debug',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
        'null': {
            'formatter': 'syslog',
            'class': 'logging.NullHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['syslog', 'sentry'],
            'level': 'INFO',
        },
        SITE_PACKAGE_NAME: {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
            'qualname': SITE_PACKAGE_NAME,
        },
    }
}

RAVEN_CONFIG = {
    'dsn': os.getenv('DJANGO_SENTRY_DSN', ''),
    'environment': os.getenv('DJANGO_SENTRY_ENVIRONMENT', 'Undefined'),
    'release': VERSION,
    'transport': RequestsHTTPTransport,
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': (
        'dejavu_base.tools.should_show_debug_toolbar')
}

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE", 'django.db.backends.postgresql'),
        'NAME': os.getenv("DB_NAME", 'docker'),
        'USER': os.getenv("DB_USER", 'docker'),
        'PASSWORD': os.getenv("DB_PASSWD", 'docker'),
        'HOST': os.getenv("DB_HOST", 'localhost' if LOCAL else 'db'),
        'PORT': os.getenv("DB_PORT", '54320' if LOCAL else '5432'),
    }
}
