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

    def foreward(self, distance, speed):
        print("move fwd " + str(distance))
        default_speed = self.drivebase.settings()[0]
        self.drivebase.settings(straight_speed=speed)
        self.drivebase.straight(distance, then=Stop.BRAKE, wait=True)
        self.drivebase.settings(straight_speed=default_speed)

    def reverse(self, distance, speed):
        print("move backward " + str(distance))
        default_speed = self.drivebase.settings()[0]
        self.drivebase.settings(straight_speed=speed)
        self.drivebase.straight(-distance, then=Stop.BRAKE, wait=True)
        self.drivebase.settings(straight_speed=default_speed)

    def turn(self, degree, speed=200):
        print("turning " + str(degree))
        default_settings = self.drivebase.settings()
        self.drivebase.settings(default_settings[0], default_settings[1], speed, default_settings[3])
        self.drivebase.turn(degree, then=Stop.HOLD, wait=True)
        self.drivebase.settings(default_settings[0], default_settings[1], default_settings[2], default_settings[3])
    
    def turn_front_motor(self, degree, speed):
        print("turning front motor " +str(degree))
        self.attachment_motor.run_angle(speed=speed, rotation_angle=degree, then=Stop.BRAKE, wait=True)

    def turn_back_motor(self, degree, speed):
        print("turning front motor " +str(degree))
        self.back_motor.run_angle(speed=speed, rotation_angle=degree, then=Stop.BRAKE, wait=True)

    def drive(self, speed, turn_rate):
        """Drive at specified speed and turn rate"""
        print(f"driving at speed {speed}, turn rate {turn_rate}")
        self.drivebase.drive(speed, turn_rate)
    
    def stop(self):
        """Stop the drivebase"""
        print("stopping")
        self.drivebase.stop()
    
    def attachment_run_angle(self, speed, angle):
        """Run attachment motor at specified speed for specified angle"""
        print(f"attachment motor running at speed {speed} for angle {angle}")
        self.attachment_motor.run_angle(speed, angle)
    
    # def execute(self, filename):
    #     """
    #     Play a noise and then execute a specific robot program.
        
        def drive(self, speed, turn_rate):
            """Drive at specified speed and turn rate"""
            print(f"driving at speed {speed}, turn rate {turn_rate}")
            self.drivebase.drive(speed, turn_rate)
        
        def stop(self):
            """Stop the drivebase"""
            print("stopping")
            self.drivebase.stop()
        
        def attachment_run_angle(self, speed, angle):
            """Run attachment motor at specified speed for specified angle"""
            print(f"attachment motor running at speed {speed} for angle {angle}")
            self.attachment_motor.run_angle(speed, angle)
        
        # def execute(self, filename):
        #     """
        #     Play a noise and then execute a specific robot program.
            
        #     Args:
        #         filename: Name of the robot program to execute
        #     """
        #     print(f"Starting execution of {filename}...")
            
        #     # Play a startup sound
        #     print("Playing startup sound...")
        #     self.hub.speaker.beep(523, 200)  # C5
        #     self.hub.speaker.beep(659, 200)  # E5
        #     self.hub.speaker.beep(784, 200)  # G5
        #     self.hub.speaker.beep(1047, 200) # C6
            
        #     try:
        #         # Execute specific robot programs
        #         if filename == "mission2akewl":
        #             self.run_mission2akewl()
        #         else:
        #             print(f"Unknown program: {filename}")
        #             return
                    
        #     except Exception as e:
        #         print(f"Error executing {filename}: {e}")
            
        #     # Play completion sound
        #     print("Playing completion sound...")
        #     self.hub.speaker.beep(784, 200)  # G5
        #     self.hub.speaker.beep(659, 200)  # E5
        #     self.hub.speaker.beep(523, 200)  # C5
        
        # def run_mission2akewl(self):
        #     """Run the mission2akewl robot program"""
        #     print("Running mission2akewl program...")
            
        #     # Move attachment motor up
        #     self.attachment_run_angle(100, 250)
            
        #     # Drive forward
        #     self.drive(300, 0)
        #     wait(2600)
        #     self.stop()
            
        #     # Turn left
        #     self.turn(-20)
            
        #     # Move attachment motor down slightly
        #     self.attachment_run_angle(100, -75)
            
        #     # Drive forward a bit
        #     self.drive(150, 0)
        #     wait(500)
        #     self.stop()
            
        #     # Move attachment motor down more
        #     self.attachment_run_angle(100, -150)
            
        #     # Drive backward
        #     self.drive(-200, 0)
        #     wait(500)
        #     self.stop()
            
        #     # Turn right
        #     self.turn(30)
            
        #     # Drive backward
        #     self.drive(-300, 0)
        #     wait(2600)
        #     self.stop()
            
        #     print("Mission2akewl program completed!")
        
