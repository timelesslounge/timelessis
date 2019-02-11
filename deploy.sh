#!/bin/sh

# Scripts to deploy application to staging server
# @todo #126:30min Finish implementing deploy scripts. Add scripts in cron 
#  (like the one created in #47). Verify the web application is running - 
#  execute couple of curl requests.

echo "-- Run tests"
pytest

echo "-- Creating staging tag"
git tag -a staging-$tag -m "Rultor deploy staging-$tag"

STAGING_SERVER=$(jq -r '.credentials.server.staging.address' ../credentials.json)
STAGING_USER=$(jq -r '.credentials.server.staging.username' ../credentials.json)
STAGING_KEY=../staging.id_rsa

echo "-- Copy application code to staging server"
scp -i $STAGING_KEY -r . $STAGING_USER@$STAGING_SERVER:/app

# add scripts in cron (like the one created in #47)
# verify the webapplication is running
ssh -i $STAGING_KEY $STAGING_USER@$STAGING_SERVER << EOF
  echo "-- Creating database user: timeless_user"
  sudo -u postgres psql -c "CREATE USER timeless_user WITH 
    SUPERUSER
    CREATEDB
    CREATEROLE
    INHERIT
    LOGIN
    ENCRYPTED PASSWORD 'timeless_pwd';"
  echo "-- Creating database: timelessdb_dev"  
  sudo -u postgres psql -c "CREATE DATABASE timelessdb_dev;"
  echo "-- Creating database: timelessdb_test"  
  sudo -u postgres psql -c "CREATE DATABASE timelessdb_test;"
  echo "-- REPLACE: add scripts to cron"
  cd /app
  echo "-- Running database migrations"
  python manage.py db upgrade
  echo "-- Running web application server"
  export FLASK_APP=main.py
  export FLASK_ENV=development
  flask run &
  echo "-- REPLACE: verify web application is running ok"
EOF



