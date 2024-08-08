#!/bin/bash

# Configuración de las credenciales de PostgreSQL
export PGPASSWORD="smartquaildev1719pass"
export PGUSER="sqadmindb"
export POSTFIX_POSTGRES_DB="POSFIXDB"
export POSTFIX_POSTGRES_USER="sqadmindb"
export POSTFIX_POSTGRES_HOST="smartquaildb"
export POSTFIX_POSTGRES_PASSWORD="smartquaildev1719pass"

function log {
  echo "$(date) $ME - $@"
}

function addUserInfo {
  if ! id -u info &>/dev/null; then
    log "Adding user 'info'"
    adduser -D -H info
  else
    log "User 'info' already exists"
  fi
}

function createTable {
  local table_name=$1
  local table_sql=$2

  log "Creating ${table_name} table in PostgreSQL..."
  POSTFIX_POSTGRES_PASSWORD=$POSTFIX_POSTGRES_PASSWORD psql -U "$POSTFIX_POSTGRES_USER" -d "$POSTFIX_POSTGRES_DB" -h "$POSTFIX_POSTGRES_HOST" -c "$table_sql"
  
  if [ $? -eq 0 ]; then
    log "${table_name} table created successfully."
  else
    log "Failed to create ${table_name} table."
  fi
}

function createVirtualTables {
  createTable "virtual_domains" "CREATE TABLE IF NOT EXISTS virtual_domains (id SERIAL PRIMARY KEY, domain VARCHAR(255) NOT NULL UNIQUE);"
  createTable "virtual_mailbox_domains" "CREATE TABLE IF NOT EXISTS virtual_mailbox_domains (id SERIAL PRIMARY KEY, domain VARCHAR(255) NOT NULL UNIQUE);"
  createTable "virtual_aliases" "CREATE TABLE IF NOT EXISTS virtual_aliases (id SERIAL PRIMARY KEY, source VARCHAR(255) NOT NULL, destination VARCHAR(255) NOT NULL);"
  createTable "virtual_mailboxes" "CREATE TABLE IF NOT EXISTS virtual_mailboxes (id SERIAL PRIMARY KEY, mailbox VARCHAR(255) NOT NULL UNIQUE);"
}

function serviceConf {
  if [[ ! $HOSTNAME =~ \. ]]; then
    HOSTNAME="$HOSTNAME.$DOMAIN"
  fi

  for VARIABLE in $(env | cut -f1 -d=); do
    VAR=${VARIABLE//:/_}
    VALUE=${!VAR}
    sed -i "s|{{ $VAR }}|$VALUE|g" /etc/postfix/*.cf
  done

  if [ -f /overrides/postfix.cf ]; then
    while read -r line; do
      [[ -n "$line" && "$line" != [[:blank:]#]* ]] && postconf -e "$line"
    done < /overrides/postfix.cf
    echo "Loaded '/overrides/postfix.cf'"
  else
    echo "No extra postfix settings loaded because optional '/overrides/postfix.cf' not provided."
  fi

  if ls -A /overrides/*.map 1> /dev/null 2>&1; then
    cp /overrides/*.map /etc/postfix/
    postmap /etc/postfix/*.map
    rm /etc/postfix/*.map
    chown root:root /etc/postfix/*.db
    chmod 0600 /etc/postfix/*.db
    echo "Loaded 'map files'"
  else
    echo "No extra map files loaded because optional '/overrides/*.map' not provided."
  fi
}

function setPermissions {
  # Ensure directories and files have correct permissions
  log "Setting permissions for Postfix directories and files..."

  # Set ownership and permissions for Postfix directories
  chown -R postfix:postfix /var/spool/postfix
  chmod 750 /var/spool/postfix/private
  chmod 750 /var/spool/postfix

  # Set ownership and permissions for Postfix configuration files
  chown -R root:root /etc/postfix
  chmod 640 /etc/postfix/*.cf

  # Set permissions for SSL certificates
  chown root:root /etc/ssl/certs/fullchain.pem /etc/ssl/private/privkey.pem
  chmod 644 /etc/ssl/certs/fullchain.pem
  chmod 600 /etc/ssl/private/privkey.pem
}

function serviceStart {
  addUserInfo
  createVirtualTables
  serviceConf
  setPermissions
  log "[ Iniciando Postfix... ]"
  /usr/sbin/postfix start-fg
}

export DOMAIN=${DOMAIN:-"localdomain"}
export HOSTNAME=${HOSTNAME:-"localhost"}
export MESSAGE_SIZE_LIMIT=${MESSAGE_SIZE_LIMIT:-"50000000"}
export RELAYNETS=${RELAYNETS:-""}
export RELAYHOST=${RELAYHOST:-""}

serviceStart &>> /proc/1/fd/1
