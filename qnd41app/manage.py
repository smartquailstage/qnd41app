#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pathlib
from dotenv import load_dotenv

# Establecer la ruta al archivo .env en la carpeta de settings
CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
env_path = CURRENT_DIR / '.env_pro'
load_dotenv(dotenv_path=env_path)

def main():
    """Run administrative tasks."""
    # Cargar variables del archivo .env
    load_dotenv()

    # Verificar y establecer DJANGO_SETTINGS_MODULE
    settings_module = os.getenv('DJANGO_SETTINGS_MODULE', 'qnd41app.settings.pro')
    if not settings_module:
        raise RuntimeError("La variable DJANGO_SETTINGS_MODULE no está configurada.")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
