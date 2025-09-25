from bob import Bob

def execute(bob: Bob):

    bob.foreward(distance=700, speed=100)

    bob.turn(63,60)

    bob.foreward(distance=230, speed=100)

    bob.turn_front_motor(300,200)

    bob.turn_back_motor(420,200)

    bob.reverse(220,100)

    bob.turn(10,60)

    bob.reverse(40,100)

    bob.turn_back_motor(-200,100)

    bob.foreward(100,200)

    bob.turn(-45,60)

    bob.reverse(600,400)

