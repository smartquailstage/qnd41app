#!/bin/sh

# Iniciar Dovecot en segundo plano
echo "Starting Dovecot..."
dovecot &

# Esperar unos segundos para asegurar que Dovecot haya iniciado correctamente
sleep 10

# Define the user and group
USER="vmail"
GROUP="vmail"

# Define the main directory
MAIL_DIR="/var/mail"

# Create the directories if they don't exist
mkdir -p "$MAIL_DIR"

# Adjust ownership and permissions for the main mail directory
echo "Setting permissions and ownership for $MAIL_DIR"
chown $USER:$GROUP "$MAIL_DIR"
chmod 755 "$MAIL_DIR"

# Recursively adjust ownership and permissions for all subdirectories
echo "Setting permissions and ownership for all directories under $MAIL_DIR"
find "$MAIL_DIR" -type d -exec chown $USER:$GROUP {} \;
find "$MAIL_DIR" -type d -exec chmod 755 {} \;

# Set permissions for maildir subdirectories and files
echo "Setting permissions for files under $MAIL_DIR"
find "$MAIL_DIR" -type f -exec chmod 644 {} \;

# Check if /var/mail/info@mail.smartquail.io/tmp exists; create if needed
INFO_DIR="$MAIL_DIR/info@mail.smartquail.io/tmp"
mkdir -p "$INFO_DIR"

# Adjust ownership and permissions for the specific info directory
echo "Setting permissions and ownership for $INFO_DIR"
chown $USER:$GROUP "$INFO_DIR"
chmod 755 "$INFO_DIR"

# Verify the results
echo "Verification of permissions and ownership:"
ls -ld "$MAIL_DIR"
ls -ld "$MAIL_DIR/info@mail.smartquail.io"
ls -ld "$INFO_DIR"

echo "Permissions and ownership have been set."

# Keep the container running by tailing the log file
tail -f /var/log/dovecot.log
