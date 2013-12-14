import dj_database_url
from project.settings import *
DEBUG = False
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'pg_9430',                      # Or path to database file if using sqlite3.
#        'USER': 'pg_9430a',                      # Not used with sqlite3.
#        'PASSWORD': 'Slask\ spiewa',                  # Not used with sqlite3.
#        'HOST': 'pysilesia.megiteam.pl',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '5436',                      # Set to empty string for default. Not used with sqlite3.
#        }
#}

DATABASES = {'default': dj_database_url.config()}

CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '91.227.38.24:9000',
            'KEY_PREFIX': 'pysilesia'
        }
}

EMAIL_HOST = 'pysilesia.megiteam.pl'
SERVER_EMAIL = 'noreply@pysilesia.org'
DEFAULT_FROM_EMAIL = 'noreply@pysilesia.org'
EMAIL_HOST_USER = 'noreply@pysilesia.org'
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

COMPRESS_OFFLINE = True

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from local_settings import *
except ImportError:
    pass

ALLOWED_HOSTS = ('pysilesia.org', 'www.pysilesia.org', '2618.rev.megiteam.pl', '.pysilesia.megiteam.pl')

####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
