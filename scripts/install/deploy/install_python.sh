#!/bin/sh

# Script for installing Python

sudo add-apt-repository -y ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get -y install python3.6 python3.6-dev python3.6-venv python3-pip
echo "Done installing Python 3.6"
alias python=python3.6
