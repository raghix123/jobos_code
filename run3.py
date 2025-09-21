from bob import Bob

def execute(bob: Bob):


    bob.turn_front_motor(-300,300)

    bob.foreward(distance=700, speed=100)

    bob.turn(52)

    bob.foreward(distance=205, speed=100)

    bob.turn_front_motor(300,200)

    bob.turn_back_motor(350,200)

    bob.reverse(400,200)

    bob.turn_back_motor(-300,300)

    bob.foreward(100,200)

    bob.turn(-45)

    bob.reverse(600,400)

