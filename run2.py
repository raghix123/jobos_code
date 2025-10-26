import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):

    bob.foreward(745,500)

    bob.turn(-25,60)

    bob.foreward(20,100)

    bob.turn_front_motor(-300, 300)

    bob.reverse(25,1000)

    bob.turn(-25,100)

    bob.reverse(100,1000)

    bob.turn(-75,100)

    bob.reverse(125,1000)

    bob.turn(72,100)

    bob.reverse(100,1000)

    bob.turn_back_motor(450,500)

    bob.reverse(110,300)
    
    bob.turn_back_motor(-150,200)

    bob.turn(-30)
    
    wait(200)

    bob.turn(40)

    bob.foreward(250,1000)

    bob.turn(60)

    bob.reverse(800,1000)