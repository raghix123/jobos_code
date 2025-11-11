import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward(450,200)
    bob.foreward(-150,200)
    bob.foreward(250,200)
    bob.foreward(-600,500)