#!/bin/sh

# @todo #299:30min Continue the deploy algorithm. We need to create an
#  employee with role administator belonging to company "Timeless" and
#  credentials that will be taken by encrypted credential file.

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

 service postgresql status
 if [ "$?" -gt "0" ]; then
   echo "Postgres is Not running, launching".
   service postgresql start
   echo "Postgres launched"
 else
   echo "Postgres already running"
 fi

sudo cp timeless_pg.service /lib/systemd/system/
sudo systemctl start timeless_pg.service

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

company = $(sudo -u postgres -H -- psql -d timelessdb -c "INSERT INTO company (name, code, address) values ('Timeless', 'Tm', '')")
role = $(sudo -u postgres -H -- psql -d timelessdb -c "INSERT INTO role (name, works_on_shifts, company_id) values ('Administrator', False, $company)")
password = "pass from rultor"
sudo -u postgres -H -- psql -d timelessdb -c "INSERT INTO employee
    (first_name, last_name, username, phone_number, birth_date,
    registration_date, account_status, user_status, email, password, pin_code,
    comment, company_id, role_id)
    values
    ('First', 'Last', 'timeless', '988888', '', '', 'active', 'active',
    'abc@xyz.com', $password, '10', 'Timeless user', $company, $role
    )
    "
