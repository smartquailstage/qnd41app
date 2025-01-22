#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pathlib
from dotenv import load_dotenv

# Establecer la ruta al archivo .env en la carpeta actual
CURRENT_DIR = pathlib.Path(__file__).resolve().parent
env_path = CURRENT_DIR / '.env_pro'
load_dotenv(dotenv_path=env_path)

def main():
    """Run administrative tasks."""
    # Establecer DJANGO_SETTINGS_MODULE desde el archivo .env o usar un valor predeterminado
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE', 'qnd41app.settings.pro'))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on "
            "your PYTHONPATH. Did you forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
