from bob import Bob

def execute(bob: Bob):

    yield from bob.foreward_and_front_motor(335,200,325,200)

    yield from bob.foreward(-270,300)

    yield from bob.foreward_and_front_motor(100,300,-325,200)

    yield from bob.foreward(-300,200)
