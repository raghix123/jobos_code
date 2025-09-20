import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward(distance=750, speed=200)
    #bob.turn(degree=-29)
    #bob.turn(degree=38)
    #bob.foreward(distance=-80, speed=100)
    #bob.turn(degree=20)
    #bob.foreward(distance=80, speed=100)
    #bob.turn_front_motor(degree=300, speed=100)
    #bob.foreward(distance=13, speed=100)
    #bob.turn_front_motor(degree=-300, speed=100)
    #bob.foreward(distance=-25, speed=100)
    #bob.turn(degree=-50)
    #bob.foreward(distance=-25, speed=100)
    #bob.foreward(-50,100)
    #bob.turn(-54)
    #bob.foreward(25,100)
    # for crash in range(5):    
    #     bob.turn_back_motor(degree=350, speed=2000)
    #     bob.turn_back_motor(degree=-350, speed=2000)
        