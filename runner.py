from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

import run1, run2, run3, run4, run5, run6, run7, run8, run9, run10
from bob import Bob

hub = PrimeHub()
bob = Bob(hub)

runs = [run1, run2, run3, run4, run5, run6, run7, run8, run9, run10]

LOG_INTERVAL_MS = 100
STEP_WAIT_MS = 10


def calibrate_and_wait_until_still():
    hub.imu.reset_heading(0)
    bob.drivebase.reset()
    hub.display.text(".")
    while not hub.imu.stationary():
        wait(10)
    hub.speaker.beep(1000, 100)


def run_with_logging(gen, should_log=False):
    elapsed = 0
    last_log = -LOG_INTERVAL_MS

    # Header once per run
    print(bob.log_header())

    while True:
        try:
            next(gen)
        except StopIteration:
            return

        if should_log and elapsed - last_log >= LOG_INTERVAL_MS:
            print(bob.log_row(elapsed))
            last_log = elapsed

        wait(STEP_WAIT_MS)
        elapsed += STEP_WAIT_MS


def start(log=False): 
    current_index = 0
    hub.display.number(current_index + 1)

    while True:
        pressed = hub.buttons.pressed()

        if Button.RIGHT in pressed:
            current_index = (current_index + 1) % len(runs)
            hub.display.number(current_index + 1)
            wait(300)

        elif Button.LEFT in pressed:
            calibrate_and_wait_until_still()
            gen = runs[current_index].execute(bob)  # run is now a generator function
            run_with_logging(gen, log)
            hub.display.number(current_index + 1)
            wait(300)

        wait(50)