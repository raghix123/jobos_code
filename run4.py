import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    # bob.set_speed_factor(0.5)

    bob.turn_front_motor(395,500)
    # Ready to run

    bob.forward_safe(740,500)
    bob.turn_safe(-34,250, then=Stop.COAST)
    wait(200)
    # Who lived here is done
    
    bob.turn_safe(130,100, then=Stop.HOLD)
    # Forge is done

    bob.forward_safe(120, 100)
    # Boulders pushed

    bob.turn_front_motor(60,100, then=Stop.BRAKE)
    bob.turn_front_motor(10,20, then=Stop.HOLD)
    # Tool to pick up heavy thing down

    bob.forward_safe(180,300)
    # Pick up and dropped

    bob.forward_safe(-155,300)
    bob.turn_front_motor(-150,100)
    bob.forward_safe(-155,300)
    
    # Moved back    
    
    bob.turn_safe(-90,250)
    bob.forward_safe(-30,250)
    bob.turn_safe(-20,100)
    bob.forward_safe(12,250)
    bob.turn_safe(-40,100)
    bob.forward_safe(-30,150)

    # Moved into position
    for crash in range(5):    
        bob.turn_back_motor(380,4000)
        bob.turn_back_motor(-380,4000)

    # Got all the pills out    
    bob.turn_safe(45,250)
    bob.forward_safe(-700,1000)
    
    # Back home