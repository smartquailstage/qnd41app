# Dockerfile for Postfix
FROM alpine:3.16

LABEL maintainer="your-email@example.com"

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
    && mkdir -p /var/spool/postfix/private

# Create vmail user and group
RUN addgroup -g 1001 vmail && \
    adduser -D -u 1001 -G vmail -s /sbin/nologin vmail

# Copy configuration files
COPY postfix/main.cf /etc/postfix/main.cf
COPY postfix/master.cf /etc/postfix/master.cf

COPY postfix /etc/postfix

COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/

# Create necessary directories and set permissions
RUN mkdir -p /var/spool/postfix/private \
    && chown postfix:postfix /var/spool/postfix/private \
    && chown vmail:vmail /var/spool/postfix/private \
    && chmod 750 /var/spool/postfix/private

RUN mkdir -p /var/spool/postfix/private/transport \
    && chown postfix:postfix /var/spool/postfix/private/transport \
    && chown vmail:vmail /var/spool/postfix/private/transport \
    && chmod 750 /var/spool/postfix/private/transport \
    && chown root:root /etc/postfix/sql/*.cf \
    && chmod 644 /etc/postfix/sql/*.cf \
    && chown root:root /etc/postfix/sql/ \
    && chmod 755 /etc/postfix/sql/

# Expose the SMTP port
EXPOSE 25

# Define entrypoint script
COPY postfix/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

ENTRYPOINT ["/usr/local/bin/start.sh"]
