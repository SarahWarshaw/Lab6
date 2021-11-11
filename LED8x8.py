import time
from shifter import Shifter

class led8x8():
  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,0b10100101, 0b10011001, 0b01000010, 0b00111100]
  pattern2 = [0b11011110,0b11011100,0b11011010,0b11011010,0b11011010,0b11011010,0b11011100,0b11011110]
  rows = [0b00000001, 0b00000010,0b00000100, 0b00001000,0b00010000, 0b00100000,0b01000000, 0b10000000]
  cols = [0b00000001, 0b00000010,0b00000100, 0b00001000,0b00010000, 0b00100000,0b01000000, 0b10000000]
  mask = 0b11111111
  for n in range(8):
    pattern[n] = (~pattern[n] & mask)
  def __init__(self,data,latch,clock):
    self.shifter = Shifter(data,latch,clock)
  def display(self):
    for n in range(8):
      self.shifter.shiftByte(led8x8.pattern2[n])
      self.shifter.shiftByte(led8x8.rows[n])
      self.shifter.latch()
      
      

      


  
