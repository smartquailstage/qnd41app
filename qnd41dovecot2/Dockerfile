# Dockerfile for Dovecot
FROM alpine:3.16

LABEL maintainer="your-email@example.com"

# Install Dovecot and necessary dependencies
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
    bash \
    openssl

# Copy configuration files
COPY dovecot/dovecot.conf /etc/dovecot/dovecot.conf

# Create necessary directories and set permissions
RUN mkdir -p /var/spool/postfix/private \
    && chown dovecot:dovecot /var/spool/postfix/private \
    && chmod 750 /var/spool/postfix/private

# Expose the necessary ports
EXPOSE 110 143 587 993 4190

# Define entrypoint script
COPY dovecot/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

ENTRYPOINT ["/usr/local/bin/start.sh"]
