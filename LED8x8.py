import time
from shifter import Shifter
import multiprocessing

class led8x8():
  # pattern2 = [0b10001110,0b01101100,0b01101010,0b10001010,0b10001010,0b01101010,0b01101100,0b10001110] #DB pattern
  rows = [0b00000001, 0b00000010,0b00000100, 0b00001000,0b00010000, 0b00100000,0b01000000, 0b10000000]
  cols = [0b00000001, 0b00000010,0b00000100, 0b00001000,0b00010000, 0b00100000,0b01000000, 0b10000000]
  mask = 0b11111111
  def __init__(self,data,latch,clock):
    self.shifter = Shifter(data,latch,clock)
    pattern = multiprocessing.Array('i',8)
    p = multiprocessing.Process(target = self.smiley,args = (pattern,))
    p.daemon = True
    p.start()
  def display(self):
    for n in range(8):
      self.shifter.shiftByte(self.pattern[n])
      self.shifter.shiftByte(led8x8.rows[n])
      self.shifter.latch()
  def smiley(self,pattern):
    for n in range(8):
      pattern[n] = 0b10001110 
      
      

      


  
