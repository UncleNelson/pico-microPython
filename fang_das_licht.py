import machine
import utime
import random # Für die Ermittlung eines zufälligen Index

#Die LEDs initialisieren
led_gelb = machine.Pin(16, machine.Pin.OUT)
led_gruen = machine.Pin(17, machine.Pin.OUT)
led_rot = machine.Pin(18, machine.Pin.OUT)

#Die Taster initialisieren
taster_gelb = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
taster_gruen = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
taster_rot = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

#Je ein LED und einen Taster in eine Liste geben
#Die Elementen können jetzt mit z.B. block_1[0] und block_1[1] angesprochen werden
block_1 = [led_gelb, taster_gelb]
block_2 = [led_gruen, taster_gruen]
block_3 = [led_rot, taster_rot]

"""
Zusätzlich geben wir alle drei Blocks in eine Liste.
Damit können wir einen zufälligen Index zwischen 0 und 2 ermitteln
und einen Block daraus zufällig auswählen.
"""
blocks = [block_1, block_2, block_3]

"""
Zur lesbareren Darstellung im Code.
Wir können jetzt z.B. auf das LED im block_1 wie folgt zugreifen:
blog_1[led]
"""
led = 0
taster = 1

#Globale Variablen zur Spielsteuerung
isRunning = True  #Flag für die Spiel-Laufzeit
punkte = 0        #Punkte, wir starten mit 0 Punkten ins Spiel
gewinngrenze = 13 #Bei erreichter Grenze an Punkten haben wir gewonnen
wartezeit = 30    #Definition ist in Zyklen (wir definieren einen Zyklus später mit 0.1 Sekunden)

#Es wird ein zuvor ermittelter block und die Anzahl
#an Zyklen übergeben, die zur Auswertung durchlaufen werden sollen.
def leuchten(block, zyklen):

    #Um globale Variablen innerhalb einer Funktion zu verändern,
    #muss man sie mit dem Schlüsselwort 'global' annotieren
    global punkte
    global wartezeit

    block[led].value(1) #das LED des Blocks leuchtet auf
    for zyklus in range(zyklen): #Zyklen durchlaufen
        if block[taster].value() == 1: #ist der Taster gerade gedrückt?
            #Wenn Ja, dann:
            punkte += 1 #plus einen Punkt
            if punkte % 2 == 0: #Wenn die aktuellen Punkte durch 2 keinen Rest haben
                wartezeit -= 4 #verküren wir die Zyklen um 4
            block[led].value(0) #LED wieder aus
            return #Funktion sofort verlassen

        utime.sleep(0.1)#die Zeit, die ein Zyklus in Anspruch nehmen soll in Sekunden

    #wenn alle Zyklen durchlaufen sind, und der Taster nicht dedrückt wurde
    #kommen wir hier an. Nach der for-Schleife
    punkte -= 1 #dann wird ein Punkt abgezogen
    wartezeit += 4 #die Zyklen werden wieder um 4 erhöht
    block[led].value(0) #und natürlich die LED wieder ausgeschaltet


#diese Funktion überprüft, ob gewonnen oder verloren wurde
def gewonnenVerloren():
    global isRunning #in beiden Fällen muss isRunning auf false gesetzt werden
    if punkte <= 0: #0 Punkte heißt: Verloren
        verloren()
        isRunning = False #Das Spiel ist zu Ende
    elif punkte == gewinngrenze: #ist die Gewinngrenze erreicht, ist das Spiel gewonnen
        gewonnen()
        isRunning = False #Das Spiel ist zu Ende


#Sequenz, wenn das Spiel verloren wurde
def verloren():
    print("------- Leider Verloren --------") #in der Konsole ausgeben
    #Die LED im block_3 neunmal aufblinken lassen
    for i in range(9):
        block_3[led].value(1)
        utime.sleep(0.3)
        block_3[led].value(0)
        utime.sleep(0.1)
        

#Sequenz, wenn das Spiel gewonnen wurde
def gewonnen():
    print("*********** GEWONNEN ***********") #in der Konsole ausgeben

    #ein Lauflicht mit allen LEDs erzeugen
    for i in range(9):
        for block in blocks:
            block[led].value(1)
            utime.sleep(0.1)
            block[led].value(0)
        machine.Pin("LED").value(1) #einschließlich der On-Board LED
        utime.sleep(0.1)
        machine.Pin("LED").value(0)
        

#für die Ausgabe des aktuellen Spielstand in der Konsole
def statusAusgeben():
    ausgabe = f"Spiel läuft ... Punkte: {punkte}" #ein formatierter String, der
                                                  #die globale Variable 'punkte' mit einbezieht
    print(ausgabe, end=" \r") #Ausgabe in der Konsole
                            #\r setzt den Cursor wieder an den Anfang der Zeile



# Ab hier beginnt die Programmlogik
#
# -------------- Main -------------------------
statusAusgeben() #als erstes den Status einmal ausgeben
while isRunning: #solange isRunning == true
    blockIndex = random.randrange(3) #zufälliger Index zwischen 0 und 2
    leuchten(blocks[blockIndex], wartezeit) #wir übergeben den zufällig ermittelten Block aus
                                            #der Liste und die globale Variable 'wartezeit'
    statusAusgeben() #wieder den Spielstand ausgeben
    gewonnenVerloren() #prüfen ob gewonnen oder verloren wurde
    waitTime = random.randrange(20) #zufällige Zahl zwischen 0 und 19
    utime.sleep((waitTime / 10) + 0.5) #geteilt durch 10 = Sekunden
                                       #plus 0.5 Sekunden
                                       #Bsp: waitTime = 7
                                       # -> (7 / 10) = 0.7 Sekunden
                                       # -> + 0.5 = 1.2 Sekunden







