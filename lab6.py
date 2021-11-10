import time 
from LED8x8 import led8x8

dataPin, latchPin, clockPin = 23,24,25

myLED8x8 = led8x8(dataPin, latchPin, clockPin)

while True:
  myLED8x8.display()

