from bob import Bob

from pybricks.tools import wait
from pybricks.parameters import Stop

def execute(bob: Bob):
    bob.foreward(distance=320, speed=300, then=Stop.BRAKE)
    bob.arc(radius=550, angle=50, then=Stop.BRAKE)
    bob.turn_front_motor_dc(dc=70, time=650)
    wait(1000)
    bob.turn_front_motor(degree=-180, speed=200, then=Stop.COAST)
    # Minecart sent

    bob.turn_back_motor(degree=370, speed=400)
    bob.arc(radius=-450, angle=-40, speed=200)
    bob.turn_back_motor(degree=-120, speed=100)
    # Brush picked up
    
    bob.arc(radius=90, angle=90, then=Stop.BRAKE)
    bob.foreward_and_front_motor(foreward_distance=450, foreward_speed=500, turn_degree=180, turn_speed=200)
    # Back home