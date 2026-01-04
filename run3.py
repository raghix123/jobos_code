from bob import Bob

from pybricks.tools import wait
from pybricks.parameters import Stop

def execute(bob: Bob):
    yield from bob.foreward(distance=320, speed=300, then=Stop.BRAKE)
    yield from bob.arc(radius=550, angle=50, then=Stop.BRAKE)
    yield from bob.turn_front_motor_dc(dc=70, time=650)
    wait(1000)
    yield from bob.turn_front_motor(degree=-180, speed=200, then=Stop.COAST)
    # Minecart sent

    yield from bob.turn_back_motor(degree=370, speed=400)
    yield from bob.arc(radius=-450, angle=-40, speed=200)
    yield from bob.turn_back_motor(degree=-120, speed=100)
    # Brush picked up
    
    yield from bob.arc(radius=90, angle=90, then=Stop.BRAKE)
    yield from bob.foreward_and_front_motor(foreward_distance=450, foreward_speed=500, turn_degree=180, turn_speed=200)
    # Back home