FROM debian:11-slim

# Copia los archivos necesarios
COPY dovecot.gpg /etc/apt/keyrings/dovecot.gpg
COPY dovecot.list /etc/apt/sources.list.d/dovecot.list
COPY mail.smartquail.io/certs/fullchain.pem /etc/dovecot/fullchain.pem
COPY mail.smartquail.io/private/privkey.pem /etc/dovecot/privkey.pem

# Ajusta los permisos de los archivos de certificados
RUN chmod 600 /etc/dovecot/fullchain.pem /etc/dovecot/privkey.pem

# Actualiza el sistema e instala los paquetes necesarios
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
        postfix \
        postfix-ldap \
        postfix-pgsql && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crea los grupos y usuarios necesarios
RUN groupadd -g 1000 vmail && \
    useradd -u 1000 -g 1000 vmail -d /srv/vmail && \
    passwd -l vmail 


# Configura los directorios y permisos
RUN rm -rf /etc/dovecot && \
    mkdir -p /srv/mail && \
    chown vmail:vmail /srv/mail 


# Define el punto de entrada para el contenedor
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["dovecot"]
