# Dockerfile for Dovecot
FROM alpine:3.16

LABEL maintainer="your-email@example.com"

# Install Dovecot and necessary dependencies
RUN apk add --no-cache \
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
COPY dovecot.conf /etc/dovecot/dovecot.conf
#COPY dovecot/ssl/ /etc/dovecot/ssl/

# Create necessary directories and set permissions
RUN mkdir -p /var/mail \
    && chown vmail:vmail /var/mail \
    && chmod 770 /var/mail \
    && mkdir -p /var/spool/dovecot \
    && chown dovecot:dovecot /var/spool/dovecot \
    && chmod 750 /var/spool/dovecot

# Expose necessary ports
EXPOSE 110 143 993 4190

# Define entrypoint script
COPY run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh

ENTRYPOINT ["/usr/local/bin/run.sh"]
