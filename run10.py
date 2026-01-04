from bob import Bob

def execute(bob: Bob):
    yield from bob.foreward(distance=400, speed=200)