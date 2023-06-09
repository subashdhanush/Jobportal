"""
Django settings for singaporeportal project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from lib2to3.pgen2.token import NAME
from pathlib import Path
import os
import smtplib



# import django
# from django.utils.encoding import force_str
# django.utils.encoding.force_text = force_str


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-52rbpr=dw0c+nqz80+of$gx2%z@6ur&^*2u=@3_3t%#bgx%*w#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'ckeditor',
    'taggit',
    'jobportal',
    'paypal.standard.ipn',
    'social_django',
    # 'hitcount',
    

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'singaporeportal.urls'

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

WSGI_APPLICATION = 'singaporeportal.wsgi.application'

SOCIAL_AUTH_USERNAME_FORM_HTML = 'save_profile.html'


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'jobportal.pipeline.save_profile'
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
         'NAME':'JobList',
         'USER':'postgres',
         'PASSWORD':'subash',
         'HOST':'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
MEDIA_URL='/media/'
STATICFILES_DIR=[

os.path.join(BASE_DIR,'static')

]
STATIC_ROOT=os.path.join(BASE_DIR,'assets')

SOCIALACCOUNT_LOGIN_ON_GET=True

# LOGIN_REDIRECT_URL = '/employerdashboard'
LOGIN_REDIRECT_URL   ='/empregister/'


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '323735035574-pic4adf4nfvnadp7el3e6b0a8mtd2gfp.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}

# STATIC_URL = '/static/'

# STATIC_ROOT=os.path.join(BASE_DIR,'assets')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL="jobportal.User"

# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST='smtp.gmail.com'
# DEFAULT_FROM_EMAIL = 'subashweb03@gmail.com'
# SERVER_EMAIL = 'subashweb03@gmail.com'
# EMAIL_HOST_USER='subashweb03@gmail.com'
# EMAIL_HOST_PASSWORD ='suiwksxodexhezxm'
# EMAIL_PORT=587
# EMAIL_USE_TLS=True


EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
DEFAULT_FROM_EMAIL = 'myjobsg.com@gmail.com'
SERVER_EMAIL = 'myjobsg.com@gmail.com'
EMAIL_HOST_USER='myjobsg.com@gmail.com'
# EMAIL_HOST_PASSWORD ='suiwksxodexhezxm'
EMAIL_HOST_PASSWORD ='ytgrcbwuudzvulrg'
EMAIL_PORT=587
EMAIL_USE_TLS=True




# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST='smtp.outlook.office365.com'
# DEFAULT_FROM_EMAIL = 'myjob@myjob.com.sg'
# SERVER_EMAIL = 'myjob@myjob.com.sg'
# EMAIL_HOST_USER='myjob@myjob.com.sg'
# EMAIL_HOST_PASSWORD ='6CuDvsGNHXkCHrU'
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# FROM_EMAIL = "myjob@myjob.com.sg"

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp-mail.outlook.com'
# EMAIL_HOST_USER = 'myjob@myjob.com.sg'
# EMAIL_HOST_PASSWORD = '6CuDvsGNHXkCHrU'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# server = smtplib.SMTP('smtp.office365.com', 587) 
# server.starttls()
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# SERVER_EMAIL = EMAIL_HOST_USER


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_header": "Admin Panel",

    "welcome_sign": "Welcome to the myjob",
}


#Paypal Settings
PAYPAL_TEST = True

SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'



PAYPAL_RECEIVER_EMAIL='myjobsg.com@gmail.com'

