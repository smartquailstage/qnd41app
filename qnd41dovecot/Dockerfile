FROM debian:11

LABEL org.opencontainers.image.authors="dovecot@dovecot.org"

ENV container=docker \
    LC_ALL=C
ARG DEBIAN_FRONTEND=noninteractive

# Copiar el archivo de clave pública y el archivo de lista de repositorios
COPY dovecot.gpg /etc/apt/trusted.gpg.d/
COPY dovecot.list /etc/apt/sources.list.d/

# Actualizar la lista de paquetes e instalar los necesarios
RUN apt-get update && apt-get install -y \
    tini \
    dovecot-core \
    dovecot-gssapi \
    dovecot-imapd \
    dovecot-ldap \
    dovecot-lmtpd \
    dovecot-lua \
    dovecot-managesieved \
    dovecot-mysql \
    dovecot-pgsql \
    dovecot-pop3d \
    dovecot-sieve \
    dovecot-solr \
    dovecot-sqlite \
    dovecot-submissiond \
    ca-certificates \
    ssl-cert && \
    rm -rf /var/lib/apt/lists/* && \  # Corregido: * para eliminar todo el cache
    groupadd -g 1000 vmail && \
    useradd -u 1000 -g 1000 vmail -d /srv/vmail && \
    passwd -l vmail && \
    rm -rf /etc/dovecot && \  # Asegúrate de que este directorio no sea necesario
    mkdir -p /srv/mail && \
    chown vmail:vmail /srv/mail && \
    mkdir -p /etc/dovecot && \  # Asegúrate de crear el directorio antes de usarlo
    make-ssl-cert generate-default-snakeoil && \
    ln -sf /etc/ssl/certs/ssl-cert-snakeoil.pem /etc/dovecot/cert.pem && \
    ln -sf /etc/ssl/private/ssl-cert-snakeoil.key /etc/dovecot/key.pem

# Copiar el archivo de configuración de Dovecot
COPY dovecot.conf /etc/dovecot/dovecot.conf

VOLUME ["/etc/dovecot", "/srv/mail"]

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/dovecot", "-F"]
