# Inherit from standard settings file for default
from hellowebapp.settings import *

# Everything below will override our standard settings:

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Set debug to False
DEBUG = False

# Static asset configuration
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'