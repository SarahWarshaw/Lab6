import time 
from LED8x8 import led8x8
import multiprocessing
dataPin, latchPin, clockPin = 23,24,25

myLED8x8 = led8x8(dataPin, latchPin, clockPin)

try:
  while True:
  # pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,0b10100101, 0b10011001, 0b01000010, 0b00111100]
    myLED8x8.display()
    time.sleep(0.1)
except Exception as e:
  print (e)
  myLED8x8.p.terminate()
  myLED8x8.p.join(2)
