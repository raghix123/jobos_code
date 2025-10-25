import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.turn_front_motor(395,500)
    bob.foreward(740,500)
    bob.turn(-34,250)
    wait(200)
    bob.turn(130,100)

    bob.foreward(120, 100)
    bob.turn_front_motor(60,100, then=Stop.BRAKE)
    bob.turn_front_motor(10,20, then=Stop.HOLD)
    bob.foreward(180,300)
    
    # Just knocked off the weighted thing

    bob.foreward(-155,300)
    bob.turn_front_motor(-150,100)
    bob.foreward(-155,300)
    
    # Moved back    
    
    bob.turn(-90,250)
    bob.foreward(-30,250)
    bob.turn(-20,100)
    bob.foreward(12,250)
    bob.turn(-40,100)
    bob.foreward(-30,150)

    # Moved into position
    for crash in range(5):    
        bob.turn_back_motor(380,4000)
        bob.turn_back_motor(-380,4000)

    # Got all the pills out    
    bob.turn(45,250)
    bob.foreward(-700,1000)
    
    # Back home