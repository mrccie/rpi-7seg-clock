#!/bin/bash

# This script is invoked every time the rpi_7seg service
#  is started.  It logs the date and time that the
#  service was started to allow administrators to track
#  how often failures occur.

# Directory where the logs are stored
logdir="/home/pi/rpi-clock/log"


####
#  Startup Logging
####

# Ensure record log exists
if [ ! -f $logdir/startup.log ]; then
        touch $logdir/startup.log
fi

# Tail the log into a temporary file
tail -n 19 $logdir/startup.log > $logdir/temp.log

# Echo the date/time to the temp log
echo "7seg service started at: " $(date) >> $logdir/temp.log

# Replace the record log with the temp log
rm $logdir/startup.log
mv $logdir/temp.log $logdir/startup.log

