import os
import sys

def main():
    # Definir explícitamente el módulo de configuración a utilizar
    settings_module = 'qnd41app.settings.pro'  # Aquí defines de forma explícita el módulo de configuración pro.

    # Establecer la variable de entorno DJANGO_SETTINGS_MODULE
    # Esto le dice a Django qué archivo de configuración utilizar para este entorno.
    os.environ['DJANGO_SETTINGS_MODULE'] = settings_module

    # Ahora que ya hemos configurado el módulo de settings, ejecutamos el comando de Django
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
