from bob import Bob

def execute(bob: Bob):

    bob.foreward_and_front_motor(335,200,325,200)

    bob.foreward(-270,300)

    bob.foreward_and_front_motor(100,300,-325,200)

    bob.foreward(-300,200)
