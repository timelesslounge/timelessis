#!/bin/sh

# Scripts to install Postgres and init timelessis databases
echo "Start Postgres server"
/etc/init.d/postgresql start
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