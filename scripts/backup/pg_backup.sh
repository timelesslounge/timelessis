#!/bin/bash

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
        *)
            echo " [ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Unknown Option \"$1\"" 1>&2
            exit 2
            ;;
    esac
done

if [ $# = 0 ]; then
    SCRIPTPATH=$(cd ${0%/*} && pwd -P)
    source $SCRIPTPATH/pg_backup.config
fi;

###########################
#### PRE-BACKUP CHECKS ####
###########################

# Make sure we're running as the required backup user
if [ "$BACKUP_USER" != "" -a "$(id -un)" != "$BACKUP_USER" ]; then
	echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] This script must be run as $BACKUP_USER. Exiting." 1>&2
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
#### START THE BACKUPS ####
###########################


FINAL_BACKUP_DIR=$BACKUP_DIR"`date +\%Y-\%m-\%d`/"

echo "Making backup directory in $FINAL_BACKUP_DIR"

if ! mkdir -p $FINAL_BACKUP_DIR; then
	echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Cannot create backup directory in $FINAL_BACKUP_DIR. Go and fix it!" 1>&2
	exit 1;
fi;

###########################
###### FULL BACKUP #######
###########################

echo -e "\n\nPerforming full backup"
echo -e "--------------------------------------------\n"

echo "Plain backup of $DATABASE"
if ! pg_dump -Fp -h "$HOSTNAME" -U "$USR" "$DATABASE" | gzip > $FINAL_BACKUP_DIR"$DATABASE".sql.gz.in_progress; then
	echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Failed to produce plain backup database $DATABASE" 1>&2
else
	mv $FINAL_BACKUP_DIR"$DATABASE".sql.gz.in_progress $FINAL_BACKUP_DIR"$DATABASE".sql.gz
fi

echo -e "\nAll database backups complete!"

#####################################
###### UPLOAD TO GOOGLE DRIVE #######
#####################################


echo -e "\n\n Uploading backup to Google Drive"
echo -e "--------------------------------------------\n"

if ! gdrive upload $FINAL_BACKUP_DIR"$DATABASE".sql.gz; then
    echo "[ERROR]["$(date +\%Y-\%m-\%d\ %H:%M:%S:%3N)"] Upload to Google Drive backup of $DATABASE failed!" 1>&2
else
    echo -e "\nUpload of database backups complete!"
fi
