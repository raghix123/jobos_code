from bob import Bob

def execute(bob: Bob):
    yield from bob.foreward_and_front_motor(355,200,400,150)

    yield from bob.foreward(-270,300)

    yield from bob.foreward_and_front_motor(125,300,-325,200)

    yield from bob.foreward(-300,200)
