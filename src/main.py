#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# morse-code-twitter

# Local Imports
from rpi_morse_button import *

# Constants
MORSE_PIN = 12


def main():
    button = RPiMorseButton(MORSE_PIN)
    while(True):
        try:
            pass  # Wait for something to happen.
        except KeyboardInterrupt:
            GPIO.cleanup()
            return


if __name__ == '__main__':
    main()
