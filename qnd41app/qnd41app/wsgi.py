import os
from django.core.wsgi import get_wsgi_application

# Obtener la variable de entorno DJANGO_SETTINGS_MODULE, si no está, se usará el valor predeterminado.
settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', 'qnd41app.settings.local')

# Configurar la variable de entorno DJANGO_SETTINGS_MODULE, si no está ya configurada.
os.environ['DJANGO_SETTINGS_MODULE'] = settings_module

application = get_wsgi_application()
