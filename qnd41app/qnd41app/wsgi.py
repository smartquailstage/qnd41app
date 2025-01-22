"""
WSGI config for qnode30_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import pathlib
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Establecer la ruta al archivo .env en la carpeta de settings
CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
env_path = CURRENT_DIR / '.env_pro'
load_dotenv(dotenv_path=env_path)

# Establecer el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qnd41app.settings.pro')

# Crear la aplicación WSGI
application = get_wsgi_application()
