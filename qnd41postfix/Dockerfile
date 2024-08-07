FROM alpine:3.16
LABEL MAINTAINER="Mauricio Silva <mausilva@smartquail.io.com>"

# Instalar curl, tar, make y otras dependencias necesarias para compilar Postfix y PostgreSQL
RUN apk add --no-cache bash build-base linux-pam-dev openssl-dev dovecot iptables pcre-dev postgresql-client postfix-pgsql postfix postfix-pcre cyrus-sasl-dev

# Copiar la configuración de Postfix
COPY conf /etc/postfix

# Copiar certificados SSL
COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/

# Crear el directorio y dar permisos adecuados
RUN mkdir -p /var/spool/postfix/private/transport \
    && chown postfix:postfix /var/spool/postfix/private/transport \
    && chmod 750 /var/spool/postfix/private/transport \
    && chown root:root /etc/postfix/sql/*.cf \
    && chmod 644 /etc/postfix/sql/*.cf \
    && chown root:root /etc/postfix/sql/ \
    && chmod 755 /etc/postfix/sql/

# Crear el usuario vmail
RUN adduser -D -u 1000 -G mail -s /sbin/nologin vmail

# Crear el directorio para el usuario vmail y ajustar permisos
RUN mkdir -p /var/mail \
    && chown vmail:mail /var/mail \
    && chmod 770 /var/mail \
    && mkdir -p /var/spool/postfix/private \
    && chown postfix:postfix /var/spool/postfix/private \
    && chown vmail:mail /var/spool/postfix/private \
    && chmod 750 /var/spool/postfix/private

# Volumen para el directorio spool de Postfix
VOLUME ["/var/spool/postfix"]

# Entrypoint para iniciar Postfix
ENTRYPOINT ["/etc/postfix/postfix-service.sh"]

# Exponer el puerto SMTP (25)
EXPOSE 25
