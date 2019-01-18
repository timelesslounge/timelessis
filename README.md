# Timeless IS

Timeless IS is a web-based management software for a franchise of hookah bars called "Timeless Lounge"

## Current state

Timeless Lounge is currently using a set of software tools were developed around an external application called [Poster](https://joinposter.com/en) that is also providing APi to access data.
This application is not flexible enough, does not cover all the needs for process automation, therefore there is a need to develop full-fledged information system designed to combine the experience gained in automating processes in lounge bars and support the expansion of the franchise network.

## Non-functional requirements

### Technology stack

* Python 3.7.2 - programming language
* Flask - backend framework;
* React - backend framework;
* PostgreSQL - permanent storage;
* Redis - cache storage;

### Usability

The application should be able to work on any computer displays as well as mobile devices (smartphones and tablets). The interface of the application should be sophisticated, but simple, self-explanatory and intuitive

### Security

* Authentication by login/password
* Management of the users/roles (map users to roles, grant/revoke permissions, etc.)

### Fault tolerance

Very important for us in case of serious software/hardware failure. The system should not lose/corrupt data (regular database backups) and we should able to restore system performance within 15 minutes (master-slave replication and failover should be configured).

## Functional Requirements

### Admin Module

#### General Information

* The module is designed to manage spots, Users and their roles
* Only Users with Manager role and above should have access to this module
* Module sections should be represented as tabs (at the top of the screen)
* Ability to sort / filter data in all tables based on values ​​from any column
* The module consists of the following sections:
  * **Companies**: The list of all the companies managed by our software; (Visible only to Administrator role)
  * **Spots**: The list of all the bars belonging to a given company;
  * **Users**: The list of all the users belonging to a given company;
  * **Roles**: The list of all the roles configured and privileges;

#### Involved Entities

* Company
* Spots
* Floors
* Tables
* TableShapes
* Scheme
* SchemeCondition
* Users
* Roles
* Items

#### Privileges by Role

* Administrator
  * Add / Modify / Archive Spots
  * Create / modify / activate / deactivate accounts for all spots Users
  * View User profiles
* Owner
  * Create / modify / activate / deactivate accounts for all Users associated with owned spots
  * View self-profile
  * View User profiles associated with owned spots
* Director
  * Create / modify / activate / deactivate accounts for all managers, masters, interns associated with spots he involved in
  * View self-profile
  * View profiles of managers, masters, interns associated with spots he involved in
* Manager
  * Create / modify / activate / deactivate accounts for all masters and interns associated with spots he involved in
  * View self-profile
  * View profiles of masters and interns associated with spots he involved in
* Spot Admin
  * Only reservation table access
* Master / Intern
  * View self-profile
  * Modify account

### Reservation Module

#### General Information

* Reservation Management module should be deployed on separate subdomain
* UI should be designed for large screens
* Only Users with the Spot Admin role and above must have access to this module
* Users shouldn’t have an access to the reservation table outside of a spot
* Reservations table should have a support for a concurrent work, e.g. 2 Users can update the table from different devices
* Tables may accommodate more than 1 reservation (example: bar), if such setting is On
* One reservation can contain multiple tables
* Adding / Modifying / Deleting reservations only allowed for current and future shifts
* The system should prevent any possible reservation overlapping and violating of constraints (such as table’s min / max capacity)
* Time should be in a 24-hour format
* The module consists of the following sections:
  * **Timeline-based table**: shows all reservations in a particular spot for a selected day divided by tables (Y-Axis) and time intervals (X-Axis).
  * **Page to add/modify reservations**: page to create or modify reservations
  * **Table map**: Ideally, this element should be located together with the main timetable-view. It should be hideable from the main screen. The main idea of this element is to help freshers to navigate across the tables.
  * **Settings Page**: Page to set default duration of the reservation and notification settings

#### Involved Entities

* Reservation

![Reservation Life Cycle](https://drive.google.com/file/d/1TK7qZoj7DB68BI48PlLHac4LxkBTAc56/view)

* Customers
* Comments

#### Privileges by Role

* Spot Admin
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
