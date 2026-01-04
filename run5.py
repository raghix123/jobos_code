import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    yield from bob.turn_front_motor(degree=-50, speed=100)
    # Ready

    yield from bob.foreward(distance=375, speed=200)
    yield from bob.turn(degree=-45, speed=75, then=Stop.BRAKE)
    # Marketwares solved

    yield from bob.foreward(distance=365, speed=200)
    yield from bob.turn_back_motor(degree=-300, speed=1000)
    yield from bob.turn_back_motor(degree=300, speed=1000)
    # Tip the scales A done

    yield from bob.foreward(distance=-210, speed=200)
    yield from bob.turn(degree=32, speed=75, then=Stop.BRAKE)
    yield from bob.turn_front_motor(degree=60, speed=100)
    yield from bob.turn(degree=-35, speed=75, then=Stop.HOLD)
    wait(500)
    # Tip the scales B done

    yield from bob.foreward(distance=400, speed=800)
    yield from bob.arc(radius=-1500, angle= 60, speed= 800, then= Stop.COAST)
    # Back home
    
