#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time


def millis():
    """ Function which mimics Arduino millis() """
    return int(round(time.time() * 1000))


MORSE_PIN = 18


def loop():
    """ Loop will run and is not expected to exit. """
    prev_button_pressed = False
    time_var = 0

    while True:
        curr_button_pressed = not GPIO.input(MORSE_PIN)

        if not curr_button_pressed:
            if prev_button_pressed:
                duration = millis() - time_var
                print(duration)
                if duration < 20:
                    continue

                prev_button_pressed = False
        else:
            prev_button_pressed = True


def main():
    """ Main entry point. """
    loop()


if __name__ == '__main__':
    main()
