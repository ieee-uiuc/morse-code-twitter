#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time


# Constants
MORSE_PIN = 18
DOT = 100  # ms
DASH = 3 * DOT


def millis():
    """ Function which mimics Arduino millis() """
    return int(round(time.time() * 1000))


def setup():
    """ Setup function. Sets up the GPIO on the Pi. """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MORSE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    """ Loop will run and is not expected to exit. """
    prev_button_pressed = False
    time_var = 0
    curr_tweet = ""
    tweet_started = False

    while True:
        curr_button_pressed = not GPIO.input(MORSE_PIN)
        
        if curr_button_pressed:
            if not prev_button_pressed:  # Button was just pressed
                # How long was it up?
                duration = millis() - time_var

                if DASH < duration <= 1.5 * DASH:
                    curr_tweet += ' '
                elif 1.5 * DASH < duration < 3 * DASH:
                    curr_tweet += '  '
                
                # Keep Track of how long it will be pressed.
                time_var = millis()
                prev_button_pressed = True
                tweet_started = True

                # How long was it up?

        else:  # Button not pressed
            if prev_button_pressed:  # Button was just released
                duration = millis() - time_var
                time_var = millis()
                
                # Determine if the duration held was a dot or a dash.
                if duration <= 1.5 * DOT:
                    curr_tweet += '.'
                else:
                    curr_tweet += '-'

                prev_button_pressed = False
            else:  # Button has been up. How long?
                duration = millis() - time_var
                
                if duration >= 3 * DASH and tweet_started:
                    print(curr_tweet)
                    curr_tweet = ""
                    tweet_started = False

        
        # Debouncing Kludge
        time.sleep(0.01)


def main():
    """ Main entry point. """
    setup()
    loop()


if __name__ == '__main__':
    main()
