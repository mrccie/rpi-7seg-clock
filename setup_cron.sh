#!/bin/bash

# This script sets up a cron job to run regularly to
#  enable the web portal functionality.

# Step 1: Save all current cronjobs by root in a file
crontab -l > /home/pi/rpi_7seg/bash/cron_list.txt

# Step 2: Add the cron job to the list
echo "* * * * * /home/pi/rpi_7seg/bash/webconfig_cron.sh" >> /home/pi/rpi_7seg/bash/cron_list.txt

# Step 3: Reload edited list of cron jobs
crontab cron_list.txt

# Step 4: Clean Up
rm /home/pi/rpi_7seg/bash/cron_list.txt

