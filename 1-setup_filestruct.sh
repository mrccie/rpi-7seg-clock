#!/bin/bash

# This script sets up some basic stuff needed by other scripts
#

# Create folder structure
mkdir /home/pi/rpi-clock
mkdir /home/pi/rpi-clock/bash
mkdir /home/pi/rpi-clock/python
mkdir /home/pi/rpi-clock/setup
mkdir /home/pi/rpi-clock/setup/www_files

# Copy files to appropriate places
cp ./setup/bash/* /home/pi/rpi-clock/bash/
cp ./setup/python/* /home/pi/rpi-clock/python/
cp ./setup/* /home/pi/rpi-clock/setup/
cp ./setup/www_files/* /home/pi/rpi-clock/setup/www_files/
