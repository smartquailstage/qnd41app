from .base_prod import *



DEBUG=True

ALLOWED_HOSTS = ['*']


#import wagtail_ai

#WAGTAIL_AI_PROMPTS = wagtail_ai.DEFAULT_PROMPTS + [
#    {
#        "label": "Simplify",
#        "description": "Rewrite your text in a simpler form",
#        "prompt": "Rewrite the following text to make it simper and more succinct",
#        "method": "replace",
#    }
#]


#CSRF_COOKIE_DOMAIN=".www.smartquail.io"
#CSRF_COOKIE_SECURE = True
#CSRF_TRUSTED_ORIGINS = ['https://www.smartquail.io','https://146.190.164.22']
#CORS_ALLOWED_ORIGINS = [
#    'https://www.smartquail.io','https://146.190.164.22'
#    # Otros orígenes permitidos si los hay
#]

BATON = {
    'SITE_HEADER': '<a href="#"><img src="/static/img/m2.png" height="26px"></a>',
    'SITE_TITLE': 'The Smartest IT Business Analytics',
    'INDEX_TITLE': 'SmartBusinessAnalytics by SmartQuail',
    'SUPPORT_HREF': '#',
    'COPYRIGHT': '<a href="#"><img src="/static/img/m2.png" height="18px"></a>&nbsp;&nbsp; copyright © 2024', # noqa
    'POWERED_BY': '<a href="#"><img src="/static/img/logo_smartquailgray.png" height="13px"</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': True,
    'MENU_TITLE': 'Todo en Orden',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/img/login_splash.jpg',
   
    'MENU': (
       
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
         { 'type': 'title', 'label': 'Dirección Espacio Público', 'apps': ('auth','todo_en_orden', ) },
         {
            'type': 'app',
            'name': 'actividades_espacio_publico',
            'label': 'Propuestas',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'subject',
                    'label': 'Administración de eventos'
                },
                {
                    'name': 'evento_30000',
                    'label': 'Evento 30000'
                },
                 {
                    'name': 'evento_20000',
                    'label': 'Evento 20000'
                },
                {
                    'name': 'evento_10000',
                    'label': 'Evento 10000'
                },
                {
                    'name': 'evento_5000',
                    'label': 'Evento 5000'
                },
              
            )
        },
         { 'type': 'title', 'label': 'Dirección Creatividad & Fomento', 'apps': ('auth','todo_en_orden', ) },
        {
            'type': 'app',
            'name': 'editorial_literaria',
            'label': 'Editorial & literario',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'subject',
                    'label': 'Categorías de convocatorias'
                },
                {
                    'name': 'course',
                    'label': 'Convocatorias realizadas'
                },
                
                {
                    'name': 'module',
                    'label': 'Bases técnicas inscriptas en convocatorias'
                },
              
            )
        },
         {
            'type': 'app',
            'name': 'proyectos',
            'label': 'Proyectos postulados',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'subject',
                    'label': 'Volumenes editoriales'
                },
                {
                    'name': 'project',
                    'label': 'Proyectos editoriales '
                },
            )
        },

         { 'type': 'title', 'label': 'Administración de perfiles', 'apps': ('auth','todo_en_orden', ) },
              {
            'type': 'app',
            'name': 'usuarios',
            'label': 'Administración de usuarios',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'profile',
                    'label': 'Perfil de usuarios'
                },
                {
                    'name': 'contacts',
                    'label': 'Perfil de contactos'
                },
                {
                    'name': 'legal',
                    'label': 'Perfil de personería'
                },
                {
                    'name': 'activity',
                    'label': 'Perfil de actividad cultural'
                },
                {
                    'name': 'declaracionveracidad',
                    'label': 'declaratorias'
                },
            )
        },
         { 'type': 'title', 'label': 'Comunicación', 'apps': ('auth','todo_en_orden', ) },
         {
            'type': 'app',
            'name': 'usuarios',
            'label': 'Información y Normativas',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'dashboard',
                    'label': 'Pagina de Inicio'
                },
                {
                    'name': 'privacypolicy',
                    'label': 'Políticas de privacidad Fomento editorial'
                },
                {
                    'name': 'termsofuse',
                    'label': 'Condiciones de uso Fomento editorial'
                },

                {
                    'name': 'activityprivacypolicy',
                    'label': 'Políticas de privacidad Espacio público'
                },
                 {
                    'name': 'activitytermsofuse',
                    'label': 'Condiciones de uso Espacio público'
                },


            )
        },        
    ),
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Obtención de variables de entorno para la configuración de PostgreSQL
DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_ENGINE = os.environ.get("POSTGRES_ENGINE")

# Verificación de disponibilidad de las variables necesarias para PostgreSQL
DB_IS_AVAILABLE = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])

# Configuración condicional para PostgreSQL
if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': DB_DATABASE,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }

#Static files DevMod





from .cdn.conf import * #noqa




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# celery setup



#Email setups
EMAIL_HOST          = os.environ.get('EMAIL_HOST')
EMAIL_PORT          =  os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER ')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS       = False
#EMAIL_USE_SSL       = False


REDIS_HOST=os.environ.get('REDIS_HOST')
REDIS_PORT=os.environ.get('REDIS_PORT')
REDIS_DB =os.environ.get('REDIS_DB')  

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


# social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET =  os.environ.get('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ')


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


# Configuración de AWS
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL")  # Cambia si usas otro endpoint
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"  # Cambia a 'private' si los archivos deben ser privados
}

# Configuración de almacenamiento
AWS_LOCATION = os.environ.get("AWS_LOCATION")  # 'static' o 'media'

# Asegúrate de que la URL de los archivos estáticos esté correcta
STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'