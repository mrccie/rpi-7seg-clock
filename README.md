# rpi-7seg-clock

Author: mrccie<br>
Date: JAN-2024<br>
Version: 2.0 -- TESTING!<br>


## Purpose

rpi-7seg-clock is a package designed to drive a 7-segment clock (and some optional accessories) with a Raspberry Pi.

It is my hope that this will let you focus on what's important (cool looking cases) and offload what isn't (the mundane software).

For your convenience, this package includes web server on the Raspberry Pi that enables you to use a web browser to customize clock settings, diagnose issues, reboot/shut down the Pi, and even disable the web interface itself.

## Hardware and OS Requirements

This solution has been tested on the following hardware / software:
- Platform: Raspberry Pi 3B+, Raspberry Pi Zero WH (RPi 4, 5, and Zero 2 have not been tested but should work)
- Storage: 16GB SD card
- OS: Raspberry Pi OS 11 (bullseye)
- Clock Display: [Adafruit 1.2" 4-Digit 7-Segment Display w/ I2C Backpack](https://www.adafruit.com/product/1270) (available in multiple colors)
- (OPTIONAL) [Digital Light Sensor](https://www.amazon.com/gp/product/B00NLA4D4U/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1)
- (OPTIONAL) [High Precision Clock](https://www.adafruit.com/product/3013)

Note:
- Some soldering is required for the 7-segment display's backpack as well as the high precision clock
- Any digital light sensor (DLS) should work about the same way; there's nothing special about the one linked
- A DLS is recommended to enable automatic brightness control based on ambient light levels, though scheduled brightness changes are a supported alternative
- NTP is used to keep the system time accurate so a high precision clock is only necessary if you want extreme offline precision (aka "overengineering")


## Raspberry Pi Initialization

If you're setting up a Pi from scratch you'll need to do a few things to get it ready for use. This section will cover a few items:

- Initial Raspberry Pi OS Setup Requirements
- [optional][recommended] Update the Operating System
- [optional][recommended] Configure a Static IP (for the web interface)
- [optional] Miscellaneous Best Practices


#### Configure an RPi during Image Setup

[This article](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html) does a great job of covering multiple methods for initial Raspberry Pi setup. Items to make sure you set are:

- A username you will remember
- A strong password (don't let your clock host an attacker)
- Your timezone (because obviously)
- WiFi credentials (unless you plan to use a wired network connection)

** Because this is a clock you probably do not need a desktop (GUI) as part of the build, so I recommend a Lite version of the OS without one (though it will work with one as well).


#### Update the operating system

From an SSH session or a local keyboard, run the following commands.  You may need to hit "Y" or "Enter" at points to accept downloading updates.
```sh
sudo apt-get update
sudo apt-get upgrade
```


#### Set a Static IP

From an SSH session or a local keyboard, modify the file /etc/dhcpcd.conf
```sh
sudo nano /etc/dhcpd.conf
```

Example configuration file contents (for a wireless connection):
```sh
interface wlan0
static ip_address=192.168.1.50/24    
static routers=192.168.1.1
static domain_name_servers=208.67.220.220 8.8.8.8
```


#### Miscellaneous

Set your local timezone (in case you move or we finally stop falling forward/back):
```sh
sudo raspi-config
> 5 - Localization Options
>> L2 - Change Time Zone
>>> Pick accordingly
>>>> Finish
```


## Installation: Pre-Requisites and Git

#### Pre-requisites:
- Raspberry Pi has internet connectivity
- Terminal access to the Pi (local or via SSH)

#### Enable i2c Interface
```sh
sudo raspi-config
> 3 - Interfacing Options
>> P5 - I2C
>>> Would you like to enable... Yes
>>>> Finish
```
(You may receive an error like 'modprobe: FATAL: Module i2c-dev not found in directory /lib/modules/5.4.83+'; this can be ignored)

#### Install git
```sh
sudo apt-get install -y git
```

#### [optional] Configure git
<i>If you don't know why you would do this, you don't need to do this.</i>
```sh
git config --global user.email "<email>"
git config --global user.name "<username>"
```

#### Make a directory to clone this repository (code) to
```sh
cd ~
mkdir clock-git
cd clock-git
```


## Installation

From within the directory you created above (~/clock-git in the example), download the repository (code) via git.
```sh
git clone https://github.com/mrccie/rpi-7seg-clock
```

Go into the repository directory.
```sh
cd rpi-7seg-clock
```

Use the install script found within.
```sh
sudo ./install.sh
```

<b>You're Done!</b>


## What to Do Next?

If you want to customize your clock beyond the default behavior (ie. change brightness scheme, set to 24-hour mode, etc.), open a web browser and navigate to the IP address you set for your clock.  When using the web interface, please be aware that changes you make may take a minute or so to be picked up.

<i>In my testing this clock survives unexpected power disconnects very, very well (thanks, faulty USB cable!).  That said, it is a computer... when possible, please shut it down (via the web interface if you'd like) and wait a minute before unplugging it.  Startup takes a second but is automatic once power is restored.</i>
