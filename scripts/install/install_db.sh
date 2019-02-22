#!/bin/sh

# @todo #299:30min Continue the deploy algorithm. We need to create an
#  employee with role administator belonging to company "Timeless" and
#  credentials that will be taken by encrypted credential file.

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
