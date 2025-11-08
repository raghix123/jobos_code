from bob import Bob

from pybricks.tools import wait
from pybricks.parameters import Stop

def execute(bob: Bob):
    bob.foreward(distance=320, speed=400, then=Stop.BRAKE)
    bob.arc(radius=550, angle=50, then=Stop.BRAKE)
    bob.turn_front_motor_dc(dc=60, time=485)
    wait(1000)
    bob.turn_front_motor(degree=-180, speed=200, then=Stop.COAST)
    # Minecart sent

    bob.turn_back_motor(degree=380, speed=400)
    bob.arc(radius=-450, angle=-40, speed=200)
    bob.turn_back_motor(degree=-120, speed=100)
    # Brush picked up

    bob.arc(radius=90, angle=90, then=Stop.BRAKE)
    bob.foreward_and_front_motor(foreward_distance=300, foreward_speed=500, turn_degree=180, turn_speed=200)


    # bob.drivebase.arc(radius=90, angle=90)


    # bob.foreward(distance=700, speed=400)

    # bob.turn(58,60)

    # bob.foreward(distance=185, speed=200)

    # bob.turn_front_motor(270,200)

    # wait(200)

    # bob.turn_front_motor(-270,200)

    # bob.turn_back_motor(350,300)

    # bob.reverse(200,400)

    # bob.turn(17,100)

    # bob.reverse(120,100)

    # bob.turn_back_motor(-200,200)

    # bob.foreward(100,1000)

    # bob.turn(-60,100)

    # bob.reverse(600,1000)

