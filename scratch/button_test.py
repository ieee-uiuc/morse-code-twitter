#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    button_pressed = not GPIO.input(18)
    if button_pressed:
        print('Button Pressed')
        time.sleep(0.2)
