from components import SwitchLight # importieren der Klasse aus dem Modul
import utime

# zwei Objekte der Klasse SwitchLight vereinbaren
light1 = SwitchLight(16, 15)
light2 = SwitchLight(17, 14)

# ... und in einer Dauerschleife anwenden
while True:
    light1.pulseOnTaster()
    light2.checkTasterAndToggle()
    utime.sleep(0.1)

