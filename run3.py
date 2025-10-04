from bob import Bob

def execute(bob: Bob):

    bob.foreward(distance=700, speed=300)

    bob.turn(63,60)

    bob.foreward(distance=230, speed=200)

    bob.turn_front_motor(300,300)

    bob.turn_back_motor(420,300)

    bob.reverse(220,300)

    bob.turn(10,60)

    bob.reverse(50,100)

    bob.turn_back_motor(-200,300)

    bob.foreward(100,200)

    bob.turn(-45,60)

    bob.reverse(600,400)

