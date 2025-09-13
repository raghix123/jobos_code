from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Note
from pybricks.tools import wait

hub = PrimeHub()
    
number = 1
hub.display.number(number)

while True:
    pressed = hub.buttons.pressed()

    # RIGHT button cycles through 1 → 5
    if Button.RIGHT in pressed:
        number += 1
        if number > 5:
            number = 1
        hub.display.number(number)
        wait(300)

    # LEFT button plays tune for current number
    elif Button.LEFT in pressed:
        if number == 1:
            hub.speaker.play_notes([Note.C4, Note.E4, Note.G4])  # C major
            
        elif number == 2:
            hub.speaker.play_notes([Note.D4, Note.F4, Note.A4])  # D minor
        elif number == 3:
            hub.speaker.play_notes([Note.E4, Note.G4, Note.B4])  # E minor
        elif number == 4:
            hub.speaker.play_notes([Note.F4, Note.A4, Note.C5])  # F major
        elif number == 5:
            hub.speaker.play_notes([Note.G4, Note.B4, Note.D5])  # G major
        wait(300)

    wait(50)
