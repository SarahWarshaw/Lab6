import time 
from LED8x8 import led8x8
import multiprocessing

dataPin, latchPin, clockPin = 23,24,25

myLED8x8 = led8x8(dataPin, latchPin, clockPin) #Create led8x8 object

try:
  while True:
    myLED8x8.display() #display whatever is saved in the array pattern
    time.sleep(0.001)
except Exception as e:
  print (e)
  myLED8x8.p.terminate()
  myLED8x8.p.join(2) #end process 

