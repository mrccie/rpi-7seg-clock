# rpi-7seg-clock


Author: mrccie

Copyright: 2020, mrccie

Date: 21-SEP-2020

Version: 1.0


## PURPOSE

rpi-7seg-clock is a package designed to drive a 7-segment clock (and, optionally, a digital light sensor) with a Raspberry Pi.  Hopefully this package will let you focus on what's important (cool looking cases) and offload what isn't (the mundane software).

This package will also enable a (very ugly and very basic) web server on the Raspberry Pi that enables you to customize clock settings and even reboot/shut down the Pi.


## System Requirements

This solution has been tested on the following hardware:
- Platform: Raspberry Pi 3B+, Raspberry Pi Zero
- OS: Rasbian 10 (buster)
- Clock Display: [Adafruit 1.2" 4-Digit 7-Segment Display w/ I2C Backpack](https://www.adafruit.com/product/1270) (available in multiple colors)
- [Digital Light Sensor](https://www.amazon.com/gp/product/B00NLA4D4U/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1) (optional)

Note:
- Some soldering is required for the 7-segment display and backpack
- Any digital light sensor should work; there's nothing special about the one linked


## Installation: Pre-Requisites and Git

This is just on Git for now.

Pre-requisites:
- Raspberry Pi has internet connectivity
- Terminal access to the Pi (local or via SSH)
- RECOMMENDED: Configure the Pi with a static IP for web reachability

Install git:
```sh
sudo apt-get install -y git
```

Configure git:
```sh
git config --global user.email "<email>"
git config --global user.name "<username>"
```

Make a directory to clone this repository to:
```sh
mkdir git
cd git
```


## Installation

```sh
sudo ./install.sh
```
