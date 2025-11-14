from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.back_motor.reset_angle(0)
    bob.attachment_motor.reset_angle(0)
    bob.foreward_and_front_motor(foreward_distance=640, foreward_speed=500, turn_degree=395, turn_speed=200)
    # Ready

    for hit in range(4):
        bob.turn_back_motor_dc(dc=80, time=200)
        bob.back_motor.run_target(speed=400, target_angle=0, then = Stop.BRAKE)
    # Silo done
    
    bob.foreward(85, 200)
    bob.turn(degree=-24, speed=250, then=Stop.COAST)
    wait(200)
    # Who lived here done
    bob.reset_imu_and_wait()
    bob.turn(105, 100, then=Stop.BRAKE)
    bob.turn(-65, 100, then=Stop.BRAKE)
    bob.turn(65, 50)
    # Turn to 90 degrees from original starting point (0)
    # IMU was reset to -24, so target is 90 - (-24) = 114 from reset point
    bob.turn(114 - bob.hub.imu.heading(), 50)
    
    # Forge releases

    bob.foreward(120, 100)
    # # Boulders recovered

    bob.attachment_motor.run_target(speed=200, target_angle=470, then=Stop.HOLD)
    bob.foreward(distance=210, speed=500)
    # Heavy lifting done

    bob.turn_front_motor(degree=-90, speed=500, then=Stop.BRAKE)
    # Lifting the arm

    bob.foreward(distance=-270, speed=300, then=Stop.BRAKE)
    bob.turn(90)
    bob.arc(radius=-775, angle=160, speed=400)
    # Home