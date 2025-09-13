from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
import importlib

class Bob:
    def __init__(self):
        # Hub
        self.hub = PrimeHub()
        self.hub.speaker.volume(100)

        # Motors
        self.left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.F)
        self.attachment_motor = Motor(Port.D)

        # Sensors
        self.color_sensor = ColorSensor(Port.B)

        # Drive base (wheels on C & D, 56mm wheels, 143mm axle track)
        self.drivebase = DriveBase(
            self.left_motor,
            self.right_motor,
            wheel_diameter=56,
            axle_track=143,
        )

    def forward(self, distance):
        print("move fwd " + str(distance))
        self.drivebase.straight(distance, then=Stop.HOLD, wait=True)

    def reverse(self, distance):
        print("move backward " + str(distance))
        self.drivebase.straight(distance, then=Stop.HOLD, wait=True)

    def turn(self, degree):
        print("turning " + str(degree))
        self.drivebase.turn(degree, then=Stop.HOLD, wait=True)
    
