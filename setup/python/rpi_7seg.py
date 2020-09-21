#!/usr/bin/python3

#-----------------------------------------------------------------------------#
# Name: rpi-clock-BigSeg7x4.py
#
# Tested Platform(s):
# - Raspberry Pi 3B
# - Adafruit 1.2" 4-Digit 7-Segment Display w/I2C Backpack (PID: 1260)
#
# Language: Python 3
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
#
#    01 - User Preferences
#
#-----------------------------------------------------------------------------#

# Hour Format
#   12 = 12 hour format (US/CAN)
#   24 = 24 hour format (everywhere else)
hour_format = 12

# Display Colon
#   True = Display the colon between hours and minutes
#   False = Do not display the colon between hours and minutes
colon_on = True

# Display Dimming Type
#   Valid values:
#   - 0: Display brightness not changed by software
#   - 1: Display brightness changed twice per day (one dim, one brighten)
#   - 2: Display brightness changed via digital light sensor output
dimmer_type = 2

# Display Dim Range
#   Dim leels are between 0.0 (lowest) and 1.0 (highest)
dim_low_level = 0.0
dim_high_level = 0.8

# Basic Dimmer (Type 1) Settings
#  Only needed if the dimmer type is set to "1" (basic dimmer)
#  Hours must use the 24-hour format (this is just BASIC dimming!)
#  Dim levels are between 0.0 (lowest) and 1.0 (highest)
basic_dim_low_hour = 20
basic_dim_low_minute = 30
basic_dim_high_hour = 8
basic_dim_high_minute = 30

# Digital Light Sensor (DLS)
#  dls_present - True if Present, False if Not
#  dls_board_pin - RPi GPIO pin number that the data output is connected to
#                  using BOARD numbers, not GPIO numbers
dls_present = True
dls_board_pin = 18



#-----------------------------------------------------------------------------#
#
#    02 - Import Requirements (hopes, dreams, pylons...)
#
#-----------------------------------------------------------------------------#

# adafruit stuff
from adafruit_ht16k33.segments import BigSeg7x4

# raspberry pi gpio
import board
from gpiozero import DigitalInputDevice

# python stuff
import datetime
import time
import os



#-----------------------------------------------------------------------------#
#
#    03 - Global Variables
#
#-----------------------------------------------------------------------------#

hour = 0
minute = 0
second = 0
disp_hour = 0
disp_minute = 0
disp_second = 0
is_am = True
is_noon = False
brightness = 0.8
webconfig_file = "/var/www/html/7seg_files/webconfig.conf"
use_webconfig = True



#-----------------------------------------------------------------------------#
#
#    04 - OS & Hardware Prep
#
#-----------------------------------------------------------------------------#

# 7-Segment Board Definition
i2c = board.I2C()
display = BigSeg7x4(i2c)

# Set the display brightness to the default value
display.brightness = brightness

# Set up digital light sensor, if applicable
if( dls_present ):
    dls = DigitalInputDevice("BOARD" + str(dls_board_pin))



#-----------------------------------------------------------------------------#
#
#    05 - Startup Functions
#
#-----------------------------------------------------------------------------#

# Function: post()
#   Power On Self Test
#   Tests all segments of the display to test for hardware issues
def post():

    # Start Blank
    display.fill(0)
    time.sleep(0.75)

    # Test Colons & Dots
    post_colon_test = 4
    while( post_colon_test >= 0 ):
        if( post_colon_test % 2 == 0 ):
            display.colon = True
            display.top_left_dot = True
            display.bottom_left_dot = True
            display.ampm = True
        else:
            display.colon = False
            display.top_left_dot = False
            display.bottom_left_dot = False
            display.ampm = False

        time.sleep(0.75)
        post_colon_test -= 1

    # Test Segments
    post_num = 9999
    while( post_num > 0 ):
        display.print(post_num)
        time.sleep(0.75)
        post_num -= 1111

    display.print("0000")
    time.sleep(0.75)

    # Test Display Fading
    display.fill(0)
    display.set_digit_raw(2, 0b01110110)
    display.set_digit_raw(3, 0b00000110)
    post_fade = 1.0
    while( post_fade >= 0.0 ):
        display.brightness = post_fade
        time.sleep(0.3)
        post_fade -= 0.1

    # End Blank
    display.fill(0)
    time.sleep(0.75)

    return



# Function: set_defaults()
#   Sets the clock to default behavior
def set_defaults():

    #-- Get Intial Time --#
    init_datetime = datetime.datetime.now()
    init_hour = init_datetime.hour
    init_minute = init_datetime.minute
    init_second = init_datetime.second
    

    #-- Display Brightness --#

    global brightness

    # Auto-dimmer: Type 0 (OFF)
    if( dimmer_type == 0 ):
        brightness = 0.8

    # Auto-dimmer: Type 1 (Basic)
    elif( dimmer_type == 1 ):
        if( basic_dim_low_hour < basic_dim_high_hour ):
            if( (init_hour >= basic_dim_low_hour) and \
                (init_hour < basic_dim_high_hour) ):
                brightness = dim_low_level
            else:
                brightness = dim_high_level
        else:
            if( (init_hour >= basic_dim_high_hour) and \
                (init_hour < basic_dim_low_hour) ):
                brightness = dim_high_level
            else:
                brightness = dim_low_level

    # Auto-dimmer: Type 2 (DLS)
    elif( dimmer_type == 2 ):
        bright = not dls.is_active
        if( bright ):
            brightness = dim_high_level
        else:
            brightness = dim_low_level

    # Configure display
    display.brightness = brightness

    return




#-----------------------------------------------------------------------------#
#
#    06 - Normal Operation Functions
#
#-----------------------------------------------------------------------------#

# Function: get_datetime()
#   Gets the current date and time, as reported by the OS
def get_datetime():

    # Global Variables
    global hour
    global minute
    global second
    global disp_hour
    global disp_minute
    global disp_second
    global is_am
    global is_noon

    # Get current date and time
    curr_datetime = datetime.datetime.now()

    # Get the hour, minute and second
    hour = curr_datetime.hour
    minute = curr_datetime.minute
    second = curr_datetime.second

    # Set the hour, minute and second for display
    #  Because Americans can't use 24-hour clocks
    disp_hour = hour
    disp_minute = minute
    disp_second = second
    
    # Identify AM vs PM
    if( hour >= 12 ):
        is_am = True
    else:
        is_am = False

    # Is it noon?
    if( (hour==12) and (minute==0) ):
        is_noon = True
    else:
        is_noon = False

    # Adjust hour reading if necessary
    if((hour_format == 12) and (hour > 12)):
        disp_hour -= 12
    
    return



# Function: display_time()
#   Displays the current time (hh:mm)
def display_time():

    # Noon Special!
    if( is_noon  ):
        draw_noon()
        return

    # Hour - Digit 1
    dig0 = int(disp_hour / 10)
    if( dig0 > 0 ):
        display[0] = str(dig0)
    else:
        display[0] = ' '

    # Hour - Digit 2
    dig1 = disp_hour % 10
    display[1] = str(dig1)
    
    # Minute - Digit 3
    dig2 = int(disp_minute / 10)
    display[2] = str(dig2)
    
    # Minute - Digit 4
    dig3 = disp_minute % 10
    display[3] = str(dig3)

    # Colon
    if( colon_on ):
        display.colon = True
    else:
        display.colon = False

    # AM/PM dots
    if( (is_am) and (hour_format == 12) ):
        display.top_left_dot = True
    else:
        display.top_left_dot = False

    return



# Function: draw_noon()
#   Draws 'noon' on the clock
#   Really just an easter egg
def draw_noon():

    display.set_digit_raw(0, 0b00110111)    #n
    display.set_digit_raw(1, 0b00111111)    #0
    display.set_digit_raw(2, 0b00111111)    #0
    display.set_digit_raw(3, 0b00110111)    #n

    # Technically, AM means "pre-midday" and PM means "post-midday"
    #  ... so noon (being midday) is neither.  But hey, we've got to
    #  pick one of them.
    # This defect could be improved with an RGB that changes to a color
    #  that is not defined as the AM or PM color, and also by the
    #  removal of all this commentary about the AM/PM dot in an easter
    #  egg that will only display for one minute a day.
    display.top_left_dot = True

    return



# Function: set_dim_level()
#  Selects the more appropriate dimmer function
def set_dim_level():

    # Type 0 = No Auto-Dimmer
    if( dimmer_type == 0 ):
        return

    # Type 1 = Basic Dimmer
    elif( dimmer_type == 1 ):
        basic_dimmer()
        return

    # Type 2 = DLS Dimmer
    elif( dimmer_type == 2 ):
        dls_dimmer()
        return

    return



# Function: basic_dimmer()
#   Dims and brightens the clock face once per day
#    (one dim + one brighten).
#   Only for use if there is no hardware light sensor or
#    software-based option available.
def basic_dimmer():

    # Global variables
    global brightness

    # Set dim to low at appropriate time
    if( (hour == basic_dim_low_hour) and (minute == basic_dim_low_minute) ):
        brightness = dim_low_level
        display.brightness = brightness

    # Set dim to high at appropriate time
    elif( (hour == basic_dim_high_hour) and (minute == basic_dim_high_minute) ):
        brightness = dim_high_level
        display.brightness = brightness

    return



# Function: dls_dimmer()
#   Dims and brightens the clock face based on readings from a
#    Digital Light Sensor (DLS)
#   The DLS returns:
#    True if it is Dark
#    False if it detects Light
def dls_dimmer():

    # Global variables
    global brightness

    # We average a few readings on changes, just to be sure
    dls_average_needed = False
    average = 0

    # is_active is True when the sensor reads Dark
    bright = not dls.is_active

    # Identify whether a brightness change has occurred
    if( bright ):
        if( brightness == dim_high_level ):
            return
        else:
            dls_average_needed = True
    else:
        if( brightness == dim_low_level ):
            return
        else:
            dls_average_needed = True

    # Get an average score and act accordingly if brightness changed
    if( dls_average_needed ):

        # Average over 0-9 (10 numbers)
        for x in range(0, 10):
            if( not dls.is_active ):
                average += 1

        # If average is high, set brightness to high
        if( average > 4 ):
            brightness = dim_high_level
        else:
            brightness = dim_low_level

        # Set display brightness
        display.brightness = brightness

        # Reset need for an average
        dls_average_needed = False


    return



# Function: sleep()
#   Sleeps this script for as long as possible while attempting to
#    maintain accuracy to within 1 second and ensuring the display
#    is not brightening/dimming too often.
def sleep():

    # Sleep until needed (approximately)
    #   The delay may need to be adjusted generously if
    #   API calls for (eg.) weather are added
    if( second < 45 ):
        time.sleep(15)
    else:
        sleep_time = 60 - second - 0.5
        time.sleep(sleep_time)

    return



# Function: get_webconfig()
#   Checks for changes made via the web portal and applies them
def get_webconfig():

    # Globals
    global hour_format
    global colon_on
    global dimmer_type
    global dim_high_level
    global dim_low_level
    global use_webconfig

    # Abort if there is no config file
    if( not os.path.exists(webconfig_file) ):
        return

    # Read in web config file to a dictionary
    conf_dict = {}
    with open(webconfig_file) as file:
        for line in file:
            (key, val) = line.rstrip().split('=')
            conf_dict[key] = val

    # Close the web config file
    file.close()

    # Abort if web config not used
    use_webconfig = conf_dict["WEB_CONFIG"]
    if( use_webconfig != "True" ):
        return


    ### Copy in the values

    # Hour Format
    hour_format = int(conf_dict["HOUR_FORMAT"])

    # Show Colon
    if( conf_dict["COLON_ON"] == "False" ):
        colon_on = False
    else:
        colon_on = True

    # Dimmer Type
    dimmer_type = int(conf_dict["DIMMER_TYPE"])

    # Dimmer Level
    dim_high_level = float(conf_dict["DIMMER_MAX"])
    dim_low_level = float(conf_dict["DIMMER_MIN"])

    # Use Webconfig
    if( conf_dict["WEB_CONFIG"] == "False" ):
        use_webconfig = False
    else:
        use_webconfig = True

    return



#-----------------------------------------------------------------------------#
#
#    95 - Main Function
#
#-----------------------------------------------------------------------------#

# Function: main()
#   Executes the normal program flow
def main():

    # Startup
    post()
    set_defaults()

    # Main execution loop
    while( True ):
        get_webconfig()
        get_datetime()
        display_time()
        set_dim_level()
        sleep()

    return



#-----------------------------------------------------------------------------#
#
#    99 - Execution
#
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    main()



