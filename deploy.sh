#!/bin/sh

# Scripts to deploy application to staging server
# @todo #45:30min Continue implementing deploy scripts. Find out user 
#  and domain of the staging server and replace scp and ssh with correct data.
#  Add scripts in cron (like the one created in #47). Verify the web 
#  application is running (execute couple fo curl requests).

echo "-- Run tests"
pytest

echo "-- Creating staging tag"
git tag -a staging-$tag -m "Rultor deploy staging-$tag"

echo "-- Copy application code to staging server"
scp -r . user@staging-server:/app

# add scripts in cron (like the one created in #47)
# verify the webapplication is running
ssh user@staging-server << EOF
  echo "-- Creating database user: timless_user"
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
  echo "-- TODO: add scripts in cron"
  cd /app
  echo "-- Running database migrations"
  python manage.py db upgrade
  echo "-- Running web application server"
  export FLASK_APP=main.py
  export FLASK_ENV=development
  flask run &
  echo "-- TODO: verify web application is running ok"
EOF



