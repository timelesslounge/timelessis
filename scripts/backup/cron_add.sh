#!/bin/bash
#
# Create a backup script and set it into cron.
#

if [ "$1" == "" ]; then
    echo "Please provide a cron expression as script parameter in the format \"* * * * *\""
else
    echo  $1 " ./pg_backup.sh" > backup.sh
    chmod 755 backup.sh
    sudo mv backup.sh /etc/cron.d/
fi
