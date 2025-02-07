

import os
from pathlib import Path
from dotenv import load_dotenv
#prueba
BASE_DIR = Path(__file__).resolve().parent.parent


# Load environment variables from the .env_local file.
ENV_FILE_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_FILE_PATH)

# Retrieve the Django secret key from environment variables.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Optionally, you can add a default value or raise an exception if SECRET_KEY is not set
if SECRET_KEY is None:
    raise ValueError("DJANGO_SECRET_KEY is not set in the environment variables.")




# Application definition

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",
    #'usuarios',
    #'baton',
    #'editorial_literaria',
    #'account',
    #'courses',
    #'courses_exams',
    #'card_test',
    #'thumbnails',
    #'cart',
   
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   # 'django.contrib.sites',
    #'django_comments',
    #Wagtail Inicials
    'core',
    
    #'wagtail',
    'wagtail',
    'wagtailmedia',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'django.contrib.humanize',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    
    'wagtail.locales',
    'rosetta',
    #'wagtail.contrib.settings',
    
    'wagtail.admin',
   # 'wagtail.core',
   # 'wagtail.contrib.settings',
    'wagtail.contrib.routable_page',
    #'wagtail.contrib.modeladmin',
    #'wagalytics',
    #'wagtailfontawesome',
    "wagtail_localize",
    #"wagtail_localize.locales",
    #'wagtail_ai',
    'wagtailgmaps',
    'wagtailmenus',
    #'wagtail.contrib.modeladmin',
    'django_social_share',
   
    'taggit',
    #'proyectos',
   # 'students',
  #  'webapp_0',
   # 'actividades_espacio_publico',
  #  'streams',
    'widget_tweaks',
    'django_forms_bootstrap',

   # 'datetimewidget',
   #SMARTQUAIL-BUSINESS-CONSULTING
    #'shop',
    #'coupons',
    #'cart',
    #'todo_en_orden',
    #'coupons',
    #'orders',
    #'contracts',
    #'services',
    #'cart',
    #'cart_c',
    #'payment',
    #'django_phonenumbers',
    #'phonenumber_field',
    #'shop',
    #'cart',

    'sblcart',
    'sblshop',
    'sblorders',

    
    'sbtcart',
    'sbtshop',
    'sbtorders',

    'sbmcart',
    'sbmshop',
    'sbmorders',

    'sbacart',
    'sbashop',
    'sbaorders',

    'bootstrap4',
    'webapp',
    'social_django',
    'sorl.thumbnail',
    #'students',
    'embed_video',
    'qr_code',
    'storages',
    #'actions',
    'boto3',
   
    #'memcache_status',
    'rest_framework',
    'ckeditor',
   # 'js_blog_app',
    'wagtail.contrib.settings',
    
    "bootstrap_datepicker_plus",
    
    #'baton.autodiscover',
   
]


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



MIDDLEWARE = [
    #'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    #'wagtail.core.middleware.site.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]






ROOT_URLCONF = 'qnd41app.urls'
LOCALE_PATHS =  (
    os.path.join(BASE_DIR, 'locale/'),
)

#WAGTAIL SETUPS
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}
#SITE_ID = 1
#WagtailAnalitycs
GA_KEY_CONTENT = os.environ.get('GA_KEY_CONTENT_ENV')
GA_VIEW_ID = os.environ.get('GA_VIEW_ID_ENV')


WAGTAIL_SITE_NAME = 'Smart Business Media'

#RESTFRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

#Redis Setup




#DJANGO ADMIN SETUPS

#LOGINGS REDIRECT

#LOGIN_REDIRECT_URL = 'accounts:dashboard'
#LOGIN_URL = 'login'
#LOGOUT_URL = 'logout'

#from django.urls import reverse_lazy
#LOGIN_REDIRECT_URL = reverse_lazy('course_list')



#WEBAPP SETTINGS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CART_SESSION_ID = 'cart'
SBLCART_SESSION_ID = 'cart'
SBACART_SESSION_ID = 'cart'
SBTCART_SESSION_ID = 'cart'
SBMCART_SESSION_ID = 'cart'

BRAINTREE_MERCHANT_ID = os.environ.get('BRAINTREE_M_ID')
BRAINTREE_PUBLIC_KEY = os.environ.get('BRAINTREE_KEY')
BRAINTREE_PRIVATE_KEY = os.environ.get('BRAINTREE_PRIVATE_KEY')

from braintree import Configuration, Environment
# para desplegar cambiar sandbox con Production
Configuration.configure(
    Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    #'account.authentication.EmailAuthBackend',
    #'social_core.backends.facebook.FacebookOAuth2',
    #'social_core.backends.twitter.TwitterOAuth',
    #'social_core.backends.google.GoogleOAuth2',
]





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
                'wagtailmenus.context_processors.wagtailmenus',
                'wagtail.contrib.settings.context_processors.settings',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'qnd41app.wsgi.application'

WAGTAIL_ADMIN_BASE_URL =  os.environ.get('DOMAINS')
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 5 * 1024 * 1024 * 1024  # 5 GB en bytes
WAGTAILIMAGES_MAX_IMAGE_PIXELS = 1000000000  # 1 millardo de píxeles (1 Gb)





# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


#POSTGRES_READY=str(os.environ.get('POSTGRES_READY_ENV'))





# Configuración de sesiones usando Redis
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"
#SESSION_CACHE_ALIAS = "default"




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

LANGUAGE_CODE = 'es-Ec'
TIME_ZONE = 'America/Guayaquil'




WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),
    ('es', 'Spanish'),
]


WAGTAIL_I18N_ENABLED = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]



USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


MEDIA_URL = "/media/"
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [BASE_DIR / "staticfiles"]  
STATIC_URL = "/static/"
STATIC_ROOT = STATIC_ROOT = BASE_DIR / "static"





