# Dockerfile for Postfix and Dovecot
FROM alpine:3.16

LABEL maintainer="your-email@example.com"

# Install Dovecot and Postfix
RUN apk update && apk add --no-cache \
    dovecot \
    dovecot-pgsql \
    dovecot-mysql \
    dovecot-ldap \
    dovecot-ssl \
    dovecot-managesieved \
    dovecot-lmtpd \
    dovecot-imapd \
    dovecot-pop3d \
    dovecot-sieve \
    postfix \
    bash \
    openssl \
    iproute2 \
    && mkdir -p /var/spool/postfix/private \
    && chown postfix:postfix /var/spool/postfix/private \
    && chmod 750 /var/spool/postfix/private

# Copy configuration files
COPY dovecot/dovecot.conf /etc/dovecot/dovecot.conf
COPY postfix/main.cf /etc/postfix/main.cf

# Create entrypoint script
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

ENTRYPOINT ["/usr/local/bin/start.sh"]

EXPOSE 25 110 143 587 993 4190
