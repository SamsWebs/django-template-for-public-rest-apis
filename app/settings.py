import os

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY', 'dev-only-insecure-key-change-in-production'
)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = []

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'app.urls'
ASGI_APPLICATION = 'app.asgi.application'

DATABASES = {}

USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ABOUT_MESSAGE = os.environ.get('ABOUT_MESSAGE', '')
