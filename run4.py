import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward(distance=750, speed=200)
    bob.turn(degree=-25)
    bob.turn(degree=40)
    bob.foreward(distance=-80, speed=100)
    bob.turn(degree=25)
    bob.foreward(distance=50, speed=100)
    bob.turn_front_motor(degree=270, speed=100)
    bob.foreward(distance=15, speed=100)
    bob.turn_front_motor(degree=-270, speed=100)
    bob.foreward(distance=25, speed=100)
    bob.turn(degree=-50)
    bob.foreward(distance=-10, speed=10)
    
    for crash in range(5):    
        bob.turn_back_motor(degree=350, speed=2000)
        bob.turn_back_motor(degree=-300, speed=1000)