import machine
import utime

# Pin Nummer 15 als Input mit Pull-Down Widerstand definieren
# und in taster speichern
taster = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

# das On-Board LED in led speichern
led = machine.Pin("LED", machine.Pin.OUT)

while True: # Dauerschleife
    if taster.value() == 1: # Taster gedrückt?
        print("Taster gedrückt", end="\r")
        led.value(1) # on-board led an
    else: # sonst Taster nicht gedrückt
        print("_______________", end="\r")
        led.value(0) # on-board led aus
        
    utime.sleep(0.2) # 0.2 Sekunden schlafen
