#!/bin/bash

# This script sets up the python service

### Python Service ###

# Create clock service
cp /home/pi/rpi-clock/setup/rpi_7seg.service /etc/systemd/system/

# Enable the service so it will start on reload
systemctl enable rpi_7seg.service

