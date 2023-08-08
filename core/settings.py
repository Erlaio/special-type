import os

from pathlib import Path

from core.settings_ import settings


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = settings.SECRET_KEY.get_secret_value()

DEBUG = settings.DEBUG

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yookassa_payment.apps.YookassaPaymentConfig',
    'api.apps.ApiConfig',
    'adminapp.apps.AdminappConfig',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'rest_captcha'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# SQLite:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Postgres:
DATABASES = {
    'default': {
        'ENGINE': settings.DB_ENGINE,
        'NAME': settings.POSTGRES_DATABASE_NAME,
        'USER': settings.POSTGRES_USER,
        'PASSWORD': settings.POSTGRES_PASSWORD.get_secret_value(),
        'HOST': settings.POSTGRES_HOST,
        'PORT': settings.POSTGRES_PORT
    }
}


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


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/backend_static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'backend_static')

MEDIA_URL = '/backend_media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'backend_media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

API_YOOKASSA_KEY=settings.API_YOOKASSA_KEY

SHOP_ID=settings.SHOP_ID


REST_CAPTCHA = {
    'CAPTCHA_IMAGE_SIZE': (245, 66),
    'CAPTCHA_FONT_SIZE': 30
}