#!/bin/sh

# Scripts to install Postgres and init timelessis databases
echo "Start Postgres server"
sudo echo "listen_addresses = '*'" >> /etc/postgresql/10/main/postgresql.conf
sudo /etc/init.d/postgresql start
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
