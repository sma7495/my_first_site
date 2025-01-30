from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h$@k()o*cn=o)(c(o=#)*9%uxq(g(fa8!f^pp7m%s385m(ei3v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



#Site ID / 2 : 127.0.0.1
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


INTERNAL_IPS = [

    "127.0.0.1",
]