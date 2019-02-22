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
