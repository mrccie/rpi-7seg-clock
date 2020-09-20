#!/bin/bash

# This script executes system options for the clock
#  To avoid issues, only one system option will be
#  executed at a time and the rest will be cleared.
# ... because this is a home-made clock, not an iPod.

# Directory where the webpage puts files
webdir="/var/www/html/7seg_files"


####
#  System Configuration Options
####

# Option: Reboot Clock
if [ -f $webdir/reboot-server ]; then
    rm -f $webdir/reboot-server
    rm -f $webdir/shutdown-server
    rm -f $webdir/disable-web
    if [ -f $webdir/reboot-server ]; then
        echo "Cannot remove file reboot-server"
    else
        /sbin/shutdown -r now
    fi

# Option: Shut Down Clock
elif [ -f $webdir/shutdown-server ]; then
    rm -f $webdir/reboot-server
    rm -f $webdir/shutdown-server
    rm -f $webdir/disable-web
    if [ -f $webdir/shutdown-server ]; then
        echo "Cannot remove file shutdown-server"
    else
        /sbin/shutdown -h now
    fi

# Option: Disable Web Interface
elif [ -f $webdir/disable-web ]; then
    rm -f $webdir/reboot-server
    rm -f $webdir/shutdown-server
    rm -f $webdir/disable-web
    if [ -f $webdir/disable-web ]; then
        echo "Cannot remove file disable-web"
    else
        systemctl disable apache2
        systemctl stop apache2
    fi

fi



