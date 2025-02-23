import machine
import utime

class Bodensensor:
    
    def __init__(self, pin):
        self.sensor = machine.ADC(pin) # den sensor initialisieren
        self.max_wert = 57000          # der ermittelte maximale Wert
        self.min_wert = 25400          # der ermittelte minimale Wert
        self.messungen = []            # Liste für die Bestimmung des Mittelwerts
                                       #    der Messungen

    # Die Methode liefert den reinen ADC Wert
    def rohwert(self):
        return self.sensor.read_u16()

    # Umrechnung des Wertes in Prozent
    def prozent(self):
        # der höchste Wert zwischen 25400 und 57000
        # ... also 31600
        hoechstwert = self.max_wert - self.min_wert

        # der Maximalwert minus des gemessenen Rohwerts ergibt die eigentliche Messung
        # mit max(wert, 0) verhindern wir einen Negativen Wert
        messung = max((self.max_wert - self.rohwert()), 0)

        # Dreisatzrechnung für den prozendualen Wert
        prozent =  messung * 100 / hoechstwert

        return prozent
    
    def durchschnitt(self):
        messung = int(self.prozent()) # der Prozentwert als Ganzzahl

        self.messungen.append(messung) # messung in die Liste hinzufügen

        # die Summe aller Elemente in der Liste geteilt durch die
        # Anzahl der Elemente in der Liste ergibt den Mittelwert
        # Auch hier konvertieren wir in eine Ganzzahl und schneiden die
        # Nachkommastellen ab
        schnitt = int(sum(self.messungen) / len(self.messungen))

        # Wenn die Liste mehr als 20 messungen hat, entfernen wir den ersten
        # Eintrag, um zu verhindern, dass die Liste immer länger wird
        # und es zu einem Memory Leak kommt
        if len(self.messungen) > 20:
            self.messungen.pop(0)

        # Den Mittelwert in der Konsole ausgeben
        return schnitt



# --------------- Benutzung der Klasse ---------------------------

sensor = Bodensensor(27)

while True:
    messung = sensor.durchschnitt()
    print(messung, end= " \r")
    utime.sleep(0.2)

