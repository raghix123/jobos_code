from bob import Bob

from pybricks.tools import wait
from pybricks.parameters import Stop

def execute(bob: Bob):
    yield from bob.foreward(-275, 1200)
    yield from bob.turn(-32, 500)
    yield from bob.foreward(-360, 1200)