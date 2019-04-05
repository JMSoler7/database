import os

from database.settings.common import *  # NOQA F401,F403
from database.settings.common import SITE_PACKAGE_NAME
from database.settings.common import BASE_DIR
from database.settings.common import INSTALLED_APPS
from database.settings.common import MIDDLEWARE
from database.settings.common import LOGGING
from database.settings.common import REST_FRAMEWORK

SECRET_KEY = 'AIXO_ES_UNA_CLAU_DE_DEVELOPMENT'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
LOGGING['loggers']['']['handlers'] = ['stdout']
LOGGING['loggers'][SITE_PACKAGE_NAME]['level'] = 'DEBUG'

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += (
    'rest_framework.authentication.BasicAuthentication',)
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}
