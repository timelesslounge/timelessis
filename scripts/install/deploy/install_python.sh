#!/bin/sh

# Script for installing Python

python -c 'import sys; assert sys.version_info >= (3, 6), "Unsupported version {}".format(sys.version_info[:2])'
if [ "$?" -gt "0" ]; then
  echo "Python 3.6 is Not installed, installing".
  sudo add-apt-repository -y ppa:jonathonf/python-3.6
  sudo apt-get update
  sudo apt-get -y install python3.6 python3.6-dev python3.6-venv
  echo "Done installing Python 3.6"
  alias python=python3
else
  echo "Python installed"
fi
