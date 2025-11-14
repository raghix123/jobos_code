import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.turn_front_motor(degree=-50, speed=100)
    # Ready

    bob.arc(radius=-690, angle=25, then=Stop.BRAKE)
    bob.turn(degree=-60, speed=75, then=Stop.BRAKE)
    # Marketwares solved

    bob.foreward(distance=365, speed=200)
    bob.turn_back_motor(degree=-300, speed=1000)
    bob.turn_back_motor(degree=300, speed=1000)
    # Tip the scales A done

    bob.foreward(distance=-220, speed=200)
    bob.turn(degree=30, speed=75, then=Stop.BRAKE)
    bob.turn_front_motor(degree=60, speed=100)
    bob.turn(degree=-35, speed=200, then=Stop.BRAKE)
    # Tip the scales B done

    bob.arc(radius=-750, angle=-60, speed=400, then=Stop.COAST)
    return
    bob.arc(radius=-800, angle=-60, speed=1000, then=Stop.COAST)
    return
    
    
    
    
    # Below is an attempt to tip the scales
    bob.arc(radius=-300, angle=90)
    bob.turn_back_motor(degree=-250, speed=1000)
    bob.turn_back_motor(degree=250,speed=1000)
    return
    bob.foreward(280,300)
    bob.turn(-90,200)
    bob.foreward(440,300)
    bob.turn_back_motor(degree=-250, speed=1000)
    bob.turn_back_motor(degree=250,speed=1000)
    #challenge tip the scales A done

    return

    bob.turn(-90,200)
    bob.turn_front_motor(degree=300, speed=400)
    bob.turn(-15,200)
    bob.foreward(60,60)
    bob.turn_front_motor(degree=-200, speed=100)
    #challenge Angler Artifacts B done

    bob.foreward(distance=-60, speed=600)
    bob.turn(degree=105, speed=200)
    bob.foreward(distance=-530, speed=1500)
    bob.turn(degree=44, speed=200)
    bob.turn_front_motor_until_stalled(speed=300, duty_limit=40)
    bob.turn_front_motor(degree=-80, speed=300)
    bob.foreward(distance=70, speed=200)
    bob.turn(degree=-38, speed=200)
    # #challenge What's on Sale B done

    bob.foreward(200,300)
    bob.turn(18,200)
    bob.turn_front_motor_until_stalled(speed=300, duty_limit=40)
    #arm goes into challenge Tip the Scales B

    bob.turn(-30,200)
    bob.turn(20,200)
    bob.foreward(-800,1500)
    #Back home
