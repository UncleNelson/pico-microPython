""" für das Arbeiten mit uasyncio muss auch
    SwitchLight ein bisschen erweitert werden.
    Bitte sieh dir dazu auch die Änderungen in der Klasse
    SwitchLight() an.
    Sei befindet sich in der Datei: components.py """

import uasyncio as aio # muss importiert werden für async, await
from components import SwitchLight

# die zwei SwitchLights werden nach wie vor mit
# LED- und Taster Pins initialisiert
# (die Pin-Nummern müssen natürlich dementsprechend an deinen eigenen Aufbau
#  angepasst werden)
ledLeft = SwitchLight(16,14)
ledRight = SwitchLight(17,15)

async def mainTask(): # die ausführende Funktion muss im async-Kontext sein
    
    # jede SwitchLight hat jetzt einen eigenen Event-Listener
    # und wird in einem Task aufgerufen
    # Tasks werden von uasyncio als asynchron laufende Aufgabe behandelt
    t1 = aio.create_task(ledLeft.listen()) 
    t2 = aio.create_task(ledRight.listen())
    # diese zwei Aufrufe starten beide Tasks parallel
    await t1 
    await t2
    
    
aio.run(mainTask()) # mit .run startet nun das Script