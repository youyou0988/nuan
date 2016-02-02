"""
Django settings for nuan project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n8kf-7@j8r@by1nt%k!8xga0xpt)4adg(qh9m3-z6x8rsy+a7h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['139.129.130.201']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, "./templates"),)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nuan.urls'

WSGI_APPLICATION = 'nuan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "./static"),

    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

#
# EMAIL_HOST = 'mail.warmframe.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'web@warmframe.com'
# EMAIL_HOST_PASSWORD = 'Liu36363'
# DEFAULT_FROM_EMAIL = 'web@warmframe.com'
# SERVER_EMAIL = 'web@warmframe.com'
#
# EMAIL_USE_TLS = False
# for sending email to register
# EMAIL_HOST = 'smtp.mxhichina.com'
EMAIL_HOST = "smtp.aliyun.com"
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'warmframe@aliyun.com'
# EMAIL_HOST_PASSWORD = 'lIU36363'
EMAIL_HOST_PASSWORD = 'liu36363'
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = False
