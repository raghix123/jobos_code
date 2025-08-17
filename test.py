import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize hub
hub = PrimeHub()

# Drive motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)

# Attachment motor (with small fixture + gears)
attachment_motor = Motor(Port.C)

# Set up drivebase
drivebase = DriveBase(left_motor, right_motor, wheel_diameter=89, axle_track=152)

# Drive forward fast

attachment_motor.run_angle(300, 40)

drivebase.drive(350, 0)
wait(2250)
drivebase.stop()

drivebase.turn(20)

drivebase.drive(100, 0)
wait(500)
drivebase.stop()

attachment_motor.run_angle(350, 100)

drivebase.turn(-20)

drivebase.drive(-300, 0)
wait(2750)
drivebase.stop()