# Dockerfile for Postfix
FROM alpine:3.16

LABEL maintainer="your-email@example.com"

# Install Postfix and necessary dependencies
RUN apk add --no-cache \
    postfix \
    postfix-pcre \
    postfix-pgsql \
    cyrus-sasl \
    cyrus-sasl-plain \
    cyrus-sasl-login \
    bash \
    curl \
    openssl \
    iproute2 \
    && mkdir -p /var/spool/postfix/private

# Copy configuration files
COPY postfix/main.cf /etc/postfix/main.cf
COPY postfix/master.cf /etc/postfix/master.cf

# Create necessary directories and set permissions
RUN mkdir -p /var/spool/postfix/private \
    && chown postfix:postfix /var/spool/postfix/private \
    && chmod 750 /var/spool/postfix/private

# Expose the SMTP port
EXPOSE 25

# Define entrypoint script
COPY postfix/postfix-service.sh /usr/local/bin/postfix-service.sh
RUN chmod +x /usr/local/bin/postfix-service.sh

ENTRYPOINT ["postfix/postfix-service.sh"]
