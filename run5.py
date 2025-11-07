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
    bob.turn_back_motor(degree=-180, speed=1000)
    bob.turn_back_motor(degree=180,speed=1000)
    #challenge tip the scales A done

    bob.turn(-90,200)
    bob.turn_front_motor(degree=300, speed=400)
    bob.turn(-15,200)
    bob.foreward(60,60)
    bob.turn_front_motor(degree=-200, speed=100)
    #challenge Angler Artifacts B done

    bob.foreward(distance=-60, speed=600)
    bob.turn(degree=105, speed=200)
    bob.foreward(distance=-510, speed=1500)
    bob.turn(degree=44, speed=200)
    bob.turn_front_motor_until_stalled(speed=300, duty_limit=30)
    bob.turn_front_motor(degree=-80, speed=300)
    bob.foreward(distance=70, speed=200)
    bob.turn(degree=-38, speed=200)
    # #challenge What's on Sale B done

    bob.foreward(180,300)
    bob.turn(15,200)
    bob.turn_front_motor_until_stalled(speed=300, duty_limit=30)
    #arm goes into challenge Tip the Scales B

    bob.turn(-30,200)
    bob.turn(20,200)
    bob.foreward(-800,1500)
    #Back home
