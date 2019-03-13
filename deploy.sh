#!/bin/sh

# Scripts to deploy application to staging server

ENVIRONMENT='staging'

SERVER=$(jq -r ".credentials.server.$ENVIRONMENT.address" ../credentials.json)
USER=$(jq -r ".credentials.server.$ENVIRONMENT.username" ../credentials.json)
PASSWORD=$(jq -r ".credentials.server.$ENVIRONMENT.password" ../credentials.json)
PG_USER=$(jq -r ".credentials.postgres.$ENVIRONMENT.username" ../credentials.json)
PG_PASS=$(jq -r ".credentials.postgres.$ENVIRONMENT.password" ../credentials.json)


FIRST_NAME=$(jq -r ".credentials.account.admin.first_name" ../credentials.json)
LAST_NAME=$(jq -r ".credentials.account.admin.last_name" ../credentials.json)
USERNAME=$(jq -r ".credentials.account.admin.username" ../credentials.json)
EMAIL=$(jq -r ".credentials.account.admin.email" ../credentials.json)
PASSWORD=$(jq -r ".credentials.account.admin.password" ../credentials.json)
PINCODE=$(jq -r ".credentials.account.admin.pincode" ../credentials.json)

echo "-- Remove our own venv dir"
rm -rf ./venv

cp ../credentials.json .

echo "-- Remove existing dir"
sshpass -p $PASSWORD ssh -o StrictHostKeyChecking=no $USER@$SERVER -tt << EOF
  rm -rf /app
  logout
EOF

echo "-- Copy application code to staging server"
sshpass -p $PASSWORD scp -o StrictHostKeyChecking=no -r `pwd` $USER@$SERVER:/app

# add scripts in cron (like the one created in #47)
# verify the webapplication is running
echo "-- Execute install script"
sshpass -p $PASSWORD ssh -o StrictHostKeyChecking=no $USER@$SERVER -tt << EOF
  cd /app
  chmod +x /app/scripts/install/deploy/install_dependencies.sh
  /app/scripts/install/deploy/install_dependencies.sh
  cd /app
  echo "-- REPLACE: add scripts to cron"
  python3.6 -m venv venv
  echo "-- Enabling virtual environment"
  . venv/bin/activate
  echo "-- Installing dependent libraries"
  pip3 install -r requirements.txt
  echo "-- Running database migrations"
  export TIMELESSIS_CONFIG="config.StagingConfig"
  export SQLALCHEMY_DATABASE_URI="postgresql://$PG_USER:$PG_PASS@localhost/timelessdb"
  python3.6 manage.py db upgrade
  company_id=$(sudo -u postgres -H -- psql -qtA -d timelessdb -c "INSERT INTO companies (name, code, address, created_on, updated_on) values ('Timeless', 'Tm', '', current_timestamp, current_timestamp) returning id")
  role_id=$(sudo -u postgres -H -- psql -qtA -d timelessdb -c "INSERT INTO roles (name, works_on_shifts, company_id) values ('Administrator', False, $company_id) returning id")
  sudo -u postgres -H -- psql -d timelessdb -c "INSERT INTO employee
    (first_name, last_name, username, phone_number, birth_date,
    registration_date, account_status, user_status, email, password, pin_code,
    comment, company_id, role_id)
    values
    ('$FIRST_NAME', '$LAST_NAME', '$USERNAME', '988888', '', '', 'active', 'active',
     '$EMAIL', '$PASSWORD', '$PINCODE', 'Timeless user', $company_id, $role_id
    )
  "
  echo "-- Running web application server"
  export FLASK_APP=main.py
  export FLASK_ENV=development
  export FLASK_RUN_PORT=80
  export FLASK_RUN_HOST=$SERVER
  nohup flask run > /var/log/timeless.log 2>&1 &
  rm -rf /app/credentials.json
  echo "-- REPLACE: verify web application is running ok"
  logout
EOF

exit 0
