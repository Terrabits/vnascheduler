#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install python2.7
sudo apt-get install python-pip
sudo apt-get install python-dev
sudo apt-get install git

cd ~
git clone https://github.com/Terrabits/vnascheduler.git
cd vnascheduler
sudo pip2 install -r requirements.txt
