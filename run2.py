import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.turn_front_motor(-40,100)

    bob.foreward(745,500)

    bob.turn(-27,60)

    bob.foreward(55,100)

    bob.turn_front_motor(-300, 300)

    bob.foreward(distance=-25, speed=1000, then=Stop.HOLD)

    bob.turn(-70,100, Stop.HOLD)

    bob.foreward(-250,200, Stop.HOLD)
    
    bob.turn(65,60, Stop.HOLD)

    bob.turn_back_motor(450,500, Stop.HOLD)

    bob.foreward(distance=-175, speed=200, then=Stop.HOLD)

    bob.turn_back_motor(-225, 100, Stop.COAST)
    bob.turn_back_motor(degree=-225, speed=5000, then=Stop.COAST)

    bob.turn(degree=-10, speed=100, then=Stop.COAST)
    wait(200)
    # Statue rebuild done

    bob.foreward(distance=175, speed=200)
    bob.turn(degree=65, speed=200, then=Stop.BRAKE)
    bob.foreward(distance=-800, speed=800)
    # Back home
    

    # bob.turn(40)

    # bob.foreward(125,1000)

    # bob.turn(-40)

    # bob.foreward(300,1000)

    # bob.turn(-70)

    # bob.foreward(900,1000)