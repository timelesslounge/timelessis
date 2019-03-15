#!/bin/bash

CURRENT_DIR=`pwd`

which psql
if [ "$?" -gt "0" ]; then
  echo "Postgres Not installed, installing"
  sudo apt-get -y install wget ca-certificates
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
  sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
  sudo apt-get update
  sudo apt-get -y install postgresql postgresql-contrib
  echo "Done installing Postgres"
else
  echo "Postgres already installed"
fi

echo "Restarting Postgres"
service postgresql restart

sudo cp $CURRENT_DIR/scripts/install/deploy/timeless_pg.service /lib/systemd/system/
sudo systemctl start timeless_pg.service

which jq
if [ "$?" -gt "0" ]; then
  echo "Installing jq to parse credentials"
  sudo apt-get -y install jq
  echo "Done installing jq"
else
  echo "jq already installed"
fi

#checks if the database exists and create if not
if sudo -u postgres -H -- psql -lqt | cut -d \| -f 1 | grep -qw "timelessdb"; then
    echo "Database already exists: nothing to do!"
else
    echo "Creating database: timelessdb"
    sudo -u postgres psql -c "CREATE DATABASE timelessdb;"
    echo "Timeless database created successfully"
fi

credentials_src=./credentials.json
PG_USER=$(cat ${credentials_src} | jq '.credentials.postgres.staging.username')
PG_PWD=$(cat ${credentials_src} | jq '.credentials.postgres.staging.password')

#checks if the user exists and create if not
if sudo -u postgres -H -- psql -t -c '\du' | cut -d \| -f 1 | grep -qw "$PG_USER"; then
    echo "User already exists: nothing to do!"
else
    echo "Creating user: $PG_USER"
    sudo -u postgres -H -- psql -t -c "CREATE USER ${PG_USER:1:-1} WITH SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN ENCRYPTED PASSWORD '${PG_PWD:1:-1}';"
    echo "Timeless user created successfully"
fi
