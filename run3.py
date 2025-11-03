from bob import Bob

from pybricks.tools import wait

def execute(bob: Bob):

    # bob.foreward(distance=700, speed=400)

    # bob.turn(60,60)

    # bob.foreward(distance=175, speed=200)

    bob.turn_front_motor(200,200)

    wait(200)

    bob.turn_back_motor(500,300)

    bob.reverse(220,400)

    bob.turn(10,100)

    bob.reverse(50,100)

    bob.turn_back_motor(-200,300)

    bob.foreward(100,1000)

    bob.turn(-45,100)

    bob.reverse(600,1000)

