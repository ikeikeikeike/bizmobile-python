import os

ADMINS = (
    ('test@example.com', 'BizMo Kun'),
)

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_PATH, 'media'))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'python_bizmobile.db'
TEST_DATABASE_NAME = 'python_bizmobile-test.db'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'TEST_NAME': TEST_DATABASE_NAME,
    }
}


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_BACKEND = 'locmem://'
SECRET_KEY = 'verysecret'

# to make sure timezones are handled correctly in Django>=1.4
#USE_TZ = True
