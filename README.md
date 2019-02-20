# Timeless IS

Timeless IS is a web-based management software for a franchise of hookah bars called "Timeless Lounge"

## Current state

Timeless Lounge is currently using a set of software tools were developed around an external application called [Poster](https://joinposter.com/en) that is also providing APi to access data.
This application is not flexible enough, does not cover all the needs for process automation, therefore there is a need to develop full-fledged information system designed to combine the experience gained in automating processes in lounge bars and support the expansion of the franchise network.

## Non-functional requirements

### Technology stack

* [Python 3.6.7](https://www.python.org/downloads/) - programming language
* [Flask](http://flask.pocoo.org/) - backend framework;
* [React](https://reactjs.org/) - frontend framework;
* [PostgreSQL 10.6](https://www.postgresql.org/) - permanent storage;
* [Redis](https://redis.io/) - cache storage;

### Usability

The application should be able to work on any computer displays as well as mobile devices (smartphones and tablets). The interface of the application should be sophisticated, but simple, self-explanatory and intuitive.

A good example on how should be developed the frontend is the [GetSling webapp](https://app.getsling.com/).

### Security

* Authentication by login/password
* Management of the users/roles (map users to roles, grant/revoke permissions, etc.)

### Fault tolerance

Very important for us in case of serious software/hardware failure. The system should not lose/corrupt data (regular database backups) and we should able to restore system performance within 15 minutes (master-slave replication and failover should be configured).

## Functional Requirements

### Admin Module

#### General Information

* The module is designed to manage spots, Employees and their roles
* Only Employees with Manager role and above should have access to this module
* Module sections should be represented as tabs (at the top of the screen)
* Ability to sort / filter data in all tables based on values ​​from any column
* The module consists of the following sections:
  * **Companies**: The list of all the companies managed by our software; (Visible only to Administrator role)
  * **Locations**: The list of all the bars belonging to a given company;
  * **Employees**: The list of all the users belonging to a given company;
  * **Roles**: The list of all the roles configured and privileges;

#### Involved Entities

* Company
* Locations
* Floors
* Tables
* TableShapes
* Scheme
* SchemeCondition
* Employees
* Roles
* Items

#### Privileges by Role

* Administrator
  * Add / Modify / Archive Locations
  * Create / modify / activate / deactivate accounts for all spots Employees
  * View Employee profiles
* Owner
  * Create / modify / activate / deactivate accounts for all Employees associated with owned spots
  * View self-profile
  * View Employee profiles associated with owned spots
* Director
  * Create / modify / activate / deactivate accounts for all managers, masters, interns associated with spots he involved in
  * View self-profile
  * View profiles of managers, masters, interns associated with spots he involved in
* Manager
  * Create / modify / activate / deactivate accounts for all masters and interns associated with spots he involved in
  * View self-profile
  * View profiles of masters and interns associated with spots he involved in
* Location Admin
  * Only reservation table access
* Master / Intern
  * View self-profile
  * Modify account

### Reservation Module

#### General Information

* Reservation Management module should be deployed on separate subdomain;
* UI should be designed for large screens;
* Only Employees with the Location Admin role and above must have access to this module;
* Employees shouldn’t have an access to the reservation table outside of a spot;
* Reservations table should have a support for a concurrent work, e.g. 2 Employees can update the table from different devices;
* Tables may accommodate more than 1 reservation (example: bar), if such setting is On;
* One reservation can contain multiple tables;
* Adding / Modifying / Deleting reservations only allowed for current and future shifts;
* The system should prevent any possible reservation overlapping and violating of constraints (such as table’s min / max capacity);
* Time should be in a 24-hour format;
* The module consists of the following sections:
  * **Timeline-based table**: shows all reservations in a particular spot for a selected day divided by tables (Y-Axis) and time intervals (X-Axis);

![Timeline-based table](https://drive.google.com/uc?export=view&id=1rZcmESm-cWDycv0YFgce5gdlydjbIVL8)

  * **Page to add/modify reservations**: page to create or modify reservations;
  * **Table map**: Ideally, this element should be located together with the main timetable-view. It should be hideable from the main screen. The main idea of this element is to help freshers to navigate across the tables;

![Floorplan](https://drive.google.com/uc?export=view&id=1HfkDN4uS21bFud2J49jHPCyYLTWoJ2OL)

  * **Settings Page**: Page to set default duration of the reservation and notification settings;

#### Involved Entities

* Reservation

![Reservation Life Cycle](https://drive.google.com/uc?export=view&id=1Cr35yF9kXEyzAqScRmBZqs9b8vdQQBAN)

* Customers
* Comments

#### Privileges by Role

* Location Admin
  * Select a day from calendar
  * Select a floor from floor plan list
  * Create/Modify/Delete reservations
  * View a list of unconfirmed / late / not contacting reservations
  * Move reservations using drag & drop
  * Stretch reservations
  * Split reservations
  * Undo action
* Manager
  * All Masters permissions
  * Create/edit comment of the day
* Director
  * All Managers permissions
  * Settings
* Owner
  * View reservation table
  * Settings
* Administrator
  * Full access to all reservation tables

## Development Guidelines

* Always be as pythonic as possible;
* [PEP-8](https://www.python.org/dev/peps/pep-0008/) is your friend;
     * Strings are delimited by double quotes; use single quotes if you
     need to represent a quoted text inside a String.

* It's better to write clear code than good comments;
* The right test cycle is:
  1. Write a test;
  2. Run it and watch it fail;
  3. Write just enough code to make it pass;
  4. Go to 1;
* If you have questions on a task, ask it on the same issue or open a new one;
* Use PDD when you couldn't complete a task;
* Only submit stable and working PRs;
* PLEASE NOTE: when forking, remember to add rultor as collaborator in your private REPO, otherwise we won't be able to merge your contribution (and you won't get paid ;-) )

### Setup Development Environment

```
# Install RVM (for pdd)
curl -sSL https://get.rvm.io | bash -s stable --ruby
gem install pdd

# Download Python
wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tgz
tar xvzf Python-3.6.7.tgz
cd Python-3.6.7
./configure
make
make test
sudo make install

# Create workspace and virtual environment
mkdir timelessis-project
mkdir timelessis-project/venv
python3 -m venv timelessis-project/venv

# Clone the repository
cd timelessis-project
git clone https://github.com/<your-github-username>/timelessis.git
cd timelessis

# Activate virtual environment
. ../venv/bin/activate
```

### Dependency Install

```
pip install -r requirements.txt
```

### Setup PostgreSQL for Debian / Ubuntu
Debian / Ubuntu repositories include PostgreSQL by default. To install PostgreSQL, use the apt-get (or other apt-driving) command:
```
sudo apt-get update
sudo apt-get install postgresql-10
```
If packages are not found, do the following steps:
1. Create the file /etc/apt/sources.list.d/pgdg.list and add a line for the repository:
```
sudo deb http://apt.postgresql.org/pub/repos/apt/ {DEBIAN_OR_UBUNTU_VERSION}-pgdg main
```
NOTE: `DEBIAN_OR_UBUNTU_VERSION` is a code name, like `trusty` (ubuntu 14.01), `xenial` (16.04) and so on.

2. Import the repository signing key, and update the package lists
```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
and then repeat `apt-get update` and `apt-get install` commands.


### Database Setup
```
sudo -u postgres createuser --superuser timeless_user
sudo -u postgres createdb timelessdb_dev
sudo -u postgres createdb timelessdb_test
psql -U postgres -d timelessdb_dev
> alter user timeless_user with encrypted password 'timeless_pwd';
psql -U timeless_user -d timelessdb_dev
```

### Redis Installation
We use Redis for cache storage. For installing Redis:
```
sudo apt install make gcc libc6-dev tcl
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
sudo make install
src/redis-server
```

### Database backups
Backup scripts (`pg_backup.sh` and `pg_restore.sh`) are used for save storage of
database. Both of those scripts keep the configuration inside `pg_backup.config` file.
Password for those scripts can be provided using standard Postgres methods like
`PGPASSWORD` environment variable or `~/.pgpass` file.

Database backups are uploaded to Google Drive. Note that in order to do backup
(and restore), you have to install [GDrive](https://github.com/prasmussen/gdrive#downloads)
and configure [Service Account](https://github.com/prasmussen/gdrive#service-account)
credentials. Set `SERVICE_ACCOUNT_CREDENTIALS` in `pg_backup.config` to the
location of your service account credentials JSON file.

Note that the Google Drive API needs a file ID, not file name. After database
upload, you need to set the `FILE_ID` parameter in `pg_backup.config`, e.g.

```
FILE_ID=0B-Iak7O9SfIpYk9zTjZvY2xreVU
```

@todo #296:30min Automate the setting up of FILE_ID into pg_backup.config,
we already have the FILE_ID in the script, so what's left is to change it
in file

### Running tests

```
export FLASK_ENV=testing
pytest
```

NOTE: To skip integration tests run:
```
pytest -k 'not it'
```

### Generating migrations

```
python manage.py db migrate
python manage.py db upgrade
```

### Running the webserver in development

```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```


### Running the webserver locally using Docker
You should have `Docker` and `Docker Compose` installed. In other case go through official tutorial to install:
1. https://www.docker.com/get-started
2. https://docs.docker.com/compose/install/

To start up the docker exec the following commands:
```
docker-compose build
docker-compose up app
```
and check that `http://127.0.0.1:5000/` works.
To run tests execute:
```
docker-compose run app_test
```

### Credential files

The file credentials/credentials.json.asc is a JSON file containing all the
credentials for the external services used in Timeless IS. This file is
decrypted during deploy phase by rultor.

This is the sample file:

```
{
  "credentials": {
    "server": {
      "staging": {
        "address": "...",
        "username": "...",
        "password": "..."
      }
    },
    "postgres": {
      "staging": {
        "username": "..."
        "password": "..."
      }
    },
    "googledrive": {
      "staging": {
        "username": "...",
        "password": "..."
      }
    },
    "redsms": {
      "staging": {
        "username": "...",
        "password": "..."
      }
    },
    "poster": {
      "staging": {
        "domain": "...",
        "username": "...",
        "password": "...",
        "token": "..."
      }
    }
  }
}
```

Under staging.id_rsa and staging.id_rsa.pub are stored the keys to log into the
staging server without username and password

See [Rultor manual](http://doc.rultor.com/reference.html) on how to use it
decrypted files
