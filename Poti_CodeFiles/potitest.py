import machine
import utime
from led import LED

poti = machine.ADC(27) # initialisieren des Potentiometers
leds = [] # eine leere Liste

a = 5 # Hilfsvariable für den Schwellenwert
for le in range(11, 16): # Die Schleife zählt von 11 bis einschließlich 15
    led = LED(le, a) # led initialisieren am Pin (le) mit dem Schwellenwert (a)
    leds.append(led) # und in die Liste einfügen
    a += 10 # die Hilfsvariable um 10 erhöhen für die nächste led


while True: # Dauerschleife für das Programm

    # 16bit wert des AC durch 1000 teilen und von 65 abziehen
    # wert befindet sich nun zwischen 0 und 65
    wert = int(65 - (poti.read_u16() / 1000))

    # die Funktion 'observe' auf allen led's in der
    # Liste aufrufen und den eingelesenen Wert des
    # AC übergeben.
    for led in leds:
        led.observe(wert)

    utime.sleep(0.1) # kurz warten bevor der nächste Schleifendurchlauf startet

    
    
