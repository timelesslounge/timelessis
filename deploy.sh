#!/bin/sh

# Scripts to deploy application to staging server
# @todo #45:30min Continue implementing deploy scripts. Find out user 
#  and domain of the staging server and replace scp and ssh with correct data.
#  Add scripts in cron (like the one created in #47). Verify the web 
#  application is running (execute couple fo curl requests).

# run tests
pytest

# create a tag
git tag -a $tag -m "Rultor deploy version $tag"

# copy code on remote server
scp -r . user@staging-server:/app

# create database (if not existing)
# run migrations
# set env variables and restart the server
# add scripts in cron (like the one created in #47)
# verify the webapplication is running
ssh user@staging-server << EOF
  sudo -u postgres psql -c "CREATE USER timeless_user WITH 
    SUPERUSER
    CREATEDB
    CREATEROLE
    INHERIT
    LOGIN
    ENCRYPTED PASSWORD 'timeless_pwd';"
  sudo -u postgres psql -c "CREATE DATABASE timelessdb_dev;"
  sudo -u postgres psql -c "CREATE DATABASE timelessdb_test;"
  cd /app
  python manage.py db upgrade
  export FLASK_APP=main.py
  export FLASK_ENV=development
  flask run
EOF



