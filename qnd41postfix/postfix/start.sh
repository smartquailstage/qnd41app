#!/bin/bash

# Configuración de las credenciales de PostgreSQL
export PGPASSWORD="smartquaildev1719pass"  # Cambia esto por la contraseña real
export PGUSER="sqadmindb"  

function log {
  echo "$(date) $ME - $@"
}

function addUserInfo {
  # Add user 'info' if it doesn't exist
  if ! id -u info &>/dev/null; then
    log "Adding user 'info'"
    adduser -D -H info
  else
    log "User 'info' already exists"
  fi
}

# Exportar las variables de entorno para PostgreSQL
export POSTFIX_POSTGRES_DB=${POSTFIX_POSTGRES_DB}
export POSTFIX_POSTGRES_PASSWORD=${POSTFIX_POSTGRES_PASSWORD}
export POSTFIX_POSTGRES_USER=${POSTFIX_POSTGRES_USER}
export POSTFIX_POSTGRES_HOST=${POSTFIX_POSTGRES_HOST}

function createTable {
  local table_name=$1
  local table_sql=$2

  log "Creating ${table_name} table in PostgreSQL..."
  if psql -U "$POSTFIX_POSTGRES_USER" -d "$POSTFIX_POSTGRES_DB" -h "$POSTFIX_POSTGRES_HOST" -c "$table_sql"; then
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
  # Check hostname variable
  if [[ ! ${HOSTNAME} =~ \. ]]; then
    HOSTNAME=$HOSTNAME.$DOMAIN
  fi

  # Substitute configuration
  for VARIABLE in $(env | cut -f1 -d=); do
    VAR=${VARIABLE//:/_}
    sed -i "s={{ $VAR }}=${!VAR}=g" /etc/postfix/*.cf
  done

  # Override Postfix configuration
  if [ -f /overrides/postfix.cf ]; then
    while read -r line; do
      [[ -n "$line" && "$line" != [[:blank:]#]* ]] && postconf -e "$line"
    done < /overrides/postfix.cf
    echo "Loaded '/overrides/postfix.cf'"
  else
    echo "No extra postfix settings loaded because optional '/overrides/postfix.cf' not provided."
  fi

  # Include table-map files
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

function serviceStart {
  addUserInfo
  createVirtualTables
  serviceConf
  # Iniciar Postfix
  log "[ Iniciando Postfix... ]"
  /usr/sbin/postfix start-fg
}

export DOMAIN=${DOMAIN:-"localdomain"}
export HOSTNAME=${HOSTNAME:-"localhost"}
export MESSAGE_SIZE_LIMIT=${MESSAGE_SIZE_LIMIT:-"50000000"}
export RELAYNETS=${RELAYNETS:-""}
export RELAYHOST=${RELAYHOST:-""}

serviceStart &>> /proc/1/fd/1
