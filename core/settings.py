from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-__2!jo#7n92v7o=2mk_&z-js#e59co)of*y+*p2&5g-685e9tp'

DEBUG = True

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    
    #packages
    
    'mptt',
    'drf_spectacular',
    'rest_framework.authtoken',
    'corsheaders',
    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'versatileimagefield',
    'leaflet',
    'django_admin_geomap',
    
    # apps
    'apps.house',
    'apps.accounts',
    'apps.main',
    'apps.helpers.api',
    'sorl.thumbnail'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'talasbek',
        'PASSWORD': 'bpsyx@MN51',
        'HOST': 'localhost',
        'PORT': '',
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


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / "media"

                    ### DRF SETTINGS ###
                    

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  
    
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Bussines.kg',
    'DESCRIPTION': 'DESCRIPTION....',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
]
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

AUTH_USER_MODEL = "accounts.User"

EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.businesskg@gmail.com"
EMAIL_HOST_PASSWORD = "fozk fuet adlf jqvd"

CELERY_BROKER_URL = "redis://localhost:6379/0"


                    ### LOGGER REQUEST ###
                    

# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'console': {"class": 'logging.StreamHandler'}
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         }
#     }
# }

                    ### WATERMARK CONFIG###
                    
WATERMARK_PATH = 'media/watermark_logo/logo-1.png'

GMAIL_TEMPLATE_ADD = '/home/madalbekovich/MProjects/House.kg/core/apps/helpers/send_mail_house.html'




# HASHED_CODE

HASHID_FIELD_MIN_LENGTH = 25

HASHID_FIELD_LOOKUP_EXCEPTION = False

HASHID_FIELD_SALT = 'EF92B778BAFE771E89245B89ECBC08A44A4E166C06659911881F383D4473E94F'
