from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

class Bob:
    def __init__(self, hub):
        self.hub = hub

        # --- MOTORS (adjust ports if needed) ---
        self.left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.F)
        self.attachment_motor = Motor(Port.D)
        self.back_motor = Motor(Port.C)

        # --- DRIVEBASE (use your real values if different) ---
        self.drivebase = DriveBase(
            self.left_motor,
            self.right_motor,
            wheel_diameter=87.0,
            axle_track=114.3,
        )
        # Gentler correction to reduce snaking (lower turn_rate = less overshoot)
        self.drivebase.settings(
            straight_speed=250,
            straight_acceleration=400,
            turn_rate=100,
            turn_acceleration=300,
        )

   # ---------------- PRIMITIVES ----------------

    def foreward(self, distance, speed, then=Stop.BRAKE):
        default = self.drivebase.settings()
        self.drivebase.settings(straight_speed=speed)
        self.drivebase.straight(distance, then=then, wait=False)
        while not self.drivebase.done():
            yield
        self.drivebase.settings(*default)

    def turn(self, degree, speed=200, then=Stop.BRAKE):
        default = self.drivebase.settings()
        self.drivebase.settings(default[0], default[1], speed, default[3])
        self.drivebase.turn(degree, then=then, wait=False)
        while not self.drivebase.done():
            yield
        self.drivebase.settings(*default)

    def turn_to(self, target_heading, speed=200, then=Stop.BRAKE):
        """Turn to an absolute heading. Assumes calibration (0 at start) has been run."""
        current = self.hub.imu.heading()
        diff = target_heading - current
        while diff > 180:
            diff -= 360
        while diff < -180:
            diff += 360
        if abs(diff) > 0:
            yield from self.turn(diff, speed, then)

    def arc(self, radius, angle, speed):
        default = self.drivebase.settings()
        self.drivebase.settings(straight_speed=speed)
        self.drivebase.curve(radius, angle, wait=False)
        while not self.drivebase.done():
            yield
        self.drivebase.settings(*default)

    def wait(self, ms):
        elapsed = 0
        while elapsed < ms:
            yield
            wait(10)
            elapsed += 10

    # ---------------- MOTOR HELPERS ----------------

    def reset_back_motor_angle(self, angle=0):
        self.back_motor.reset_angle(angle)
        yield

    def reset_attachment_motor_angle(self, angle=0):
        self.attachment_motor.reset_angle(angle)
        yield

    def turn_front_motor_dc(self, dc, time):
        self.attachment_motor.dc(dc)
        elapsed = 0
        while elapsed < time:
            yield
            wait(10)
            elapsed += 10
        self.attachment_motor.stop()

    def turn_front_motor(self, degree, speed, then=Stop.HOLD):
        self.attachment_motor.run_angle(
            speed=speed, rotation_angle=degree, then=then, wait=False
        )
        while not self.attachment_motor.done():
            yield

    def back_motor_run_target(self, speed, target_angle, then=Stop.BRAKE):
        self.back_motor.run_target(
            speed=speed, target_angle=target_angle, then=then, wait=False
        )
        while not self.back_motor.done():
            yield

    def attachment_motor_run_target(self, speed, target_angle, then=Stop.BRAKE):
        self.attachment_motor.run_target(
            speed=speed, target_angle=target_angle, then=then, wait=False
        )
        while not self.attachment_motor.done():
            yield

    def turn_back_motor_dc(self, dc, time):
        self.back_motor.dc(dc)
        elapsed = 0
        while elapsed < time:
            yield
            wait(10)
            elapsed += 10
        self.back_motor.stop()

    def turn_back_motor(self, degree, speed):
        self.back_motor.run_angle(speed=speed, rotation_angle=degree, then=Stop.BRAKE)
        while not self.back_motor.done():
            yield

    def run_front_motor_until_stalled(self, speed, then=Stop.HOLD, duty_limit=100):
        # run_until_stalled is blocking - no wait=False option
        self.attachment_motor.run_until_stalled(
            speed=speed, then=then, duty_limit=duty_limit
        )
        yield

    def run_back_motor_until_stalled(self, speed, then=Stop.BRAKE, duty_limit=100):
        # run_until_stalled is blocking - no wait=False option
        self.back_motor.run_until_stalled(
            speed=speed, then=then, duty_limit=duty_limit
        )
        yield

    # ---------------- COMPOSITES ----------------

    def foreward_and_front_motor(
        self, foreward_distance, foreward_speed, turn_degree, turn_speed, then=Stop.BRAKE
    ):
        default = self.drivebase.settings()
        self.drivebase.settings(straight_speed=foreward_speed)

        self.drivebase.straight(foreward_distance, then=then, wait=False)
        self.attachment_motor.run_angle(
            speed=turn_speed, rotation_angle=turn_degree, wait=False
        )

        while not (
            self.drivebase.done()
            and self.attachment_motor.done()
        ):
            yield

        self.drivebase.settings(*default)

    def log_header(self):
        return (
            "t_ms,"
            "heading,"
            "distance,"
            "left_angle,"
            "right_angle,"
            "front_angle,"
            "rear_angle"
        )

    def log_row(self, t_ms):
        return ",".join([
            str(t_ms),
            str(self.hub.imu.heading()),
            str(self.drivebase.distance()),
            str(self.left_motor.angle()),
            str(self.right_motor.angle()),
            str(self.attachment_motor.angle()),
            str(self.back_motor.angle()),
        ])