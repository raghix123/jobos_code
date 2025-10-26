import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward(300,300)
    bob.turn(-90,200)
    bob.foreward(460,300)
    bob.turn_back_motor(260,2000)
    bob.turn_back_motor(-260,2000)
    #challenge tip the scales A done
    bob.turn(-90,200)
    bob.turn_front_motor(380,400)
    bob.turn(-15,200)
    bob.foreward(60,60)
    bob.turn_front_motor(-230,150)
    #challenge Angler Artifacts B done
    bob.foreward(-60,600)
    bob.turn(105,200)
    bob.foreward(-510,1500)
    bob.turn(44,200)
    bob.turn_front_motor(310,300)
    bob.foreward(90,300)
    bob.turn(-38,200)
    #challenge What's on Sale B done
    bob.foreward(180,300)
    bob.turn_front_motor(-50,300)
    bob.turn(15,200)
    bob.turn_front_motor(120,300)
    #arm goes into challenge Tip the Scales B
    bob.turn(-30,200)
    bob.turn(20,200)
    bob.foreward(-800,1500)
    #Back home
