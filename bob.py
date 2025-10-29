from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.tools import StopWatch

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
    
    def _monitor_drivebase_completion(self, check_interval=5, timeout_ms=5000):
        """
        Utility function to monitor drivebase completion and stall status.
        
        Args:
            on_complete: Callback function to call when drivebase completes successfully
            on_stall: Callback function to call when drivebase stalls
            check_interval: How often to check status (milliseconds)
            timeout_ms: Maximum time to wait before giving up (milliseconds)
            
        Returns:
            'completed' if completed successfully
            'stalled' if stalled
            'timeout' if timed out
        """
        # Check if completed
        if self.drivebase.done():
            return
        
        stopwatch = StopWatch()
        while stopwatch.time() < timeout_ms:
            # Check if completed
            if self.drivebase.done():
                return

            # Check if stalled
            if self.drivebase.stalled():
                print("Drivebase stalled detected")
                self.drivebase.stop()  # Default behavior - always stop on stall
                return
        
            wait(check_interval)
        
        # Timeout reached
        print("Drivebase monitoring timed out")

    def foreward(self, distance, speed):
        print("move fwd " + str(distance))
        default_speed = self.drivebase.settings()[0]
        self.drivebase.settings(straight_speed=self.factor*speed)
        self.drivebase.straight(distance, then=Stop.BRAKE, wait=True)
        self.drivebase.settings(straight_speed=default_speed)

    def forward_safe(self, distance, speed):
        """
        Move forward with stall detection and abort capability.
        Uses the same parameters as foreward() but with stall monitoring.
        """
        print("move fwd safe " + str(distance))
        default_speed = self.drivebase.settings()[0]
        self.drivebase.settings(straight_speed=self.factor*speed)
        self.drivebase.straight(distance, then=Stop.BRAKE, wait=False)
        self._monitor_drivebase_completion()
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
        self.drivebase.turn(degree, then=Stop.HOLD, wait=True)
        self.drivebase.settings(default_settings[0], default_settings[1], default_settings[2], default_settings[3])
    
    def turn_safe(self, degree, speed=200, then=Stop.HOLD):
        """
        Turn using drivebase.turn() with stall detection and abort capability.
        Uses the same parameters as turn() but with stall monitoring.
        """
        print("turning safe " + str(degree))
        default_settings = self.drivebase.settings()
        self.drivebase.settings(default_settings[0], default_settings[1], self.factor*speed, default_settings[3])
        self.drivebase.turn(degree, then=then, wait=False)
        self._monitor_drivebase_completion()
        self.drivebase.settings(default_settings[0], default_settings[1], default_settings[2], default_settings[3])

    def turn_front_motor(self, degree, speed, then=Stop.HOLD):
        print("turning front motor " +str(degree))
        self.attachment_motor.run_angle(speed=self.factor*speed, rotation_angle=degree, then=then, wait=True)

    def turn_back_motor(self, degree, speed):
        print("turning front motor " +str(degree))
        self.back_motor.run_angle(speed=self.factor*speed, rotation_angle=degree, then=Stop.BRAKE, wait=True)

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
        
