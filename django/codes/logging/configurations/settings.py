import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sgn#kh82*#65patd=)7be(mscf)!n7=*whey$_rano@rm5(-h6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apm.apps.ApmConfig',
    'elasticapm.contrib.django'
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

ROOT_URLCONF = 'configurations.urls'

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

WSGI_APPLICATION = 'configurations.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'practice_db',
        'USER': 'root',
        'PASSWORD': 'root',
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# elastic apm server configurations
ELASTIC_APM = {
    'SERVER': 'http://localhost:8200',
    'SERVICE_NAME': 'django_division_service'
}

# Logging configurations
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'logging_formatter': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'elasticapm': {
            'level': 'ERROR',
            'class': 'elasticapm.contrib.django.handlers.LoggingHandler',
            'formatter': 'logging_formatter'
        },
        # 'console': {
        #     'level': 'INFO',
        #     'class': 'logging.StreamHandler',
        #     'formatter': 'logging_formatter'
        # },
        # 'file': {
        #     'level': 'INFO',
        #     'class': 'logging.FileHandler',
        #     'formatter': 'logging_formatter',
        #     'filename': 'division_logs'
        # }
    },
    'loggers': {
        'apm_logger': {
            'level': 'ERROR',
            'handlers': ['elasticapm'],
            'propagate': False
        }
        # 'logger': {
        #     'level': 'INFO',
        #     'handlers': ['console', 'file'],
        #     'propagate': False
        # }
    }
}
