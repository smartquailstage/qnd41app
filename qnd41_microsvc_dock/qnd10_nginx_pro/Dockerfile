FROM nginxinc/nginx-unprivileged:1.24.0-alpine-slim

# Copiar archivos de configuración de Nginx
COPY ./nginx/* /etc/nginx/

# Copiar certificados SSL y asegurarse de que sean legibles
COPY ./ssl-certs-smartquail/* /etc/nginx/
COPY ./ssl-certs-smartquail/https/www.smartquail.io/* /etc/letsencrypt/live/www.smartquail.io/

# Copiar el script de inicio
COPY ./nginx/run.sh /run.sh

# Configurar variables de entorno
ENV DOMAIN=smartquail.io
ENV LISTEN_PORT=80
ENV NGINX_PROXY=http://qnd41app:9000
ENV APP_HOST=qnd41app
ENV APP_PORT=9000

# Cambiar al usuario root para instalar paquetes y modificar permisos
USER root

# Instalar herramientas necesarias y ajustar permisos
RUN apk add --no-cache openssl bash && \
    chmod +x /run.sh && \
    # Crear directorios necesarios y ajustar permisos
    mkdir -p /qnd41app/qnd41app/qnd41app/staticfiles && \
    chmod 755 /qnd41app/qnd41app/qnd41app/staticfiles && \
    mkdir -p /qnd41app/qnd41app/qnd41app/media && \
    chmod 755 /qnd41app/qnd41app/qnd41app/media && \
    mkdir -p /qnd41app/qnd41app/qnd41app/static && \
    chmod 755 /qnd41app/qnd41app/qnd41app/static && \
    # Ajustar permisos de certificados
    chmod -R 600 /etc/letsencrypt/live && \
    chmod -R 700 /etc/letsencrypt/ && \
    chown -R nginx:nginx /etc/letsencrypt/live && \
    chown -R nginx:nginx /etc/letsencrypt

# Definir volúmenes para directorios específicos
VOLUME /qnd41app/qnd41app/qnd41app/staticfiles
VOLUME /qnd41app/qnd41app/qnd41app/media
VOLUME /qnd41app/qnd41app/qnd41app/static
VOLUME /vol/www
VOLUME /vol/proxy
VOLUME /etc/letsencrypt

# Ejecutar el script de inicio
CMD ["/run.sh"]
