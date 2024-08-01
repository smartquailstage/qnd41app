# Configuración del upstream para Django
upstream django {
    # Servidor Unix para el socket de uWSGI
    # Puedes usar este socket si prefieres no exponer el puerto en la red
    # server unix:///path/to/your/mysite/mysite.sock;

    # Servidor de red para uWSGI (reemplaza con tu configuración si usas sockets en lugar de puertos)
    server qnd41app:9000; 
}

server {
    listen 443 ssl http2;
    server_name www.${DOMAIN} 143.198.74.196 127.0.0.1;

    ssl_certificate     /etc/letsencrypt/live/www.${DOMAIN}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.${DOMAIN}/privkey.pem;

    include /etc/nginx/options-ssl-nginx.conf;
    ssl_dhparam /vol/proxy/ssl-dhparams.pem;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    # Alias para archivos estáticos
    location /static/ {
        alias /qnd41app/qnd41app/qnd41app/staticfiles/;
        client_max_body_size 1000M;
        access_log off; # Opcional: desactivar el registro de accesos para archivos estáticos
    }

    location /media/ {
        alias /qnd41app/qnd41app/qnd41app/media/;
        client_max_body_size 1000M;
        access_log off; # Opcional: desactivar el registro de accesos para archivos estáticos
    }

    location /static/ {
        alias /qnd41app/qnd41app/qnd41app/static/;
        client_max_body_size 1000M;
        access_log off; # Opcional: desactivar el registro de accesos para archivos estáticos
    }

    # Configuración para manejar solicitudes al backend de Django
    location / {
        uwsgi_pass django;
        include /etc/nginx/uwsgi_params;
        client_max_body_size 1000M;

        # Encabezados para CORS
        add_header 'Access-Control-Allow-Origin' 'https://www.smartquail.io' always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS' always;
        add_header 'Access-Control-Allow-Headers' 'Authorization, Content-Type, Accept' always;
        add_header 'Access-Control-Allow-Credentials' 'true' always;

        proxy_set_header X-Forwarded-Proto https;
    }
}
