import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward_and_front_motor(foreward_distance=525, foreward_speed=400, turn_degree=-110, turn_speed=300)
    bob.foreward(-150, 300)
    bob.foreward(200, 400)
    # Soil deposit removed

    bob.turn_front_motor(80, 100)
    bob.arc(radius=-460, angle=25, speed=200)
    bob.turn_front_motor(-300, 300)
    # Top soil removed

    bob.arc(radius=50, angle=-100, speed=75, then=Stop.HOLD)
    bob.arc(radius=-160, angle=-75, speed=75, then=Stop.BRAKE)
    bob.turn_back_motor_until_stalled(speed=450, duty_limit=40)
    bob.foreward(distance=-90, speed=100, then=Stop.COAST)
    # In position for statue rebuild
    
    bob.turn_back_motor_dc(dc=-100, time=200)
    wait(200)
    bob.turn(degree=-30, speed=100, then=Stop.COAST)
    wait(200)
    bob.turn(degree=30, speed=100, then=Stop.COAST)
    # Statue rebuilt

    bob.arc(radius=-200, angle=85, speed=500, then=Stop.COAST)
    bob.foreward(distance=600, speed=500)
    # Back home