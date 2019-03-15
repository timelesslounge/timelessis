#!/bin/sh


# Scripts to install all the dependencies, like Python, DB, Redis, etc
srcdir="./scripts/install/deploy"

chmod +x $srcdir/install_python.sh
$srcdir/install_python.sh

chmod +x $srcdir/install_db.sh
$srcdir/install_db.sh

chmod +x $srcdir/install_redis.sh
$srcdir/install_redis.sh
