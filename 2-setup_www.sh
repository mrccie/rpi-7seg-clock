#!/bin/bash

# This script fetches and installs Apache and PHP
#

# Install apache
apt-get install apache2 -y

# Install php
apt-get install php libapache2-mod-php -y

# Backup index file
mv /var/www/html/index.html /var/www/html/index.html.bak

# Make directory for webconfig file
mkdir /var/www/html/7seg_files

# Copy New Webpage Files
cp /home/pi/rpi-clock/setup/www_files/index.html /var/www/html/index.html
cp /home/pi/rpi-clock/setup/www_files/config.php /var/www/html/config.php
cp /home/pi/rpi-clock/setup/www_files/sysopt.html /var/www/html/sysopt.html
cp /home/pi/rpi-clock/setup/www_files/sysopt.php /var/www/html/sysopt.php

# Copy webconfig file
cp /home/pi/rpi-clock/setup/www_files/webconfig.conf /var/www/html/7seg_files/webconfig.conf

# Change ownership of 7seg_files folder so Apache can write to it
chown www-data: /var/www/html/7seg_files
chown www-data: /var/www/html/7seg_files/webconfig.conf

