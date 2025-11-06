from bob import Bob

from pybricks.tools import wait

def execute(bob: Bob):

    bob.foreward(distance=700, speed=400)

    bob.turn(58,60)

    bob.foreward(distance=185, speed=200)

    bob.turn_front_motor(270,200)

    wait(200)

    bob.turn_front_motor(-270,200)

    bob.turn_back_motor(350,300)

    bob.reverse(200,400)

    bob.turn(17,100)

    bob.reverse(120,100)

    bob.turn_back_motor(-200,200)

    bob.foreward(100,1000)

    bob.turn(-60,100)

    bob.reverse(600,1000)

