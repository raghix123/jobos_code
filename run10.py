from bob import Bob

def execute(bob: Bob):
    yield from bob.turn_front_motor()