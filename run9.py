from pybricks.tools import wait
from pybricks.parameters import Stop
from bob import Bob


def execute(bob: Bob):
    yield from bob.foreward(distance=420, speed=400)
    yield from bob.turn_front_motor_dc(dc=40, time=500)
    yield from bob.foreward(distance=40, speed=100)
    yield from bob.turn_front_motor(degree=-90, speed=100)
    # yield from bob.foreward_and_front_motor(foreward_distance=150, foreward_speed=100, turn_degree=-80, turn_speed=500)
    yield from bob.turn_front_motor(-200,500)
    yield from bob.foreward(distance=-50, speed=100)