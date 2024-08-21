# Dockerfile for Postfix
FROM alpine:3.16

LABEL maintainer="your-email@example.com"

ENV container=docker \
    LC_ALL=C \
    TZ=America/Guayaquil

# Environment variables
ENV DOMAIN=mail.smartquail.io
ENV HOSTNAME=mail.smartquail.io

# Install Postfix and necessary dependencies
RUN apk update && apk add --no-cache \
    postfix \
    postfix-pcre \
    postfix-pgsql \
    cyrus-sasl \
    bash \
    curl \
    openssl \
    iproute2 \
    postfix-ldap \
    postgresql-client \
    pcre \
    db \
    gdbm

# Create postfix and vmail users and groups if they do not exist
RUN addgroup -g 1001 postfix || true \
    && adduser -D -u 1001 -G postfix -s /sbin/nologin postfix || true \
    && addgroup -g 1002 vmail || true \
    && adduser -D -u 1002 -G vmail -s /sbin/nologin vmail || true

# Create necessary directories and set permissions
RUN mkdir -p /var/spool/postfix/private /var/mail/ /home/info/Maildir/{cur,new,tmp} \
    && chown -R postfix:postfix /var/spool/postfix \
    && chmod 750 /var/spool/postfix/private \
    && chmod 750 /var/spool/postfix \
    && chown -R vmail:vmail /var/mail/ /home/info/Maildir \
    && chmod 700 /var/mail/ /home/info/Maildir \
    # Set permissions for Postfix directories
    && chown -R root:root /var/spool/postfix \
    && chmod 750 /var/spool/postfix \
    && chown -R postfix:postdrop /var/spool/postfix/public \
    && chmod 750 /var/spool/postfix/public \
    && chown -R postfix:postdrop /var/spool/postfix/maildrop \
    && chmod 750 /var/spool/postfix/maildrop \
    && chown root:root /var/spool/postfix/pid \
    && chmod 750 /var/spool/postfix/pid \
    # Add permissions for /home/info/Maildir
    && mkdir -p /home/info/Maildir/ \
    && chown -R vmail:vmail /home/info/Maildir \
    && chmod 700 /home/info/Maildir

# Set permissions for the SSL certificates
RUN mkdir -p /etc/ssl/certs /etc/ssl/private \
    && chmod 700 /etc/ssl/private \
    && chown root:root /etc/ssl/certs /etc/ssl/private

# Copy configuration files
COPY postfix/main.cf /etc/postfix/main.cf
COPY postfix/master.cf /etc/postfix/master.cf
COPY postfix /etc/postfix
COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/

# Set correct permissions for the SSL certificates
RUN chown root:root /etc/ssl/certs/fullchain.pem /etc/ssl/private/privkey.pem \
    && chmod 644 /etc/ssl/certs/fullchain.pem \
    && chmod 600 /etc/ssl/private/privkey.pem

# Expose the necessary ports for SMTP and secure connections
EXPOSE 25 465 587

# Define the volume
VOLUME ["/var/mail/"]

# Define entrypoint script
COPY postfix/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

ENTRYPOINT ["/usr/local/bin/start.sh"]
