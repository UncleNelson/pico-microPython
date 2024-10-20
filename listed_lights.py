import machine #Zugriff auf Pico - Pins
import utime #für die sleep() Funktion

# eine leere Liste erzeugen
lights = []

"""
Die Funktion erzeugt ein Lauflicht - Pattern, das alle LEDs
   der Reihe nach von links nach rechts einschaltet
   und dann wieder von links nach rechts ausschaltet
"""
def snakeOnOff():
    for led in lights: #über jedes Objekt in der Liste iterieren
        led.value(1) #Licht an
        utime.sleep(0.05) #kurz warten bis zum nächsten Durchlauf
        
    for led in lights: #und noch einmal über alle LEDs gehen
        led.value(0) #Licht aus
        utime.sleep(0.05) #und wider kurz warten bis zum nächsten Durchlauf


"""
Diese Funktion lässt abwechselnd alle LEDs mit geradem Index und
   alle LEDs mit ungeradem Index blinken
"""
def blinkeblinke():
    #---- Anfang äußere Schleife ---
    for i in range(4): #alles 4x wiederholen
    
        for index in range(7): #in einer range über die Liste iterieren
            #so können wir mit den Indizes rechnen
            if index % 2 == 0: #wenn (index / 2) keinen Restwert hat
                lights[index].value(1) #Licht am Index an
            else:
                lights[index].value(0) #sonst Licht am Index aus
        utime.sleep(0.3) #kurz warten
        
        #dann alles noch einmal umgekehrt
        for index in range(7):
            if index % 2 == 0: #kein Rest ?
                lights[index].value(0) #dann Licht am Index aus
            else:
                lights[index].value(1) #sonst Licht am Index an
        utime.sleep(0.3) #kurz warten
        
    #---- Ende äußere Schleife ---
    
    # nach den 4 Wiederholungen der äußeren Schleife
    # werden alle Lichter ausgeschaltet
    for led in lights:
        led.value(0)
            
    
        

## -------------- main  ----------------------------
for pin in range(7): # alle angeschlossenen LED in die Liste
    led = machine.Pin(pin, machine.Pin.OUT) #Objekt erstellen
    lights.append(led) #und anhängen
    
while True:
    select = input("1 = snakeOnOff, 2 = blinkeblinke :") #Benutzereingabe
    
    #wir prüfen auf "1" oder "2" und führen dann die jeweilige
    #Funktion aus
    if select == "1":
        snakeOnOff()
    elif select == "2":
        blinkeblinke()
   
    
