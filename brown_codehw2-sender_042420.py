# Diedre Brown; 24 April 2020 Code HW#2A - Sender Code
# Final Project-Interact/Feedback: A Prototype

import radio
from microbit import *

# turn on radio and config channel
radio.on()
radio.config(channel=82, power=4)

# counters to keep track of messages sent
msgtrack = 0
# touchtrack = 0

# define zmorse function
# when there is no movement the base station will flash light
# the slow morse code for z
def zmorse():
    baseled = 0
    while True:
        display.show(Image.UMBRELLA)
        pin1.write_digital(1)  # turn pin1 and LED on
        sleep(300)  # delay 300 milliseconds
        pin1.write_digital(0)  # turn pin1 and LED off
        display.clear()
        sleep(300)  # delay 300 milliseconds
        display.show(Image.UMBRELLA)
        pin1.write_digital(1)  # turn pin1 and LED on
        sleep(300)  # delay 300 milliseconds
        pin1.write_digital(0)  # turn pin1 and LED off
        display.clear()
        sleep(300)  # delay 300 milliseconds
        display.show(Image.DIAMOND)
        pin1.write_digital(1)  # turn pin1 and LED on
        sleep(100)  # delay 100 milliseconds
        pin1.write_digital(0)  # turn pin1 and LED off
        display.clear()
        sleep(100)  # delay 100 milliseconds
        display.show(Image.DIAMOND)
        pin1.write_digital(1)  # turn pin1 and LED on
        sleep(100)  # delay 100 milliseconds
        pin1.write_digital(0)  # turn pin1 and LED off
        display.clear()
        baseled += 1  # /;increase base light counter
        sleep(100)

# pgm calls
# motion detected @ microbit the base station
# the microbit base station radio sends msg to the microbit receiver
while True:
    val = pin0.read_analog()
    print((val,))
    if val > 700:
        # motion detected @ microbit alpha
        # send message to microbit omega
        radio.send('movement')
        msgtrack += 1  # increase msg counter
        sleep(2000)

    # i'm thinking of adding something that senses touch at the
    # base station as an else if. it just feels like the type of thing that
    # people might like to touch, and that could generate a different light
    # pattern at the receiver station.
    # elif pin14.read_digital(1):
        # radio.send('touch')
        # touchtrack +=1 # increase msg coutner
        # sleep(2000)

    else:
        # no motion detected
        # digital white led displays SLOW morse
        # code for z by turning on and off
        zmorse()
    sleep(2000)