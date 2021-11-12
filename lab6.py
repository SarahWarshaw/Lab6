import time 
from LED8x8 import led8x8
import multiprocessing
import random

dataPin, latchPin, clockPin = 23,24,25

myLED8x8 = led8x8(dataPin, latchPin, clockPin)

def newPattern(myPattern):
  move = random.randint(0,1)
  
  pattern = [0b10001110,0b01101100,0b01101010,0b10001010,0b10001010,0b01101010,0b01101100,0b10001110]
  pattern[0] = move
  for n in range(8):
    myPattern[n] = pattern[n]

while True:
  myPattern = multiprocessing.Array('i',8)
  myPattern = newPattern(myPattern)
  p = multiprocessing.Process(target = led8x8.display,args = myPattern,)
  p.daemon = True
  p.start
  # pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,0b10100101, 0b10011001, 0b01000010, 0b00111100]
  myPattern = newPattern(myPattern)
  time.sleep(0.0001)
  p.join()

