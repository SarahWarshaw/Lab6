import time
from shifter import Shifter
import multiprocessing
import random

class led8x8():
  pattern = multiprocessing.Array('i',8) #create array that can be sent to main code from separate process
  X = 0 #current lightningbug position in X
  Y = 0 #current lightningbug position in Y
  prevPattern = [0b11111110,0b11111111,0b11111111,0b11111111,0b11111111,0b11111111,0b11111111,0b11111111] #Use this so that the pattern that is read by the main function isnt in the middle of a transition between patterns
  rows = [0b00000001, 0b00000010,0b00000100, 0b00001000,0b00010000, 0b00100000,0b01000000, 0b10000000]
  mask = 0b11111111
  def __init__(self,data,latch,clock):
    self.shifter = Shifter(data,latch,clock) #create shifter object
    p = multiprocessing.Process(target = self.lightningBug,args = (self.pattern,)) #create process when led8x8 object is created 
    p.daemon = True
    p.start() #start process

  def display(self):
    # send two bytes and then ping the latch pin
    for n in range(8):
      self.shifter.shiftByte(self.pattern[n])
      self.shifter.shiftByte(led8x8.rows[n])
      self.shifter.latch()

  def smiley(self,pattern):
    pattern[0] = 0b00111100
    pattern[1] = 0b01000010
    pattern[2] = 0b10100101
    pattern[3] = 0b10000001
    pattern[4] = 0b10100101
    pattern[5] = 0b10011001
    pattern[6] = 0b01000010
    pattern[7] = 0b00111100
  
  def lightningBug(self,pattern):
    while True:
      stepX = random.randint(-1,1) #how many spaces to move in X(-1,0,1)
      stepY = random.randint(-1,1) #how many spaces to move in Y(-1,0,1)
      if ((self.X + stepX <0) or (self.X+stepX>7)):
          stepX = 0 #don't have it go out of bounds
          print('out')
      if ((self.Y + stepY <0) or (self.Y+stepY>7)):
          stepY = 0 #don't have it go out of bounds
          print('out')
      self.X = self.X + stepX #step in X
      print(self.X)
      self.Y = self.Y + stepY #step in Y
      print(self.Y)
      for n in range(8):
        self.prevPattern[n] = 0b00000000 #make all pattern 0
      self.prevPattern[self.Y] = 1<<(self.X) #In the row selected, set the pattern to have a 1 in the selected column
      for n in range(8):
        pattern[n] = (~self.prevPattern[n] & self.mask) #set pattern to inversion of previous pattern
      time.sleep(0.1) #update pattern every 0.1 sec
