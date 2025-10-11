import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward(300,300)
    bob.turn(-90,150)
    bob.foreward(460,300)
    bob.turn_back_motor(-200,2000)
    bob.turn_back_motor(200,2000)
    bob.turn(-90,60)
    bob.turn_front_motor(350,200)
    bob.turn(-15,60)
    bob.foreward(60,60)
    bob.turn_front_motor(-200,100)
    bob.foreward(-60,60)
    bob.turn(105,60)
    bob.foreward(-510,300)
    bob.turn(44,150)
    bob.turn_front_motor(325,300)
    bob.foreward(90,300)
    bob.turn(-44,150)
    bob.foreward(190,300)
    bob.turn_front_motor(-40,300)
    bob.turn(25,150)
    bob.turn_front_motor(100,300)
    bob.turn(-30,60)
    bob.turn(20,60)
    #bob.turn_front_motor(-400,300)
    #bob.turn(60,150)
    bob.foreward(-700,400)
