import time
from shifter import Shifter
import multiprocessing
import random

class led8x8():
  pattern = multiprocessing.Array('i',8)
  X = 0
  Y = 0
  # pattern2 = [0b10001110,0b01101100,0b01101010,0b10001010,0b10001010,0b01101010,0b01101100,0b10001110] #DB pattern
  rows = [0b00000001, 0b00000010,0b00000100, 0b00001000,0b00010000, 0b00100000,0b01000000, 0b10000000]
  mask = 0b11111111
  def __init__(self,data,latch,clock):
    self.shifter = Shifter(data,latch,clock)
    p = multiprocessing.Process(target = self.lightningBug,args = (self.pattern,))
    p.daemon = True
    p.start()
  def display(self):
    for n in range(8):
      self.shifter.shiftByte(self.pattern[n])
      self.shifter.shiftByte(led8x8.rows[n])
      self.shifter.latch()
  def smiley(self,pattern):
    for n in range(8):
      pattern[n] = 0b10101010
  
  def lightningBug(self,pattern):
    while True:
      while True:
        step = random.randint(-1,1)
        direc = random.randint(0,1)
        if direc == 0:
          if (self.X + step <0 or self.X+step>7):
            print ("Out of board")
          else:
            break
        elif direc ==1:
          if (self.Y + step <0 or self.Y+step>7):
            print ("Out of board")
          else:
            break

      if direc == 0: # move in X
        self.X = self.X + step
        print(self.X)
      elif direc ==1: #move in Y
        self.Y = self.Y + step
        print(self.Y) 

      print(self.X,self.Y)
      for n in range(8):
        pattern[n] = 0b00000000
      pattern[self.Y] = 1<<(self.X)
      for n in range(8):
        pattern[n] = (~pattern[n] & self.mask)
      time.sleep(0.1)
