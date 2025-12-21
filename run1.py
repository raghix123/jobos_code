import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    yield from bob.foreward(450,200)
    yield from bob.foreward(-150,200)
    yield from bob.foreward(250,200)
    yield from bob.foreward(-600,500)