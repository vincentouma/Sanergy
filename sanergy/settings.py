"""
Django settings for sanergy project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# from celery import Celery


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l$^$(_&plghod^x7u9$xqoc7evs(rpsnh2i&273819t)=24_3_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

######## C2B MPESA DETAILS.#########

#Consumer Secret
MPESA_C2B_ACCESS_KEY = 'ZGWH5CJonGUS9C7eRzvkQGgzMJShHaDD'
# Consumer Key
MPESA_C2B_CONSUMER_SECRET = 'fcobUM436AD9TwyB'
# Url for registering your paybill replace it the url you get from safaricom after you have passed the UATS
C2B_REGISTER_URL = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
#ValidationURL
# replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_VALIDATE_URL = 'http://mpesa.ngrok.io/mpesa/c2b/validate'
#ConfirmationURL
# replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_CONFIRMATION_URL = 'http://mpesa.ngrok.io/mpesa/c2b/confirmation'
#ShortCode (Paybill)
C2B_SHORT_CODE = '600000'
#ResponseType
C2B_RESPONSE_TYPE = 'Completed'

# C2B (STK PUSH) Configs
# https://developer.safaricom.co.ke/lipa-na-m-pesa-online/apis/post/stkpush/v1/processrequest

# Url for sending the STK push request replace it the url you get from safaricom after you have passed the UATS
C2B_ONLINE_CHECKOUT_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
# Where the Mpesa will post the response
#replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_ONLINE_CHECKOUT_CALLBACK_URL = 'http://mpesa.ngrok.io/mpesa/c2b/online_checkout/callback'
# TransactionType
C2B_TRANSACTION_TYPE = 'CustomerPayBillOnline'
# The Pass Key provided by Safaricom when you pass UAT's
# See https://developer.safaricom.co.ke/test_credentials
C2B_ONLINE_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
# Your Paybill
C2B_ONLINE_SHORT_CODE = '174379'

# URL generate OAUTH token
# See https://developer.safaricom.co.ke/oauth/apis/get/generate-1
GENERATE_TOKEN_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


# number of seconds from the expiry we consider the token expired the token expires after an hour
# so if the token is 600 sec (10 minutes) to expiry we consider the token expired.
TOKEN_THRESHOLD = 600

...
#CELERY SETTINGS
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'

# Application definition

INSTALLED_APPS = [
    'sanitation',
    'bootstrap3',
    'bootstrap4',
    'rest_framework',
    'mpesa_api.core',
    'mpesa_api.util',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sanergy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sanergy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sanergy',
        'USER': 'moringa',
    'PASSWORD': 'vinceobindi1005',

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),

)


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
