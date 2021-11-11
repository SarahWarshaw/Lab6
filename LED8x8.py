import time
from shifter import Shifter

class led8x8():
  pattern = [0b11111111, 0b11111111,0b11111111, 0b11111111,0b11111111, 0b11111111,0b11111111, 0b11111111]
  rows = [0b00000001, 0b00000010,0b00000100, 0b00001000,0b00010000, 0b00100000,0b01000000, 0b10000000]
  def __init__(self,data,latch,clock):
    self.shifter = Shifter(data,latch,clock)
  def display(self):
    for n in range(8):
      self.shifter.shiftByte(led8x8.rows[n])
      self.shifter.shiftByte(led8x8.pattern[n])
      

      


  
