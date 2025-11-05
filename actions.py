from pybricks.parameters import Stop
from pybricks.tools import wait

class Action:
    def execute(self, bob, wait=True):
        raise NotImplementedError

    def completed(self, bob):
        raise NotImplementedError


# Operation classes for run modules to use
class ForewardAction(Action):
    def __init__(self, distance, speed, then=Stop.BRAKE):
        self.distance = distance
        self.speed = speed
        self.then = then

    def execute(self, bob, wait=True):
        print(f"ForewardAction: distance={self.distance}, speed={self.speed}, then={self.then}")
        default_speed = bob.drivebase.settings()[0]
        bob.drivebase.settings(straight_speed=bob.factor * self.speed)
        bob.drivebase.straight(self.distance, then=self.then, wait=wait)
        if wait:
            # restore immediately
            bob.drivebase.settings(straight_speed=default_speed)
            self._restore = None
        else:
            # remember to restore when completed
            self._restore = ("straight_speed", default_speed)

    def completed(self, bob):
        done = bob.drivebase.done()
        if done and getattr(self, "_restore", None):
            # Restore straight speed once
            _, default_speed = self._restore
            bob.drivebase.settings(straight_speed=default_speed)
            self._restore = None
        return done


class TurnAction(Action):
    def __init__(self, degree, speed=200, then=Stop.HOLD):
        self.degree = degree
        self.speed = speed
        self.then = then

    def execute(self, bob, wait=True):
        print(f"TurnAction: degree={self.degree}, speed={self.speed}, then={self.then}")
        default_settings = bob.drivebase.settings()
        bob.drivebase.settings(
            default_settings[0], default_settings[1], bob.factor * self.speed, default_settings[3]
        )
        bob.drivebase.turn(self.degree, then=self.then, wait=wait)
        if wait:
            bob.drivebase.settings(
                default_settings[0], default_settings[1], default_settings[2], default_settings[3]
            )
            self._restore = None
        else:
            self._restore = ("turn", default_settings)

    def completed(self, bob):
        done = bob.drivebase.done()
        if done and getattr(self, "_restore", None):
            _, default_settings = self._restore
            bob.drivebase.settings(
                default_settings[0], default_settings[1], default_settings[2], default_settings[3]
            )
            self._restore = None
        return done


class MotorKind:
    FRONT = "front"
    BACK = "back"


class MotorMode:
    ANGLE = "angle"
    DC = "dc"
    RUN_TARGET = "run_target"


class MotorAction(Action):
    def __init__(self, motor: MotorKind, mode: MotorMode = MotorMode.ANGLE, degree=None, speed=None, then=Stop.BRAKE, dc=None, time=None, target_angle=None):
        # motor: MotorKind
        # mode: MotorMode
        self.motor = motor
        self.mode = mode
        self.degree = degree
        self.speed = speed
        self.then = then
        self.dc = dc
        self.time = time
        self.target_angle = target_angle

    def _get_motor(self, bob):
        if self.motor == MotorKind.FRONT:
            return bob.attachment_motor
        if self.motor == MotorKind.BACK:
            return bob.back_motor
        raise ValueError("Unknown motor: {}".format(self.motor))

    def execute(self, bob, wait=True):
        m = self._get_motor(bob)
        if self.mode == MotorMode.ANGLE:
            print(f"MotorAction: kind={self.motor}, angle={self.degree}, speed={self.speed}, then={self.then}")
            m.run_angle(speed=bob.factor * self.speed, rotation_angle=self.degree, then=self.then, wait=wait)
        elif self.mode == MotorMode.DC:
            print(f"MotorAction: kind={self.motor}, dc={self.dc}, time={self.time}")
            # Always time-blocking regardless of wait flag
            m.dc(self.dc)
            wait(self.time)
            m.stop()
        elif self.mode == MotorMode.RUN_TARGET:
            print(f"MotorAction: kind={self.motor}, target_angle={self.target_angle}, speed={self.speed}, then={self.then}")
            # Back motor target positioning
            m.run_target(speed=self.speed, target_angle=self.target_angle, then=self.then)
        else:
            raise ValueError("Unknown mode: {}".format(self.mode))

    def completed(self, bob):
        if self.mode in (MotorMode.ANGLE, MotorMode.RUN_TARGET):
            try:
                return self._get_motor(bob).done()
            except Exception:
                return True
        if self.mode == MotorMode.DC:
            return True
        return True

class TogetherAction(Action):
    def __init__(self, first: Action, second: Action):
        self.first = first
        self.second = second

    def execute(self, bob, wait=True):
        # Run first non-blocking, second blocking, then wait on first completion
        self.first.execute(bob, wait=False)
        self.second.execute(bob, wait=True)
        while not self.first.completed(bob):
            wait(500)

    def completed(self, bob):
        print("blah")
        return self.first.completed(bob) and self.second.completed(bob)


class WaitAction(Action):
    def __init__(self, ms):
        self.ms = ms

    def execute(self, bob, wait=True):
        # Always a blocking delay
        wait(self.ms)


class RepeatAction(Action):
    def __init__(self, times, steps):
        self.times = times
        self.steps = steps

    def execute(self, bob, wait=True):
        for _ in range(self.times):
            for sub in self.steps:
                sub.execute(bob, wait=True)

    def completed(self, bob):
        return True