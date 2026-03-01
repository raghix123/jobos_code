from pybricks.hubs import PrimeHub  # pyright: ignore[reportMissingImports]
from pybricks.pupdevices import Motor  # pyright: ignore[reportMissingImports]
from pybricks.parameters import Port, Direction, Stop  # pyright: ignore[reportMissingImports]
from pybricks.robotics import DriveBase  # pyright: ignore[reportMissingImports]
from pybricks.tools import wait  # pyright: ignore[reportMissingImports]

from bob import Bob

def execute(bob: Bob):
    yield from bob.reset_back_motor_angle(0)
    yield from bob.reset_attachment_motor_angle(0)
    yield from bob.foreward_and_front_motor(foreward_distance=620, foreward_speed=500, turn_degree=395, turn_speed=200)
    # Ready

    for hit in range(4):
        yield from bob.turn_back_motor_dc(dc=120, time=78)
        yield from bob.back_motor_run_target(speed=400, target_angle=0, then=Stop.BRAKE)
    # Silo done
    yield from bob.foreward(30,300)
    yield from bob.turn_to(-52,200, then=Stop.HOLD)
    yield from bob.foreward(360,300)
    yield from bob.foreward(-350,350)
    yield from bob.turn_to(0,300, then=Stop.HOLD)
    yield from bob.foreward(60, 350)
    yield from bob.turn(degree=-30, speed=250, then=Stop.HOLD)
    wait(200)
    # Who lived here done
    
    yield from bob.turn(105, 100)
    yield from bob.turn(-65, 100)
    yield from bob.turn_to(90, 50, then=Stop.HOLD)
    # Forge releases
    
    yield from bob.foreward(120, 100)
    # # Boulders recovered
    
    yield from bob.attachment_motor_run_target(speed=200, target_angle=480, then=Stop.HOLD)
    yield from bob.foreward(distance=210, speed=500)
    # Heavy lifting done
    

    yield from bob.turn_front_motor(degree=-90, speed=500, then=Stop.BRAKE)
    # Lifting the arm

    yield from bob.foreward(distance=-270, speed=300, then=Stop.BRAKE)
    yield from bob.turn(90)
    yield from bob.arc(radius=775, angle=-100, speed=400)
    # Home