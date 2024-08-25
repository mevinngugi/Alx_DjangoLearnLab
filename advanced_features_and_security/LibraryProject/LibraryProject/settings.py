"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%^_9-mf9-8y_t8kwc=_e0&exrdn+e+!*(nw=+#h%m6(5gug1jx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SECURE_BROWSER_XSS_FILTER = True  # Enables the X-XSS-Protection header
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking by disallowing your site in iframes
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME type sniffing
CSRF_COOKIE_SECURE = True  # Ensures the CSRF cookie is only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
CSP_DEFAULT_SRC = ("'self'",)  # Only allow resources from your own domain
CSP_SCRIPT_SRC = ("'self'", 'https://trustedscripts.com')  # Example to allow scripts from your domain and trusted sources
CSP_STYLE_SRC = ("'self'", 'https://trustedstyles.com')  # Example to allow styles from your domain and trusted sources

ALLOWED_HOSTS = []


# Application definition
# import sys
# sys.path.insert(0, '/Users/mevinngugi/TheForge/ALX-BE-Week11/Alx_DjangoLearnLab/advanced_features_and_security/')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    'csp',
]

#AUTH_USER_MODEL = "relationship_app.CustomUser"
AUTH_USER_MODEL = 'bookshelf.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_project3',
        'USER': 'root',
        'PASSWORD': '5z&^ZwqWKd#9H6',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "home"
#LOGOUT_REDIRECT_URL = "logout/"
