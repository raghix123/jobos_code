import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):

    #bob.foreward(745,1000)
    bob.foreward(745,500)

    bob.turn(-25,60)

    #bob.foreward(25,100)
    bob.foreward(20,100)

    bob.turn_front_motor(-300, 300)

    bob.reverse(25,1000)

    bob.turn(-25,100)

    bob.reverse(100,1000)

    bob.turn(-75,100)

    bob.reverse(125,1000)

    bob.turn(78,100)

    bob.reverse(100,1000)

    bob.turn_back_motor(450,500)

    bob.reverse(120,300)
    
    bob.turn_back_motor(150,-100)

    bob.turn(-30)

    bob.turn(40)

    bob.foreward(250,1000)

    bob.turn(80)

    bob.reverse(700,1000)

    # bob.reverse(700,400)

    

# Initialize hub
# hub = PrimeHub()

# # Drive motors
# left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
# right_motor = Motor(Port.F)

# # Attachment motor (with small fixture + gears)
# attachment_motor = Motor(Port.D)

# # Set up drivebase
# drivebase = DriveBase(left_motor, right_motor, wheel_diameter=89, axle_track=152)

# attachment_motor.run_angle(100,250)

# drivebase.drive(300,0)
# wait(2600)
# drivebase.stop()

# drivebase.turn(-20)

# attachment_motor.run_angle(100,-75)

# drivebase.drive(150,0)
# wait(500)
# drivebase.stop()

# attachment_motor.run_angle(100,-150)

# drivebase.drive(-200,0)
# wait(500)
# drivebase.stop()

# drivebase.turn(30)

# drivebase.drive(-300,0)
# wait(2600)
# drivebase.stop()

