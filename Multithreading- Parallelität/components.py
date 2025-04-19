import machine
import utime
import uasyncio as aio

# eine Klasse mit class einleiten und den Namen SwitchLight geben
class SwitchLight:

    # Die Klasse soll eine Pin Nummer für eine LED übergeben bekommen
    # und eine Pin Nummer für einen Taster
    # und fasst diese beiden Komponenten somit in einem Objekt zusammen
    
    
    running = False # Erweiterung für das Event-Handling im asynchronen Kontext
    
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
            
""" ----------------------------------------------------------------------
die nächsten beiden Methoden sind für den
    Kontext mit uasyncio vorgesehen """
     
    # eine mit async gekennzeichnete Methode ist eine Koroutine
    # Sie wird als "Task" mit dem Modul uasyncio gestartet.
    #
    # Jedes drin befindliche await ist innerhalb der Methode sequenziell
    # aber der Pico kann in diesen Phasen andere Koroutinen parallel
    # abarbeiten.
    async def asyncBlink(self, times):
        for i in range(times):
            self.led.value(1)
            await aio.sleep(0.05)
            self.led.value(0)
            await aio.sleep(0.4)
        self.running = False # running wieder auf False setzen um das Event freizugeben
    
    
    async def listen(self):
        while True:
            
            # wenn running False ist und der Taster gedrückt wird, kann das Event stattfinden
            if self.running == False and self.taster.value() == 1:
                
                # running auf True setzen, damit das Event während des Blinkens gesperrt ist
                self.running = True
                
                # die Koroutine als Task mit await aufrufen
                task = aio.create_task(self.asyncBlink(4))
                await task
                
            # es ist wichtig innerhalb der Dauerschleife ein wenig Zeit
            # für andere Koroutinen zu lassen
            await aio.sleep(0.2)
            
            
            
            
            
            
            
            
            
