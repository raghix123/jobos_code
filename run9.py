from pybricks.tools import wait
from pybricks.parameters import Stop
from bob import Bob


def execute(bob: Bob):
    yield from bob.foreward(distance=410, speed=400)
    
    yield from bob.turn_front_motor_dc(dc=40, time=500)

    yield from bob.foreward(distance=40, speed=100)

    yield from bob.turn_front_motor(degree=-135, speed=100)

    yield from bob.foreward(distance=100, speed=100)

    yield from bob.foreward(distance=-100, speed=100)
    
    return
    # yield from bob.foreward(distance=30, speed=100)
    # yield from bob.turn_front_motor(degree=-90, speed=100)
    yield from bob.foreward_and_front_motor(foreward_distance=50, foreward_speed=100, turn_degree=-90, turn_speed=300)
    yield from bob.turn_front_motor(-200,500)
    yield from bob.foreward(distance=-120, speed=100)