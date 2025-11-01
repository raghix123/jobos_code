import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.set_speed_factor(1)
    bob.turn_front_motor(-40,100)

    bob.foreward(745,500)

    bob.turn(-27,60)

    bob.foreward(55,100)

    bob.turn_front_motor(-300, 300)

    bob.reverse(25,1000)

    bob.turn(-70,100)

    bob.reverse(250,200)
    
    bob.turn(65,60)

    bob.turn_back_motor(450,500)

    bob.reverse(175,200)
    
    bob.turn_back_motor(-150,200)

    bob.turn(-30)
    
    wait(200)

    bob.turn(40)

    bob.foreward(250,1000)

    bob.turn(60)

    bob.reverse(800,1000)