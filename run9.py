from bob import Bob

def execute(bob: Bob):
    bob.foreward_and_front_motor(355,200,400,150)

    bob.foreward(-270,300)

    bob.foreward_and_front_motor(125,300,-325,200)

    bob.foreward(-300,200)
