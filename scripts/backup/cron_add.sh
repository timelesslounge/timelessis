#!/bin/bash
#
# Create a backup script and set it into cron.
#
echo '* * * * * ./pg_backup.sh' > backup.sh
chmod 755 backup.sh
sudo mv backup.sh /etc/cron.d/