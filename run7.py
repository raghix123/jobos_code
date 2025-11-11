from bob import Bob

def execute(bob: Bob):
    # # R TO L
    # bob.foreward(250, 1200)
    # bob.turn(-90, 500)
    # bob.foreward(1500, 1200)
    bob.foreward(200,200)
    bob.turn(-90,150)
    bob.foreward(420,200)
    bob.turn_back_motor(750,200)
    bob.turn_back_motor(-400,60)
    bob.turn_back_motor(-200,100)
    bob.foreward(80,100)
    bob.turn_front_motor(300,100)
    for hit in range(8):
        bob.turn_front_motor(60,100)
        bob.turn_front_motor(-60,100)
    