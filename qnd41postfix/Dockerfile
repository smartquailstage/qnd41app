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

# Create postfix and vmail users and groups
RUN addgroup -g 1001 postfix && \
    adduser -D -u 1001 -G postfix -s /sbin/nologin postfix && \
    addgroup -g 1002 vmail && \
    adduser -D -u 1002 -G vmail -s /sbin/nologin vmail

# Copy configuration files
COPY postfix/main.cf /etc/postfix/main.cf
COPY postfix/master.cf /etc/postfix/master.cf

COPY postfix /etc/postfix

COPY mail.smartquail.io/certs/fullchain.pem /etc/ssl/certs/
COPY mail.smartquail.io/private/privkey.pem /etc/ssl/private/

# Create necessary directories and set permissions
RUN mkdir -p /var/spool/postfix/private \
    && chown postfix:postfix /var/spool/postfix/private \
    && chown vmail:vmail /var/spool/postfix \
    && chmod 750 /var/spool/postfix/private

# Expose the SMTP port
EXPOSE 25

# Define entrypoint script
COPY postfix/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

ENTRYPOINT ["/usr/local/bin/start.sh"]
