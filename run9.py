from pybricks.tools import wait
from bob import Bob

def execute(bob: Bob):

    yield from bob.foreward_and_front_motor(270,200,350,150)

    wait(2000)

    yield from bob.foreward(30,100)

    wait(2000)

    yield from bob.foreward(-275,300)

    yield from bob.turn_front_motor(-50,100)

    yield from bob.foreward(-300,200)

    yield from bob.foreward_and_front_motor(-60,200,350,150)

    yield from bob.foreward(320,300)
    