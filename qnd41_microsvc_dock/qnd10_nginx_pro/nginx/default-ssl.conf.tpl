# Configuración del upstream para Django
upstream django {
    # Servidor Unix para el socket de uWSGI
    # server unix:///path/to/your/mysite/mysite.sock; # Para un socket de archivo
    server qnd41app:9000; # Para un socket de puerto web (lo utilizaremos primero)
}



server {
    listen 443 ssl;
    server_name www.${DOMAIN} 143.198.74.196 127.0.0.1;

    ssl_certificate     /etc/letsencrypt/live/www.${DOMAIN}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.${DOMAIN}/privkey.pem;

    include /etc/nginx/options-ssl-nginx.conf;
    ssl_dhparam /vol/proxy/ssl-dhparams.pem;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    # Alias para archivos estáticos
    location /staticfiles {
        alias /qnd41app/qnd41app/qnd41app/staticfiles;
        client_max_body_size 1000M;
    }

    location /media {
        alias /qnd41app/qnd41app/qnd41app/media;
        client_max_body_size 1000M;
    }

    location /static {
        alias /qnd41app/qnd41app/qnd41app/static;
        client_max_body_size 1000M;
    }

    # Configuración para manejar solicitudes al backend de Django
    location / {
        uwsgi_pass qnd41app:9000;
        include /etc/nginx/uwsgi_params;
        client_max_body_size 1000M;

        # Encabezados para CORS
        add_header 'Access-Control-Allow-Origin' 'https://www.smartquail.io';
        add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
        add_header Access-Control-Allow-Headers "Authorization, Content-Type, Accept";
        add_header Access-Control-Allow-Credentials "true";

        proxy_set_header X-Forwarded-Proto https;
    }
}


