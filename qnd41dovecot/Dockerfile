FROM debian:11-slim

LABEL org.opencontainers.image.authors="dovecot@dovecot.org"

ENV container=docker \
    LC_ALL=C
ARG DEBIAN_FRONTEND=noninteractive

# Añadir claves y fuentes de APT
ADD dovecot.gpg /etc/apt/keyrings/dovecot.gpg
ADD dovecot.list /etc/apt/sources.list.d/

# Copiar archivos de configuración de Dovecot
COPY dovecot.conf /etc/dovecot/dovecot.conf
COPY postfix/main.cf /etc/postfix/main.cf

# Copiar certificados SSL
COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/fullchain.pem
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/privkey.pem

# Crear usuario y grupo postfix si no existen
RUN if ! id -u postfix > /dev/null 2>&1; then \
        addgroup --system postfix && \
        adduser --system --ingroup postfix --no-create-home --shell /sbin/nologin postfix; \
    fi

# Instalar paquetes necesarios y configurar el entorno
RUN apt-get -y update && apt-get -y install \
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
  rm -rf /var/lib/apt/lists && \
  groupadd -g 1000 vmail && \
  useradd -u 1000 -g 1000 vmail -d /srv/vmail && \
  passwd -l vmail && \
  mkdir -p /srv/mail && \
  chown vmail:vmail /srv/mail && \
  mkdir -p /etc/dovecot && \
  ln -s /etc/ssl/certs/fullchain.pem /etc/dovecot/cert.pem && \
  ln -s /etc/ssl/private/privkey.pem /etc/dovecot/key.pem

# Configuración de permisos y creación de directorios necesarios
RUN mkdir -p /var/spool/postfix/private && \
    chown vmail:vmail /var/spool/postfix/private

EXPOSE 24
EXPOSE 110
EXPOSE 143
EXPOSE 587
EXPOSE 990
EXPOSE 993
EXPOSE 4190

VOLUME ["/etc/dovecot", "/srv/mail"]
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/dovecot", "-F"]
