import os
from django.core.wsgi import get_wsgi_application

# Obtener la variable de entorno
settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', 'qnd41app.settings.local')

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()