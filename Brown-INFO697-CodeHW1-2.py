# Diedre Brown
# INFO 697-07 Rapid Prototyping and Physical Computing
# Code Homework #1 - Problem 2 Environmental Data Logger

from microbit import *

# Greet the user and let them know the Microbit needs to be calibrated
display.scroll("HELLO! CALIBRATE ME!")
compass.calibrate()  # calibrate the compass before taking readings

while True:
    sleep(10000)  # every 10s
    # microbit gets temperature readings:
    mbtemp = temperature()
    # microbit gets compass heading
    mbheading = compass.heading()
    # microbit displays temperature
    display.scroll(str(mbtemp) + 'C')
    # microbit displays compass heading
    display.scroll('HEADING:' + str(mbheading))