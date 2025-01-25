FROM python:3.11-alpine
LABEL maintainer="mau_dev@smartquail.io"

ENV PYTHONUNBUFFERED 1
ENV NODE_VERSION=qnd41app
ENV NODE_APP_NAME=qnd41app
ENV USER=qnd41

# Instalar dependencias necesarias
RUN apk add --no-cache \
    git \
    postgresql-client \
    build-base \
    curl \
    postgresql-dev \
    gcc \
    musl-dev \
    python3-dev \
    linux-headers \
    libffi-dev \
    py3-cffi \
    py3-cryptography \
    jpeg-dev \
    go \
    zlib-dev \
    libjpeg \
    wget \
    fontconfig \
    ttf-freefont \
    font-noto \
    terminus-font \
    gtk+3.0 \
    pango \
    busybox-extras \
    openssl-dev \
    gettext \
   # screenfetch \
    musl musl-utils musl-locales tzdata && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /12012023.txt

# Crear directorios y asignar permisos
RUN mkdir -p /${NODE_VERSION}/${NODE_APP_NAME}/{static,media,staticfiles} && \
    chmod -R 755 /${NODE_VERSION}/${NODE_APP_NAME}/{static,media,staticfiles} && \
    chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/{static,media,staticfiles} && \
    mkdir -p /var/log/uwsgi/ && \
    chown -R ${USER}:${USER} /var/log/uwsgi/

# Copiar archivos necesarios
COPY ./12012023.txt /12012023.txt
COPY ./scripts /scripts
COPY ./uwsgi_stage.ini /${NODE_VERSION}/${NODE_APP_NAME}/uwsgi_stage.ini
COPY ./baton.min.js /${NODE_VERSION}/${NODE_APP_NAME}/${NODE_APP_NAME}/baton.min.js
COPY ./qnode_ascii-art.txt /${NODE_VERSION}/${NODE_APP_NAME}/qnode_art.txt

# Copiar zona horaria
RUN cp /usr/share/zoneinfo/America/Guayaquil /etc/localtime && \
    echo 'export LC_ALL=es_ES.UTF-8' >> /etc/profile.d/locale.sh && \
    sed -i 's|LANG=C.UTF-8|LANG=es_ES.UTF-8|' /etc/profile.d/locale.sh && \
    echo "America/Guayaquil" > /etc/timezone

# Definir el punto de entrada
ENTRYPOINT ["/scripts/uwsgi.sh"]
CMD []
