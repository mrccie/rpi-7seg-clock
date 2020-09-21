#!/bin/bash

# This script sets up some basic stuff needed by other scripts
#

# Create folder structure
sudo -u pi mkdir /home/pi/rpi-clock
sudo -u pi mkdir /home/pi/rpi-clock/bash
sudo -u pi mkdir /home/pi/rpi-clock/python
sudo -u pi mkdir /home/pi/rpi-clock/setup
sudo -u pi mkdir /home/pi/rpi-clock/setup/www_files

# Copy files to appropriate places
sudo -u pi cp ./setup/rpi_7seg.service /home/pi/rpi-clock/setup/
sudo -u pi cp ./setup/bash/* /home/pi/rpi-clock/bash/
sudo -u pi cp ./setup/python/* /home/pi/rpi-clock/python/
sudo -u pi cp ./setup/www_files/* /home/pi/rpi-clock/setup/www_files/
