import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward(750,500)
    bob.turn(-34,150)
    wait(200)
    bob.turn(95,250)
    bob.turn(-55,250)
    bob.foreward(-30,250)
    bob.turn(-20,100)
    bob.foreward(12,250)
    bob.turn(-30,100)
    bob.foreward(-28,150)
    #bob.foreward(15,100)
    for crash in range(5):    
        bob.turn_back_motor(380,4000)
        bob.turn_back_motor(-380,4000)
    bob.turn(45,250)
    bob.foreward(-700,1000)
    # bob.turn(degree=-29, speed=60)
    # bob.turn(degree=38, speed=60)
    # bob.foreward(distance=-45, speed=50)
    # bob.turn(degree=30, speed=60)
    # bob.foreward(distance=20, speed=50)
    # bob.foreward(10,50)
    # bob.turn_front_motor(degree=300, speed=60)
    # bob.foreward(distance=13, speed=100)
    # bob.turn_front_motor(degree=-300, speed=100)
    # bob.foreward(distance=-25, speed=100)
    # bob.turn(degree=-50)
    # bob.foreward(distance=-25, speed=100)
    # bob.foreward(-50,100)
    # bob.turn(-54)
    # bob.foreward(25,100)
    # for crash in range(5):    
    #     bob.turn_back_motor(degree=350, speed=2000)
    #     bob.turn_back_motor(degree=-350, speed=2000)
        