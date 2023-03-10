"""
Django settings for cflax project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
# if os.environ.get(' ') == "production":
#     __import__('pysqlite3')
#     import sys
#     sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')


# os.popen("daphne -p 8000 cflax.asgi:application")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b^)0^#wep@eqimws(-o-w3qh@_7h7^2an$4$bp@s$_o=nytm#9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Home',
    'cflax',
    'registration',
    'taxfiling',
    'dashboard',
    'ckeditor',
    'ckeditor_uploader',
    'othernavs',
    'chat',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'dashboard.middleware.simple_middleware',
]

ROOT_URLCONF = 'cflax.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Home.context_processors.regfunc',
            ],
        },
    },
]
sectionname = ["Top Form section","What We Offer","Document","Our Package","Procedure","Memorandum","Time and Fees","FAQS","Signification","Our Clients","Blogs"]
names = ['top','absm','dr','pi','pr','mm','cr','faq','sn','client','blogs']

WSGI_APPLICATION = 'cflax.wsgi.application'
ASGI_APPLICATION = 'cflax.routing.application'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 'full', 
        'width': 'full', 
    },
}
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'
CKEDITOR_UPLOAD_PATH = "uploads/"
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kirnaz',
        'USER': 'userkirnaz', 
        'PASSWORD': 'Flax@2021',
        'HOST': 'localhost',
        'PORT': '3306'
     }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


if os.environ.get('enviorment') == "production":
    DATABASES['default']=  {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kirnaz',
        'USER': 'userkirnaz', 
        'PASSWORD': 'Flax@2021',
        'HOST': 'localhost',
        'PORT': '3306',   #my port is 3306
    }
    # CHANNEL_LAYERS["default"]= {
    #         "BACKEND": "channels_redis.core.RedisChannelLayer",
    #         "CONFIG": {
    #             "hosts": [("127.0.0.1", 6379)],
    #         },
    #     },

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'


MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
