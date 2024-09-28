import machine
import utime

# definieren der drei LEDs, an welcher Pin-Nr., als Pin - Output
gruen = machine.Pin(0, machine.Pin.OUT)
gelb = machine.Pin(1, machine.Pin.OUT)
rot = machine.Pin(2, machine.Pin.OUT)

# Funktion zum Einschalten einer LED
def ledAn(led):
    led.value(1)
   
# Funktion zum Ausschalten einer LED
def ledAus(led):
    led.value(0)
    
# zum Warten einer angegebenen Zeit in Sekunden
def warte(sekunden):
    utime.sleep(sekunden)
    
# Eine Ampel-Sequenz in Deutschland
def ampelSequenz_d():
    ledAn(gruen)
    warte(2.0)
    ledAn(gelb)
    warte(0.7)
    ledAus(gruen)
    ledAus(gelb)
    ledAn(rot)
    warte(1.0)
    ledAus(rot)
    ledAn(gelb)
    warte(0.7)
    ledAus(gelb)
    
# Eine Ampel-Sequenz in Österreich
def ampelSequenz_a():
    ledAn(gruen)
    warte(2.0)
    blink(gruen, 5)
    ledAn(gelb)
    warte(0.7)
    ledAus(gelb)
    ledAn(rot)
    warte(1.0)
    ledAus(rot)
    ledAn(gelb)
    warte(0.7)
    ledAus(gelb)
    
# Alle LEDs ausschalten
def alleAus():
    ledAus(gruen)
    ledAus(gelb)
    ledAus(rot)
    
# Lässt eine LED blinken
def blink(led, wie_oft):
    if wie_oft < 1: # Ist das Argument kleiner als 1,
        return # wird die Funktion wieder verlassen
    for i in range(wie_oft - 1):
        led.value(1)
        utime.sleep(0.3)
        led.value(0)
        utime.sleep(0.3)
    led.value(1)
    utime.sleep(0.3)
    led.value(0)

# ---------- Main ----------
for i in range(2):
    print("Schleife: ", i)
    ampelSequenz_a()

   


