# Diedre Brown; 24 April 2020 Code HW#2A - Receiver Code
# Final Project-Interact/Feedback:A Prototype

import radio
from microbit import *

# turn on radio and config channel
radio.on()
radio.config(channel=82, power=4)

# motion detected @ microbit alpha(the base)
# use radio to communicate from microbit alpha to microbit omega(the receiver)
# led lights on fabric sculpture go on at microbit omega if movement
# otherwise omega displays a '- - ..' and
# alpha led light turns on

msgtracko = 0
#  touchtrack =0

while True:
    sigmsg = radio.receive()
    if sigmsg == 'movement':
            # if there was movement at microbit alpha
            # turn light on at microbit omega
            pin0.write_digital(1)  # turn pin0 and LED on
            sleep(750)  # delay 750 milliseconds
            pin0.write_digital(0)  # turn pin0 and LED off
            msgtracko += 1  # increase msg counter
            sleep(100)

    # elif sigmsg == 'touch':
        # pin0.write_digital(1)
        # sleep(3000)
        # pin0.write_digital(0)
        # touchtrack += 1
        # sleep(100)

    else:
        # no motion detected, display morse code for Z
        display.show('-')
        sleep(300)
        display.clear()
        sleep(100)
        display.show('-')
        sleep(300)
        display.clear()
        sleep(100)
        display.show('.')
        sleep(300)
        display.clear()
        sleep(100)
        display.show('.')
        sleep(300)
        display.clear()
        sleep(1000)