from bob import Bob

def execute(bob: Bob):
    bob.attachment_motor.run_angle(300,300)

    bob.foreward(distance=415, speed=300)

    bob.turn(42)

    bob.foreward(distance=365, speed=200)

    bob.turn(-20)

    bob.attachment_motor.run_angle(-300,300)