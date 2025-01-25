#!/bin/sh

# Configuración para que el script falle en caso de error
set -e

# Mostrar información del sistema con Neofetch (usa un archivo de arte ASCII específico)
neofetch --ascii qnode_art.txt --ascii_colors 2 222 3 2 2 -L, --logo

# Variables de configuración
SETTINGS_MODULE="qnd41app.settings.pro"
NODE_NAME="qnd41app"
DJANGO_SETTINGS_MODULE="qnd41app.settings.pro"
APP_PORT=${PORT:-9000}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"smartquail.info@gmail.com"}

# Realiza las migraciones de la base de datos (sin necesidad de intervención del usuario)
python3 manage.py migrate --settings=$NODE_NAME.settings.pro --noinput

# Crea el superusuario si no existe. Si ya existe, no causa un error
python3 manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

# Recolecta los archivos estáticos de Django (sin necesidad de intervención del usuario)
python3 manage.py collectstatic --settings=$NODE_NAME.settings.pro --noinput

# Inicia el servidor uWSGI
uwsgi --workers 2 \
      --master \
      --enable-threads \
      --module $NODE_NAME.wsgi \
      --ini uwsgi_stage.ini \
      --static-map /static=/qnd41app/qnd41app/qnd41app/static/

# Opcional: Gunicorn (descomentado si lo necesitas en lugar de uWSGI)
# gunicorn --worker-tmp-dir /dev/shm --bind "0.0.0.0:${APP_PORT}" qnode0_app.wsgi:application
