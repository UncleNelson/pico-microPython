import machine
import utime
from components import SwitchLight # Die Klasse SwitchLight aus components importieren
import _thread # Modul um auf den zweiten Kern zuzugreifen

# die zwei LEDs und Taster
ledLeft = SwitchLight(16,15)
ledRight = SwitchLight(17,14)

# das Lock ist wichtig um die die Variable backFlag
# immer nur von einem Tread verwendbar zu machen
a_lock = _thread.allocate_lock()
backFlag = True

# Eine Schleife für das linke LED
# diese Schleife - in einer eigenen Funktion
# schicken wir dann auf den Background-Thread
def backgroundLoop():
    print("backgroundLoop start")
    while backFlag == True:
        ledLeft.blinkOnTaster(4)
        utime.sleep(0.1)
    print("backgroundLoop end")
    
# Die Methode für die Schleifen auf dem Main-Thread.
def mainLoop():
    global backFlag
    print("mainLoop start")
    while True:
        try:                            # im try-Block wird einfach der Code
            ledRight.blinkOnTaster(4)   # abgearbeitet, der ausgeführt werden soll
            utime.sleep(0.1)
        except KeyboardInterrupt:
            with a_lock:                # Wir schließen das Schloss zu
                backFlag = False        # und bearbeiten unser Flag, damit wird der
            utime.sleep(2)              # Background-Thread zuerst angehalten
            break           # und hier steigen wir dann aus der Dauerschleife im
    print("mainLoop end")   # Main-Thread aus


# # ---------------- Programm Start ------------------
_thread.start_new_thread(backgroundLoop, ()) # wir starten zuerst den Background-Thread
                                            # da er nicht blockierend arbeitet
mainLoop()                  # danach starten wir die Dauerschleife auf dem Main-Thread
                            # .. das Programm läuft solange, bis alle Anweisungen auf dem
                            # Main-Thread abgearbeitet sind.
        
