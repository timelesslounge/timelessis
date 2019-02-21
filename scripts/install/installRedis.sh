#!/bin/bash
sudo apt -y install make gcc libc6-dev tcl
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
sudo make install
ls /var/log/redis
if [ "$?" -gt "0" ]; then
    sudo mkdir /var/log/redis
fi
sudo chown redis /var/log/redis
sudo chgrp redis /var/log/redis
sudo chmod +w /var/log/redis
sudo src/redis-server > /var/log/redis/redis.log &