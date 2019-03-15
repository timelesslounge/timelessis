#!/bin/bash

credentials_src="./credentials.json"

company_id=$(sudo -u postgres -H -- psql -qtA -d timelessdb -c "INSERT INTO companies (name, code, address, created_on, updated_on) values ('Timeless', 'Tm', '', current_timestamp, current_timestamp) returning id")
role_id=$(sudo -u postgres -H -- psql -qtA -d timelessdb -c "INSERT INTO roles (name, works_on_shifts, company_id) values ('Administrator', False, $company_id) returning id")

# read credentials from rultor
first_name=$(cat ${credentials_src} | jq '.credentials.account.admin.first_name')
last_name=$(cat ${credentials_src} | jq '.credentials.account.admin.last_name')
username=$(cat ${credentials_src} | jq '.credentials.account.admin.username')
email=$(cat ${credentials_src} | jq '.credentials.account.admin.email')
password=$(cat ${credentials_src} | jq '.credentials.account.admin.password')
pincode=$(cat ${credentials_src} | jq '.credentials.account.admin.pincode')


sudo -u postgres -H -- psql -d timelessdb -c "INSERT INTO employees
    (first_name, last_name, username, phone_number, birth_date, registration_date,
    account_status, user_status, email, password, pin_code,
    comment, company_id, role_id, created_on, updated_on)
    values
    ('${first_name:1:-1}', '${last_name:1:-1}', '${username:1:-1}', '988888', '01/01/2019', '01/01/2019', 'active', 'active',
    '${email:1:-1}', '${password:1:-1}', '${pincode:1:-1}', 'Timeless user', $company_id, $role_id, '01/01/2019', '01/01/2019')"

