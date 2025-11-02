from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):
    bob.foreward_and_front_motor(foreward_distance=660, foreward_speed=500, turn_degree=395, turn_speed=500)
    # Ready

    bob.back_motor.reset_angle(0)
    for hit in range(5):
        bob.turn_back_motor_dc(dc=70, time=200)
        bob.back_motor.run_target(speed=500, target_angle=0, then = Stop.BRAKE)
    # Silo done
    
    bob.foreward(70, 200)
    bob.turn(degree=-24, speed=250, then=Stop.COAST)
    wait(200)
    # Who lived here done
    
    bob.turn(105,100)
    # Forge releases

    bob.foreward(120, 100)
    # Boulders recovered

    bob.turn_front_motor(60,100, then=Stop.BRAKE)
    bob.turn_front_motor(10,20, then=Stop.HOLD)
    bob.foreward(210,300)
    # Heavy lifting done

    bob.turn_front_motor(degree=-90, speed=100, then=Stop.BRAKE)
    # Lifting the arm

    bob.foreward(distance=-250, speed=300, then=Stop.BRAKE)
    bob.turn(90)
    bob.foreward(740,500)

    # # bob.turn(-170, 200)
    # # bob.foreward(-140, 200)
    
    # # # Moved back
    # # # bob.turn(-90,250)
    # # # bob.foreward(-30,250)
    # # # bob.turn(-20,100)
    # # # bob.foreward(12,250)
    # # # bob.turn(-40,100)
    # # # bob.foreward(-30,150)

    # # # Moved into position
    # # for crash in range(5):    
    # #     bob.turn_back_motor(380,4000)
    # #     bob.turn_back_motor(-380,4000)

    # # # # Got all the pills out    
    # # # bob.turn(45,250)
    # # # bob.foreward(-700,1000)
    
    # # # # Back home