from pybricks.tools import wait
from bob import Bob

def execute(bob: Bob):
    yield from bob.foreward(20,60)

    yield from bob.turn_front_motor(240,150)

    yield from bob.turn(-25,60)

    yield from bob.turn(25,60)

    yield from bob.turn_front_motor(-240,150)

    yield from bob.foreward(280,100)

    yield from bob.turn_front_motor_dc(dc=60,time=220)
    
    wait(100)

    yield from bob.foreward_and_front_motor(-80,180,350,150)

    yield from bob.foreward(-350, 300)

    yield from bob.foreward(100,200)

    yield from bob.turn_front_motor(-350,100)

    yield from bob.foreward(-240,200)

