import sys
sys.path.append("Digit_4")
from tm1637 import TM1637
import utime
import machine


class Display:
    
    def __init__(self, clk, dio):
        self.display = TM1637(clk, dio)

    def zeigeZahl(self, zahl):
        self.display.number(zahl)
        
    def zeigeWort(self, wort):
        self.display.show(wort)
        
    def ausleeren(self):
        self.display.write([0,0,0,0])
        

