import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.turn_front_motor(395,500)
    # Ready

    bob.foreward(690, 500)
    for hit in range(5):
        bob.turn_back_motor(degree=535, speed=5000, then=Stop.COAST)
        bob.turn_back_motor(degree=-535, speed=1000, then=Stop.COAST)
    # Silo done
    
    bob.foreward(40, 200)
    bob.turn(-24,250)
    wait(200)
    # Who lived here done
    
    bob.turn(115,100)
    # Forge releases

    bob.foreward(120, 100)
    # Boulders recovered

    # bob.turn_front_motor(60,100, then=Stop.BRAKE)
    # bob.turn_front_motor(10,20, then=Stop.HOLD)
    # bob.foreward(180,300)
    # # Just knocked off the weighted thing

    # bob.foreward(-155,300)
    # bob.turn_front_motor(-150,100)
    # bob.foreward(-300,300)

    # bob.turn(-170, 200)
    # bob.foreward(-140, 200)
    
    # # Moved back
    # # bob.turn(-90,250)
    # # bob.foreward(-30,250)
    # # bob.turn(-20,100)
    # # bob.foreward(12,250)
    # # bob.turn(-40,100)
    # # bob.foreward(-30,150)

    # # Moved into position
    # for crash in range(5):    
    #     bob.turn_back_motor(380,4000)
    #     bob.turn_back_motor(-380,4000)

    # # # Got all the pills out    
    # # bob.turn(45,250)
    # # bob.foreward(-700,1000)
    
    # # # Back home