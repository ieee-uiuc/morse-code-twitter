#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

# Constants
MORSE_PIN = 12


def callback(channel):
    button_pressed = not GPIO.input(MORSE_PIN)
    if button_pressed:
        print("Button pressed!")
    else:
        print("Button released!")


def setup():
    """ Set up GPIO pins, callbacks. """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MORSE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(MORSE_PIN, GPIO.BOTH,
                          callback=callback, bouncetime=15)


def main():
    setup()
    while(True):
        try:
            pass  # Wait for something to happen.
        except KeyboardInterrupt:
            GPIO.cleanup()
            return


if __name__ == '__main__':
    main()
