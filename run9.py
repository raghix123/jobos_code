from pybricks.tools import wait
from bob import Bob


def execute(bob: Bob):
    # Tip the Scale B: long forward + front motor, slightly slower for stability
    yield from bob.foreward_and_front_motor(270, 180, 350, 150)

    # Short settle so chassis and IMU calm down
    wait(150)

    # Small nudge forward
    yield from bob.foreward(30, 100)

    # Keep this wait – it was already helping consistency
    wait(2000)

    # Reverse toward the roof – slower to reduce slip
    yield from bob.foreward(-275, 250)

    # Let chassis stop rocking before the roof front-motor move
    wait(100)

    # Roof action – front motor only
    yield from bob.turn_front_motor(-50, 100)

    # Brief settle after the front-motor torque
    wait(100)

    # # Continue reversing – slightly slower to keep wheels from breaking traction
    # yield from bob.foreward(-300, 180)

    # Combined reverse + front-motor for roof finish, with reduced speed and settle
    wait(100)
    yield from bob.foreward_and_front_motor(-80, 180, 350, 150)

    # Final run back to base – distance was already very repeatable
    yield from bob.foreward(320, 300)
    