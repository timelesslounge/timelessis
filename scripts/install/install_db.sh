#!/bin/sh

# Scripts to install Postgres and init timelessis databases
echo "Start Postgres server"
sudo -u postgres /etc/init.d/postgresql start
until sudo -u postgres psql -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
echo "Creating user: timeless_user"
sudo -u postgres psql -c "CREATE USER timeless_user WITH
    SUPERUSER
    CREATEDB
    CREATEROLE
    INHERIT
    LOGIN
    ENCRYPTED PASSWORD 'timeless_pwd';"
echo "Creating database: timelessdb_dev"
sudo -u postgres psql -c "CREATE DATABASE timelessdb_dev;"
echo "Creating database: timelessdb_test"
sudo -u postgres psql -c "CREATE DATABASE timelessdb_test;"
