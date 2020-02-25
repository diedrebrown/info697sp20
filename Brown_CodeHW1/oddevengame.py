# Diedre Brown
# INFO 697-07 Rapid Prototyping and Physical Computing
# Code Homework #1-1 - Problem 1 Odd or Even Game

from microbit import *
import random

# define functions
# greeting and direction function
def greeting():
    while True:
        if accelerometer.was_gesture("face up"):
            display.show(Image.PACMAN)
            display.scroll("HELLO PLAYER!")
            sleep(250)
            display.scroll("FOR ODD# PRESS A.")
            display.show(Image.TRIANGLE)
            sleep(250)
            display.scroll("FOR EVEN# PRESS B.")
            display.show(Image.DIAMOND)
            sleep(1000)
            playgame()

# playgame function
# a random # between 0 and 100 is displayed.
# user has maxtime to press A if the number is ODD or B if the number is EVEN.
# whether answer right or wrong game begins again with a new number.
# if the user doesn't make a choice the greeting displays again.
def playgame():
    while True:
        delayCounter = 0
        maxtime = 0
        while delayCounter <= maxtime:
            num = random.randint(0, 100)
            display.scroll(num)
            sleep(1000)
            if num % 2 == 0 and button_b.was_pressed():
                display.show(Image.HAPPY)
            elif num % 2 != 0 and button_a.was_pressed():
                display.show(Image.HAPPY)
            else:
                display.show(Image.SAD)
            delayCounter += 1
            maxtime += 1
            sleep(750)

# actual program calls
while True:
    greeting()
    sleep(1000)
