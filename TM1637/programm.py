import machine
import utime
from bodensensor import Bodensensor
import sys
sys.path.append("Digit_4")
from display import Display

sensor = Bodensensor(27)
display = Display(16, 17)

while True:
    feuchteWert = sensor.durchschnitt()
    display.zeigeZahl(feuchteWert)
    utime.sleep(0.1)