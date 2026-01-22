from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    yield from bob.back_motor.reset_angle(0)
    yield from bob.attachment_motor.reset_angle(0)
    yield from bob.foreward_and_front_motor(foreward_distance=640, foreward_speed=500, turn_degree=395, turn_speed=200)
    # Ready

    for hit in range(4):
        yield from bob.turn_back_motor_dc(dc=80, time=200)
        yield from bob.back_motor.run_target(speed=400, target_angle=0, then = Stop.BRAKE)
    # Silo done
    
    yield from bob.foreward(85, 200)
    yield from bob.turn(degree=-30, speed=250, then=Stop.COAST)
    wait(200)
    # Who lived here done
    
    yield from bob.turn(105, 100)
    yield from bob.turn(-65, 100)
    yield from bob.turn(65, 50)
    # Forge releases

    yield from bob.foreward(120, 100)
    # # Boulders recovered

    yield from bob.attachment_motor.run_target(speed=200, target_angle=470, then=Stop.HOLD)
    yield from bob.foreward(distance=210, speed=500)
    # Heavy lifting done

    yield from bob.turn_front_motor(degree=-90, speed=500, then=Stop.BRAKE)
    # Lifting the arm

    yield from bob.foreward(distance=-270, speed=300, then=Stop.BRAKE)
    yield from bob.turn(90)
    yield from bob.arc(radius=-775, angle=160, speed=400)
    # Home