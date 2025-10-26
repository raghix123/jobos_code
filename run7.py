from bob import Bob

def execute(bob: Bob):
    # R TO L
    bob.foreward(250, 1200)
    bob.turn(-90, 500)
    bob.foreward(1500, 1200)