from bob import Bob
from pybricks.tools import wait

# Create Bob instance
bob = Bob()

bob.attachment_run_angle(100, 250)

bob.drive(300, 0)
wait(2600)
bob.stop()

bob.turn(-20)

bob.attachment_run_angle(100, -75)

bob.drive(150, 0)
wait(500)
bob.stop()

bob.attachment_run_angle(100, -150)

bob.drive(-200, 0)
wait(500)
bob.stop()

bob.turn(30)

bob.drive(-300, 0)
wait(2600)
bob.stop()

