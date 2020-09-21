#!/bin/bash

# This script sets up a cron job to run regularly to
#  enable the web portal functionality.

# Step 0: Add root to the cron.allow file
echo "> Troubleshooting: Step 0"
echo "root" >> /etc/cron.allow

# Step 1: Save all current cronjobs by root in a file
echo "> Troubleshooting: Step 1"
if [ -f /var/spool/cron/crontabs/root ]; then
	crontab -l > /home/pi/rpi-clock/bash/cron_list.txt
fi

# Step 2: Add the cron job to the list
echo "> Troubleshooting: Step 2"
echo "* * * * * /home/pi/rpi-clock/bash/webconfig_cron.sh" >> /home/pi/rpi-clock/bash/cron_list.txt

# Step 3: Reload edited list of cron jobs
echo "> Troubleshooting: Step 3"
crontab /home/pi/rpi-clock/bash/cron_list.txt

# Step 4: Clean Up
echo "> Troubleshooting: Step 4"
rm /home/pi/rpi-clock/bash/cron_list.txt
