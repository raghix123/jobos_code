import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    # bob.foreward(660,100)
    # bob.foreward(-100,100)


    yield from bob.foreward_and_front_motor(480,250,-50,250, Stop.HOLD)
    yield from bob.turn_front_motor(50,250)
    yield from bob.foreward(-50,250)
    yield from bob.turn_front_motor(-300,250)
    yield from bob.foreward(270,250)
    yield from bob.turn_back_motor(100,250)
    yield from bob.foreward(-640,400)


    # bob.foreward(480,100)
    # bob.turn_front_motor(420,100)
    # bob.foreward(-50,100)
    # bob.turn_front_motor(-300,100)
    # bob.foreward(270,100)
    # bob.turn_back_motor(100,60)
    # bob.foreward(-640,300)


    # bob.foreward(80,100)
    # bob.turn(100,100)
    # bob.foreward(32,100)
    # bob.turn(-15,60)
    # bob.turn_front_motor(-2000,300)

    # bob.foreward(450,200)
    # bob.foreward(-150,200)
    # bob.foreward(250,200)
    # bob.foreward(-600,500)