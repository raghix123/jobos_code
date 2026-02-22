from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

import run1, run2, run3, run4, run5, run6, run7, run8, run9, run10
from bob import Bob

hub = PrimeHub()
bob = Bob(hub)

runs = [run1, run2, run3, run4, run5, run6, run7, run8, run9, run10]

# Run order: Run4, Run10, Run5, Run2, Run1, Run3, Run9 (0-based indices into runs list)
RUN_ORDER = [3, 9, 4, 1, 0, 2, 8]

LOG_INTERVAL_MS = 100
STEP_WAIT_MS = 10


def calibrate_and_wait_until_still(timeout_ms=5000):
    hub.imu.reset_heading(0)
    bob.drivebase.reset()
    hub.display.text(".")
    elapsed = 0
    while not hub.imu.stationary() and elapsed < timeout_ms:
        wait(10)
        elapsed += 10
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


def start(log=False, auto_advance=False):
    # Position in RUN_ORDER (auto_advance) or index into runs (manual)
    order_pos = 0

    if auto_advance:
        current_index = RUN_ORDER[order_pos]
    else:
        current_index = 0

    hub.display.number(current_index + 1)

    while True:
        pressed = hub.buttons.pressed()

        if Button.RIGHT in pressed:
            if auto_advance:
                order_pos = (order_pos + 1) % len(RUN_ORDER)
                current_index = RUN_ORDER[order_pos]
            else:
                current_index = (current_index + 1) % len(runs)
            hub.display.number(current_index + 1)
            wait(300)

        elif Button.LEFT in pressed:
            calibrate_and_wait_until_still()
            gen = runs[current_index].execute(bob)
            run_with_logging(gen, log)
            # After run finishes, advance to next run in order
            if auto_advance:
                order_pos = (order_pos + 1) % len(RUN_ORDER)
                current_index = RUN_ORDER[order_pos]
            hub.display.number(current_index + 1)
            wait(300)

        wait(50)