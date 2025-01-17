#!/bin/sh

set -e
neofetch --ascii qnode_art.txt --ascii_colors 2 222 3 2 2 -L, --logo && \
#go get github.com/mailhog/mhsendmail && \
#cp /root/go/bin/mhsendmail /usr/bin/mhsendmail && \
#echo 'sendmail_path = /usr/bin/mhsendmail --smtp-addr mailhog:1025' > /usr/local/etc/php/php.ini
NODE_NAME="qnd41app"
DJANGO_SETTINGS_MODULE="qnd41app.settings.pro"
APP_PORT=${PORT:-9000}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"smartquail.info@gmail.com"}

#rm /py/lib/python3.10/site-packages/baton/static/baton/app/dist/baton.min.js
#cp -f /qnd0.0_app_stg/qnd00_app_stg/baton.min.js /py/lib/python3.10/site-packages/baton/static/baton/app/dist/
python manage.py migrate --settings=$NODE_NAME.settings.pro --noinput 
python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
python manage.py collectstatic --settings=$NODE_NAME.settings.pro --noinput 
#cp -f /qnode4.1_app/qnode41_app/baton.min.js /qnode4.1_app/qnode41_app/qnode41_app/staticfiles/baton/app/dist/
#python manage.py makemessages
#python django-admin makemessages --all
#python django-admin compilemessages 

uwsgi --socket :9000  --workers 9 --master --enable-threads --module $NODE_NAME.wsgi  --ini uwsgi_stage.ini --static-map /static=/qnd41app/qnd41app/qnd41app/static/

#python manage.py listen_port25 --noinput

#gunicorn --worker-tmp-dir /dev/shm  --bind "0.0.0.0:${APP_PORT}"  qnode0_app.wsgi:application 