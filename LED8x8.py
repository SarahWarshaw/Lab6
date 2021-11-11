import time
from shifter import Shifter

class led8x8():
  pattern = [0b11111111, 0b11111111,0b11111111, 0b00000000,0b00000000, 0b00000000,0b00000000, 0b00000000]
  rows = [0b11111110, 0b11111101,0b11111011, 0b11110111,0b11101111, 0b11011111,0b10111111, 0b01111111]
  def __init__(self,data,latch,clock):
    self.shifter = Shifter(data,latch,clock)
  def display(self):
    for n in range(8):
      self.shifter.shiftByte(led8x8.pattern[n])
      self.shifter.shiftByte(led8x8.rows[n])
      
      

      


  
