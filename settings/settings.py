"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""


import json
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# from django.core.serializers import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    with open(os.path.join(BASE_DIR, 'conf', 'secrets.json')) as handle:
        SECRETS = json.load(handle)
except IOError:
    SECRETS = {
        'secret_key': 'a'
    }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j=li!gc8v(bn^f+6q@_$^zu8zfq=zxzipkpzun!y(0sbyn=csr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# DEBUG = False необходимо добавить домен сайта
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние утилиты
    'admin_reorder',
    'easy_thumbnails',

    # пользовательские приложения
    'common',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'pyproject',
#         'USER':'python',
#         'HOST':'localhost',
#         'PASSWORD':'qaz1986qaz',
#         'PORT':'3306',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SECRETS.get('db_name', ''),
        'USER': SECRETS.get('db_user', ''),
        'HOST': SECRETS.get('db_host', ''),
        'PASSWORD': SECRETS.get('db_password', ''),
        'PORT': SECRETS.get('db_port', ''),
    },
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
from django.conf.locale.ru import formats as ru_format

ru_format.DATETIME_FORMAT = "d.m.Y H:i:s"

I18N_PREFIX_DEFAULT_LANGUAGE = False

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#----------------------------
# Настройки easy-thumbnails |
#----------------------------

THUMBNAIL_BASEDIR = 'thumbs'
THUMBNAIL_NAMER = 'easy_thumbnails.namers.hashed'
THUMBNAIL_ALIASES = {
    '': {
        'large': {'size': (1920, 1080), 'crop': False},
        'middle': {'size': (800, 600), 'crop': True},
        'small': {'size': (320, 280), 'crop': True},
    },
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#----------------------------------
# Настройки панели администратора |
#----------------------------------

ADMIN_REORDER = (
    # Навигационное меню
#     {'app': 'menus', 'models': ('menus.Menu', )},
# 'redirects.Redirect', )},

)
