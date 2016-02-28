#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# morse-code-twitter

# Pip Imports
import RPi.GPIO as GPIO

# Local Imports
from morse_button import *


class RPiMorseButton(MorseButton):
    """ A class which uses a Raspberry Pi as the input to a Morse Code button.
    """
    def __init__(self, pin, tweet_timeout=5.0):
        """ Store pin, set up IO. """
        super().__init__(tweet_timeout)

        self.pin = pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.BOTH,
                              callback=self.callback, bouncetime=15)

    def callback(self, __channel):
        """ Callback for button pressing and releasing. """
        button_pressed = not GPIO.input(self.pin)

        self.handle_button_state_change(button_pressed)
