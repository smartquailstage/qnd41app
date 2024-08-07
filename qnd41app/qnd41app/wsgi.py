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

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
load_dotenv(str("ENV_FILE_PATH"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qnd41app.settings.stage')

application = get_wsgi_application()