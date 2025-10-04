<<<<<<< HEAD
import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward(300,250)
    bob.turn(-90,150)
    bob.foreward(450,250)
    bob.turn_back_motor(250,2000)
    bob.turn_back_motor(-350,2000)
    bob.foreward(-510,250)
    bob.turn(44,150)
    # bob.foreward(-300,100)
    bob.turn_front_motor(440,300)
    bob.foreward(80,250)
    bob.turn(-44,150)
    bob.foreward(190,250)
    bob.turn_front_motor(-40,300)
    bob.turn(20,150)
    bob.turn_front_motor(85,300)
    bob.turn(-70,150)
    bob.turn_front_motor(-400,300)
    bob.turn(60,150)
    bob.foreward(-500,250)


    # bob.turn_front_motor(475,100)
    # bob.foreward(270,100)
    # bob.turn(-30,100)
    # bob.foreward(150,100)
    # bob.turn(-65,100)
    # bob.turn_front_motor(-50,100)
=======
from bob import Bob

def execute(bob: Bob):
    bob.foreward(200,100)
>>>>>>> 82624e1 (Made code faster)
