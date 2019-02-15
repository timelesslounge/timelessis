#!/bin/sh

# Script for Redis availability check, installation and launch

which redis-cli
if [ "$?" -gt "0" ]; then
  echo "Redis Not installed, installing"
  sudo apt install make gcc libc6-dev tcl
  wget http://download.redis.io/redis-stable.tar.gz
  tar xvzf redis-stable.tar.gz
  cd redis-stable
  sudo make install
  cd ..
  sudo rm -rf redis-stable.tar.gz redis-stable/
  echo "Done installing Redis"
else
  echo "Redis already installed"
fi

echo "Redis PING"
redis-cli ping
if [ "$?" -gt "0" ]; then
  echo "Redis Not running, launching"
  redis-server > /dev/null &
  echo "Redis launched"
else
  echo "Redis already running"
fi
