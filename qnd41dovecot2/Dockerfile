FROM debian:11-slim

LABEL org.opencontainers.image.authors="dovecot@dovecot.org"

ENV container=docker \
    LC_ALL=C

# Argumento para evitar preguntas durante la instalación
ARG DEBIAN_FRONTEND=noninteractive

# Añadir claves y fuentes de Dovecot
COPY dovecot.gpg /etc/apt/trusted.gpg.d/
COPY dovecot.list /etc/apt/sources.list.d/

# Instalar paquetes necesarios
RUN apt-get update && \
    apt-get install -y \
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
    ssl-cert \
    postfix && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -g 1000 vmail && \
    useradd -u 1000 -g 1000 -d /srv/vmail vmail && \
    passwd -l vmail && \
    mkdir -p /srv/mail && \
    chown vmail:vmail /srv/mail && \
    make-ssl-cert generate-default-snakeoil && \
    mkdir -p /etc/dovecot && \
    ln -sf /etc/ssl/certs/ssl-cert-snakeoil.pem /etc/dovecot/cert.pem && \
    ln -sf /etc/ssl/private/ssl-cert-snakeoil.key /etc/dovecot/key.pem && \
    mkdir -p /var/spool/postfix/private && \
    chown postfix:postfix /var/spool/postfix/private

# Copiar configuración de Dovecot y Postfix
COPY dovecot.conf /etc/dovecot/dovecot.conf
COPY postfix/main.cf /etc/postfix/main.cf

# Exponer los puertos necesarios para los servicios
EXPOSE 25 110 143 587 465 993 4190

# Montar volúmenes
VOLUME ["/etc/dovecot", "/srv/mail"]

# Configurar el punto de entrada y el comando
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/dovecot", "-F"]
