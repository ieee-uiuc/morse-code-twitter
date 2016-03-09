#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

lcd.begin(16, 1)

while 1:
    lcd.clear()
    lcd.message('It works!\n')
    lcd.message('#TAG_CPS Rocks')
    sleep(.5)
