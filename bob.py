from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

class Bob:
    def __init__(self):
        # Hub
        self.hub = PrimeHub()
        self.hub.speaker.volume(100)

        # Motors
        self.left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.F)
        self.attachment_motor = Motor(Port.D)
        self.back_motor = Motor(Port.C)

        # Drive base (wheels on B & F, 89mm wheels, 152mm axle track)
        self.drivebase = DriveBase(
            self.left_motor,
            self.right_motor,
            wheel_diameter=89,
            axle_track=152,
        )
        self.drivebase.use_gyro(True)

        self.factor = 1

    def set_speed_factor(self, factor):
        self.factor = factor

    def foreward(self, distance, speed, then=Stop.BRAKE):
        print("move fwd " + str(distance))
        default_speed = self.drivebase.settings()[0]
        self.drivebase.settings(straight_speed=self.factor*speed)
        self.drivebase.straight(distance, then=then, wait=True)
        self.drivebase.settings(straight_speed=default_speed)

    def reverse(self, distance, speed):
        print("move backward " + str(distance))
        default_speed = self.drivebase.settings()[0]
        self.drivebase.settings(straight_speed=self.factor*speed)
        self.drivebase.straight(-distance, then=Stop.BRAKE, wait=True)
        self.drivebase.settings(straight_speed=default_speed)

    def turn(self, degree, speed=200, then=Stop.HOLD):
        print("turning " + str(degree))
        default_settings = self.drivebase.settings()
        self.drivebase.settings(default_settings[0], default_settings[1], self.factor*speed, default_settings[3])
        self.drivebase.turn(degree, then=then, wait=True)
        self.drivebase.settings(default_settings[0], default_settings[1], default_settings[2], default_settings[3])
    
    def turn_front_motor(self, degree, speed, then=Stop.HOLD):
        print("turning front motor " +str(degree))
        self.attachment_motor.run_angle(speed=self.factor*speed, rotation_angle=degree, then=then, wait=True)

    def turn_front_motor_until_stalled(self, speed, duty_limit=25):
        print("turning front motor till stalled")
        self.attachment_motor.run_until_stalled(speed=self.factor*speed, duty_limit=duty_limit)

    def turn_back_motor(self, degree, speed, then=Stop.BRAKE):
        print("turning front motor " +str(degree))
        self.back_motor.run_angle(speed=self.factor*speed, rotation_angle=degree, then=then, wait=True)

    def turn_back_motor_until_stalled(self, speed, duty_limit=25):
        print("turning back motor till stalled")
        self.back_motor.run_until_stalled(speed=self.factor*speed, duty_limit=duty_limit)

    def foreward_and_front_motor(self, foreward_distance, foreward_speed, motor_degree, motor_speed, turn_then=Stop.HOLD, foreward_then=Stop.BRAKE,):
        print("moving fwd" + str(foreward_distance))
        default_speed = self.drivebase.settings()[0]
        self.drivebase.settings(straight_speed=self.factor*foreward_speed)
        self.drivebase.straight(foreward_distance, then=Stop.BRAKE, wait=False)
        

        print("turning front motor " +str(motor_degree))
        self.attachment_motor.run_angle(speed=self.factor*motor_speed, rotation_angle=motor_degree, then=turn_then, wait=True)


        while not self.drivebase.done():
            wait(0.5)
        
        self.drivebase.settings(straight_speed=default_speed)

    def turn_and_back_motor(self, turn_angle, turn_speed, motor_degree, motor_speed, then=Stop.HOLD):
        print("turning " + str(turn_angle))
        default_settings = self.drivebase.settings()
        self.drivebase.settings(default_settings[0], default_settings[1], self.factor*turn_speed, default_settings[3])
        self.drivebase.turn(turn_angle, then=then, wait=False)
    

        print("turning front motor " +str(motor_degree))
        self.back_motor.run_angle(speed=self.factor*motor_speed, rotation_angle=motor_degree, then=then, wait=True)
        
        while not self.drivebase.done():
            wait(0.5)
        
        self.drivebase.settings(default_settings[0], default_settings[1], default_settings[2], default_settings[3])

            
    # def drive(self, speed, turn_rate):
    #     """Drive at specified speed and turn rate"""
    #     print(f"driving at speed {speed}, turn rate {turn_rate}")
    #     self.drivebase.drive(self.factor*speed, turn_rate)
    
    # def stop(self):
    #     """Stop the drivebase"""
    #     print("stopping")
    #     self.drivebase.stop()
    
    # def attachment_run_angle(self, speed, angle):
    #     """Run attachment motor at specified speed for specified angle"""
    #     print(f"attachment motor running at speed {speed} for angle {angle}")
    #     self.attachment_motor.run_angle(self.factor*speed, angle)
        
