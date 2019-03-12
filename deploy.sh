#!/bin/sh

# Scripts to deploy application to staging server

ENVIRONMENT='staging'

SERVER=$(jq -r ".credentials.server.$ENVIRONMENT.address" ../credentials.json)
USER=$(jq -r ".credentials.server.$ENVIRONMENT.username" ../credentials.json)
KEY=../staging.id_rsa
PG_USER=$(jq -r ".credentials.postgres.$ENVIRONMENT.username" ../credentials.json)
PG_PASS=$(jq -r ".credentials.postgres.$ENVIRONMENT.password" ../credentials.json)

echo "-- Copy application code to staging server"
scp -i $KEY -r . $USER@$SERVER:/app

# add scripts in cron (like the one created in #47)
# verify the webapplication is running
ssh -i $KEY $USER@$SERVER << EOF
  chmod +x app/scripts/install/deploy/install_dependencies.sh
  . app/scripts/install/deploy/install_dependencies.sh
  echo "-- Creating database user: $PG_USER"
  sudo -u postgres psql -c "CREATE USER $PG_USER WITH
    SUPERUSER
    CREATEDB
    CREATEROLE
    INHERIT
    LOGIN
    ENCRYPTED PASSWORD '$PG_PASS';"
  echo "-- Creating database: timelessdb_dev"  
  sudo -u postgres psql -c "CREATE DATABASE timelessdb_dev;"
  echo "-- Creating database: timelessdb_test"  
  sudo -u postgres psql -c "CREATE DATABASE timelessdb_test;"
  echo "-- REPLACE: add scripts to cron"
  cd /app
  python -m venv venv
  echo "-- Enabling virtual environment"
  . venv/bin/activate
  echo "-- Installing dependent libraries"
  pip install -r requirements.txt
  echo "-- Running database migrations"
  export TIMELESSIS_CONFIG="config.StagingConfig"
  export SQLALCHEMY_DATABASE_URI="postgresql://$PG_USER:$PG_PASS@localhost/timelessdb"
  python manage.py db upgrade
  echo "-- Running web application server"
  export FLASK_APP=main.py
  export FLASK_ENV=development
  flask run &
  echo "-- REPLACE: verify web application is running ok"
EOF
