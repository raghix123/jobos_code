import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.turn_front_motor(-40,100)
    # Ready

    bob.foreward(745,500)
    # Soil deposit #1 done

    bob.turn(-27,60)
    bob.foreward(55,100)
    bob.turn_front_motor(-300, 300)
    # Topsoil removed


    bob.foreward(distance=-10, speed=500, then=Stop.HOLD)
    bob.turn(degree=30, speed=100, then=Stop.HOLD)
    bob.foreward(distance=-400, speed=750, then=Stop.HOLD)
    # Soil deposit #2 done

    # Compensate to get back to same position as old code
    bob.foreward(distance=400, speed=750, then=Stop.HOLD)
    bob.turn(degree=-30, speed=100, then=Stop.HOLD)
    bob.foreward(distance=10, speed=500, then=Stop.HOLD)
    bob.foreward(distance=-25, speed=1000, then=Stop.HOLD)

    bob.turn(degree=-70, speed=100, then=Stop.HOLD)
    bob.foreward(distance=-250, speed=200, then=Stop.HOLD)
    bob.turn(degree=65, speed=60, then=Stop.BRAKE)
    bob.turn_back_motor_until_stalled(speed=450, duty_limit=40)
    # Lifting arm down

    bob.foreward(distance=-175, speed=200, then=Stop.BRAKE)

    bob.turn_back_motor_dc(dc=-60, time=200)
    wait(200)
    bob.turn(degree=-30, speed=100, then=Stop.COAST)
    wait(200)
    bob.turn(degree=30, speed=100, then=Stop.COAST)
    # Statue rebuild done

    bob.foreward(distance=100, speed=100, then=Stop.COAST)
    bob.turn_back_motor_until_stalled(speed=450, duty_limit=40)
    bob.drivebase.arc(radius=-185, distance=500, then=Stop.COAST)
    bob.foreward(distance=500, speed=500)
    # Back home