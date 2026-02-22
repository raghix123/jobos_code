from pybricks.tools import wait
from bob import Bob
from pybricks.parameters import Stop

def execute(bob: Bob):
    yield from bob.foreward(20,60)

    yield from bob.turn_front_motor(240,150)

    yield from bob.turn(-25,60)

    yield from bob.turn(25,60)

    yield from bob.turn_front_motor(-240,150)

    yield from bob.foreward(280,100)
    
    yield from bob.run_front_motor_until_stalled(400, then=Stop.HOLD, duty_limit=30)
    
    wait(100)
    
    # yield from bob.foreward_and_front_motor(-80,180,-350,150)

    yield from bob.foreward(-400, 300)

    yield from bob.foreward(20,100)

    yield from bob.turn(45,200)

    yield from bob.turn_front_motor(-350,100)

    yield from bob.foreward(-240,200)

