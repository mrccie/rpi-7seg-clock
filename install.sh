#!/bin/bash


#### Installing necessary system dependencies ####

# Python
apt-get install -y python3
apt-get install -y python3-pip
apt-get install -y python3-pil

# Apache 2
apt-get install -y apache2

# PHP
apt-get install -y php libapache2-mod-php



#### Installing Python dependencies ####

# Adafruit HT16K33 library for display backpack
pip3 install adafruit-circuitpython-ht16k33



#### Create directory structure ####

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



#### Get WWW Stuff Set Up ####

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




#### Set Up Cron Job for WWW Service ####

echo "> Setting up cron for WWW interface..."

# Step 0: Add root to the cron.allow file
echo "root" >> /etc/cron.allow

# Step 1: Save all current cronjobs by root in a file
if [ -f /var/spool/cron/crontabs/root ]; then
        crontab -l > /home/pi/rpi-clock/bash/cron_list.txt
fi

# Step 2: Add the cron job to the list
echo "* * * * * /home/pi/rpi-clock/bash/webconfig_cron.sh" >> /home/pi/rpi-clock/bash/cron_list.txt

# Step 3: Reload edited list of cron jobs
crontab /home/pi/rpi-clock/bash/cron_list.txt

# Step 4: Clean Up
rm /home/pi/rpi-clock/bash/cron_list.txt

echo "done."



#### Set up Python Service ####

echo "> Creating clock service..."

# Create clock service
cp /home/pi/rpi-clock/setup/rpi_7seg.service /etc/systemd/system/

# Enable the service so it will start on reload
systemctl enable rpi_7seg.service

# Start the service
systemctl start rpi_7seg.service

echo "done."
echo ""
echo ""
echo "Your clock should now be functional. Enjoy!"
