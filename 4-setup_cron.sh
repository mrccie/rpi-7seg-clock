#!/bin/bash

# This script sets up a cron job to run regularly to
#  enable the web portal functionality.

# Step 0: Add root to the cron.allow file
echo "root" >> /etc/cron.allow

# Step 1: Save all current cronjobs by root in a file
crontab -l > /home/pi/rpi-clock/bash/cron_list.txt

# Step 2: Add the cron job to the list
echo "* * * * * /home/pi/rpi-clock/bash/webconfig_cron.sh" >> /home/pi/rpi-clock/bash/cron_list.txt

# Step 3: Reload edited list of cron jobs
crontab /home/pi/rpi-clock/bash/cron_list.txt

# Step 4: Clean Up
rm /home/pi/rpi-clock/bash/cron_list.txt
