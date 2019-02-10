#!/bin/bash
sudo apt install make gcc libc6-dev tcl
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
sudo make install
src/redis-server
