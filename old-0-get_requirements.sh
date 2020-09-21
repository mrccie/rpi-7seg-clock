#!/bin/bash

# This script installs necessary dependencies
#

# Install Dependencies
apt-get install -y python3
apt-get install -y python3-pip

# Adafruit HT16K33 library for display backpack
pip3 install adafruit-circuitpython-ht16k33

# Pillow Library
apt-get install python3-pil
