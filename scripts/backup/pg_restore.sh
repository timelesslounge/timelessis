#!/bin/bash
# @todo #115:30min Implement retrieval of database backup from Google account.
#  It should be from the same Google account and location as in pg_backup.sh.

###########################
####### LOAD CONFIG #######
###########################
while [ $# -gt 0 ]; do
    case $1 in
        -c)
            if [ -r "$2" ]; then
                source "$2"
                shift 2
            else
                echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Unreadable config file \"$2\"" 1>&2
                exit 1
            fi
            ;;
        -d)
            if [ -d "$2" ]; then
                RESTORE_DIR="$2"
                shift 2
            else
                echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Unreadable directory \"$2\"" 1>&2
                exit 1
            fi
            ;;
        *)
            echo " [ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Unknown Option \"$1\"" 1>&2
            exit 2
            ;;
    esac
done
echo "FFF $RESTORE_DIR"

if [ $# = 0 ]; then
    SCRIPTPATH=$(cd ${0%/*} && pwd -P)
    source $SCRIPTPATH/pg_backup.config
fi;

###########################
#### PRE-RESTORE CHECKS ####
###########################

# Make sure we're running as the required backup user
if [ "$BACKUP_USER" != "" -a "$(id -un)" != "$BACKUP_USER" ]; then
	echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] This script must be run as $BACKUP_USER. Exiting." 1>&2
	exit 1;
fi;

if [ -z $RESTORE_DIR ]; then
	echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Backup not provided, please use -d option." 1>&2
	exit 1;
fi

if [ $(find $RESTORE_DIR -type f | wc -l) -ne 1 ]; then
	echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Backup directory contains more than one file." 1>&2
	exit 1;
fi;


###########################
### INITIALISE DEFAULTS ###
###########################

if [ ! $HOSTNAME ]; then
	HOSTNAME="localhost"
fi;

if [ ! $USR ]; then
	USR="postgres"
fi;


###########################
###### FULL BACKUP #######
###########################

RESTORE_FILE=$(find $RESTORE_DIR -type f)

echo -e "\n\nPerforming restore from $RESTORE_FILE"
echo -e "--------------------------------------------\n"

echo "Restore $DATABASE"
if ! zcat $RESTORE_FILE | psql -h "$HOSTNAME" -U "$USR" "$DATABASE"; then
	echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Failed to restore backup from $RESTORE_FILE to database $DATABASE" 1>&2
fi

echo -e "\nDatabase restore complete!"

