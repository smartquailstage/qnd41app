FROM debian:11-slim

LABEL org.opencontainers.image.authors="dovecot@dovecot.org"

ENV container=docker \
    LC_ALL=C
ARG DEBIAN_FRONTEND=noninteractive

# Añadir la clave GPG de Dovecot
ADD dovecot.gpg /etc/apt/keyrings/dovecot.gpg

# Añadir el archivo de lista de repositorios de Dovecot
ADD dovecot.list /etc/apt/sources.list.d/dovecot.list

# Copiar los certificados al directorio /etc/dovecot/
COPY mail.smartquail.io/certs/fullchain.pem /etc/dovecot/fullchain.pem
COPY mail.smartquail.io/private/privkey.pem /etc/dovecot/privkey.pem

# Cambiar los permisos de los certificados
RUN chmod 600 /etc/dovecot/fullchain.pem /etc/dovecot/privkey.pem

# Actualizar e instalar paquetes necesarios
RUN apt-get -y update && \
    apt-get -y install \
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
    postfix \
    postfix-ldap \
    postfix-pgsql && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -g 1000 vmail && \
    useradd -u 1000 -g 1000 vmail -d /srv/vmail && \
    passwd -l vmail && \
    groupadd -g 1001 postfix && \
    useradd -u 1001 -g 1001 postfix -d /var/spool/postfix && \
    passwd -l postfix && \
    rm -rf /etc/dovecot && \
    mkdir -p /srv/mail && \
    chown vmail:vmail /srv/mail && \
    mkdir -p /var/spool/postfix && \
    chown postfix:postfix /var/spool/postfix

# Añadir los archivos de configuración de Dovecot
ADD dovecot.conf /etc/dovecot/dovecot.conf
ADD dovecot-sql.conf.ext /etc/dovecot/dovecot-sql.conf.ext

# Añadir los archivos de configuración de Postfix
ADD postfix/main.cf /etc/postfix/main.cf
ADD postfix/master.cf /etc/postfix/master.cf

# Exponer los puertos necesarios
EXPOSE 24
EXPOSE 110
EXPOSE 143
EXPOSE 587
EXPOSE 990
EXPOSE 993
EXPOSE 4190

# Volumen para datos persistentes
VOLUME ["/etc/dovecot", "/srv/mail", "/var/spool/postfix"]

# Cambiar al usuario no privilegiado para ejecutar el contenedor
USER vmail

# Punto de entrada y comando predeterminado
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/dovecot", "-F"]
