import machine
import utime

# Die Klass LED nimmt eine Pin-Nummer, an der sie angeschlossen ist,
# und einen Schwellenwert entgegen, ab dem sie leuchten soll
class LED:
    def __init__(self, pin, onValue):
        self.led = machine.Pin(pin, machine.Pin.OUT) # die led initialisieren
        self.threshold = onValue                     # der Schwellenwert

    # einfache Funktion zum Anschalten der led
    def on(self):
        self.led.value(1)

    # einfache Funktion zum Ausschalten der led
    def off(self):
        self.led.value(0)

    # die Funktion nimmt einen Vergleichswert entgegen
    # und vergleicht ihn mit dem Schwellenwert
    def observe(self, value):
        if value > self.threshold: # ist der Vergleichswert größer als der Schwellenwert?
            self.on() # dann led an
        else:
            self.off() # sonst led aus
        
        
        
