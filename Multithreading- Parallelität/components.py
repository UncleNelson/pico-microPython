import machine
import utime

# eine Klasse mit class einleiten und den Namen SwitchLight geben
class SwitchLight:
    
    # Die Klasse soll eine Pin Nummer für eine LED übergeben bekommen
    # und eine Pin Nummer für einen Taster
    # und fasst diese beiden Komponenten somit in einem Objekt zusammen
    
    # der Konstruktor
    #    'self' muss in jeder Methode der Klasse als erster
    #    Parameter stehen
    def __init__(self, ledPin, tasterPin):
        # im Konstruktor findet das Initialisieren der Klasse
        # und ihrer Eigenschaften statt
        # hier wird z.B. die LED und der Taster richtig eingestellt
        self.led = machine.Pin(ledPin, machine.Pin.OUT)
        self.taster = machine.Pin(tasterPin, machine.Pin.IN, machine.Pin.PULL_DOWN)
        
    # Methode zum leuchten lassen der LED bei Taster Druck
    def checkTasterAndToggle(self):
        if self.taster.value() == 1:
            self.led.value(1)
        else:
            self.led.value(0)
            
    # Methode zum Pulsieren lassen der LED bei Taster Druck
    def pulseOnTaster(self):
        if self.taster.value() == 1:
            self.led.toggle()
            utime.sleep(0.05)
            self.led.toggle()
            utime.sleep(0.1)
        else:
            self.led.value(0)
        
    # Bei Tasterdruck blinken
    def blinkOnTaster(self, blinkCount):
        if self.taster.value() == 1:
            for i in range(blinkCount):
                self.led.value(1)
                utime.sleep(0.05)
                self.led.value(0)
                utime.sleep(0.4)
        else:
            self.led.value(0)
            
    
    
        
        