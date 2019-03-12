#!/bin/sh

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
if [! psql -lqt | cut -d \| -f 1 | grep -qw "timelessdb"; ]; then
    echo "Creating database: timelessdb"
    sudo -u postgres psql -c "CREATE DATABASE timelessdb;"
    echo "Timeless database created successfully"
fi

#checks if the user exists and create if not
if [! psql -t -c '\du' | cut -d \| -f 1 | grep -qw "timeless_user"; ]; then
    echo "Creating user: timeless_user"
    sudo -u postgres psql -c "CREATE USER timeless_user WITH
        SUPERUSER
        CREATEDB
        CREATEROLE
        INHERIT
        LOGIN
        ENCRYPTED PASSWORD 'timeless_pwd';"
    echo "Timeless user created successfully"
fi

company_id=$(sudo -u postgres -H -- psql -qtA -d timelessdb -c "INSERT INTO companies (name, code, address, created_on, updated_on) values ('Timeless', 'Tm', '', current_timestamp, current_timestamp) returning id")
role_id=$(sudo -u postgres -H -- psql -qtA -d timelessdb -c "INSERT INTO roles (name, works_on_shifts, company_id) values ('Administrator', False, $company_id) returning id")

credentials_src="/timelessis/credentials/credentials.json"

# read credentials from rultor
first_name=$(cat ${credentials_src} | jq '.credentials.account.admin.first_name')
last_name=$(cat ${credentials_src} | jq '.credentials.account.admin.last_name')
username=$(cat ${credentials_src} | jq '.credentials.account.admin.username')
email=$(cat ${credentials_src} | jq '.credentials.account.admin.email')
password=$(cat ${credentials_src} | jq '.credentials.account.admin.password')
pincode=$(cat ${credentials_src} | jq '.credentials.account.admin.pincode')


sudo -u postgres -H -- psql -d timelessdb -c "INSERT INTO employee
    (first_name, last_name, username, phone_number, birth_date,
    registration_date, account_status, user_status, email, password, pin_code,
    comment, company_id, role_id)
    values
    ('$first_name', '$last_name', '$username', '988888', '', '', 'active', 'active',
     '$email', '$password', '$pincode', 'Timeless user', $company_id, $role_id
    )
    "

