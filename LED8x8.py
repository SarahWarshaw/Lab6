import time
from shifter import Shifter

class led8x8():
  pattern = [0b01010101, 0b01010101, 0b01010101, 0b01010101,
  0b01010101, 0b01010101, 0b01010101, 0b01010101]
  def __init__(self,data,latch,clock):
    self.shifter = Shifter(data,latch,clock)
  def display(self):
    for n in range(8):
      self.shifter.shiftByte(led8x8.pattern[n])
      self.shifter.shiftByte(1<<(4))

      


  
