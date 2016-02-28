#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# morse-code-twitter

# Standard Library Imports
import abc
import time
from threading import Timer

# Local Imports
import morse
import tweeting

# CONSTANTS
DOT = 125  # ms
DASH = 3 * DOT


def millis():
    """ Function which mimics Arduino millis() """
    return int(round(time.time() * 1000))


class MorseButton(metaclass=abc.ABCMeta):
    """ Class to keep track of state variables for a morse code button. """
    def __init__(self, tweet_timeout=5.0):
        """ Set up state variables. """
        self.tweet_timeout = tweet_timeout

        # Set up state variables
        self.time_var = 0
        self.curr_tweet = ""
        self.tweet_started = False

    @abc.abstractmethod
    def callback(self):
        """ Must be implemented by specific button class. """
        pass

    def handle_tweet(self):
        """ Function which handles out the current tweet. """
        print(self.curr_tweet)

        try:
            decoded = morse.decode_message(self.curr_tweet)
            tweeting.send_tweet(decoded)

        except morse.MorseCodeDecodeError as e:
            print(e.message, ': ',  e.invalid_str)

        except twitter.api.TwitterHTTPError as t:
            print(t.message)

        self.curr_tweet = ""
        self.tweet_started = False

    def handle_button_state_change(self, button_pressed):
        """ Callback to handle button rising and falling edges. Called by a
            specific button callback.
        """
        if button_pressed:  # Button was just pressed.
            duration = millis() - self.time_var

            # If the button was already pressed, record spaces, and restart the
            # tweet printing timer.
            if self.tweet_started:
                if DASH < duration <= 2.5 * DASH:
                    self.curr_tweet += ' '
                elif 2.5 * DASH < duration:
                    self.curr_tweet += ' / '

                self.tweet_printer.cancel()
                self.tweet_printer = Timer(self.tweet_timeout,
                                           self.handle_tweet)
                self.tweet_printer.start()

            # If the tweet was not started, start it, and start the timeout.
            else:
                self.tweet_started = True
                self.tweet_printer = Timer(self.tweet_timeout,
                                           self.handle_tweet)
                self.tweet_printer.start()

            self.time_var = millis()  # Keep track of press time.

        else:  # Button was just released.
            duration = millis() - self.time_var

            # Determine if the duration held was a dot or a dash.
            if duration <= 1.5 * DOT:
                self.curr_tweet += '.'
            else:
                self.curr_tweet += '-'

            self.time_var = millis()  # Keep track of release time.
