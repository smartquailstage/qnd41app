#!/bin/sh

# Configuración para que el script falle en caso de error
set -e

# Mostrar información del sistema (si neofetch está disponible, si no, se elimina o reemplaza por una salida simple)
if command -v neofetch > /dev/null 2>&1; then
    neofetch --ascii qnode_art.txt --ascii_colors 2 222 3 2 2 -L, --logo
else
    echo "neofetch no está instalado, omitiendo la visualización ASCII."
fi

# Variables de configuración
SETTINGS_MODULE="qnd41app.settings.pro"
NODE_NAME="qnd41app"
DJANGO_SETTINGS_MODULE="qnd41app.settings.pro"
APP_PORT=${PORT:-9000}  # Asegúrate de que esta variable esté configurada en tu entorno Kubernetes
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"smartquail.info@gmail.com"}

# Realiza las migraciones de la base de datos (sin necesidad de intervención del usuario)
echo "Realizando migraciones..."
python3 manage.py migrate --settings=$NODE_NAME.settings.pro --noinput

# Crea el superusuario si no existe. Si ya existe, no causa un error
echo "Creando superusuario si no existe..."
python3 manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

# Recolecta los archivos estáticos de Django (sin necesidad de intervención del usuario)
echo "Recolectando archivos estáticos..."
python3 manage.py collectstatic --settings=$NODE_NAME.settings.pro --noinput

# Verificar si el archivo uwsgi_stage.ini está disponible antes de iniciar el servidor
if [ ! -f "uwsgi_stage.ini" ]; then
    echo "Error: El archivo uwsgi_stage.ini no existe."
    exit 1
fi

# Inicia el servidor uWSGI
echo "Iniciando uWSGI..."
uwsgi --workers 2  --master  --enable-threads  --module $NODE_NAME.wsgi  --ini uwsgi_stage.ini

# Opcional: Gunicorn (descomentado si lo necesitas en lugar de uWSGI)
# gunicorn --worker-tmp-dir /dev/shm --bind "0.0.0.0:${APP_PORT}" qnode0_app.wsgi:application
