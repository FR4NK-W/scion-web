"""
Django settings for web_scion project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from os.path import dirname as dir
from django.contrib import messages
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

WEB_SCION_DIR = dir(dir(dir(os.path.abspath(__file__))))
SCION_ROOT = dir(WEB_SCION_DIR)
sys.path.insert(0, SCION_ROOT)

# for users who don't dynamically add content root to their PATHONPATH
sys.path.insert(1, dir(SCION_ROOT))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'ad_manager',
    'guardian',

    # Two-factor authentication
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Two-factor authentication
    'django_otp.middleware.OTPMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)

ROOT_URLCONF = 'web_scion.urls'

WSGI_APPLICATION = 'web_scion.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'ad_manager.context_processors.account_urls',
)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# For django-guardian
ANONYMOUS_USER_ID = -1

ENABLED_2FA = False

# 2FA options
TWO_FACTOR_PATCH_ADMIN = ENABLED_2FA

# Security settings
CSRF_COOKIE_HTTPONLY = True
