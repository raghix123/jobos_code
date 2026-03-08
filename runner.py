from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

import run1, run2, run3, run4, run5, run6, run7, run8, run9, run10
from bob import Bob

hub = PrimeHub()
bob = Bob(hub)

runs = [run1, run2, run3, run4, run5, run6, run7, run8, run9, run10]

# Run order: Run4, Run10, Run5, Run2, Run1, Run9 (0-based indices into runs list)
RUN_ORDER = [3, 9, 4, 1, 0, 8]

LOG_INTERVAL_MS = 100
STEP_WAIT_MS = 10


def side_button_pressed():
    pressed = hub.buttons.pressed()
    return Button.LEFT in pressed or Button.RIGHT in pressed


def wait_for_side_buttons_release():
    while side_button_pressed():
        wait(10)


def run_with_logging(gen, should_log=False):
    elapsed = 0
    last_log = -LOG_INTERVAL_MS
    abort_armed = False

    # Header once per run
    print(bob.log_header())

    while True:
        if not abort_armed:
            # Ignore the start-button hold; arm abort only after both side buttons are released.
            if not side_button_pressed():
                abort_armed = True
        elif side_button_pressed():
            bob.drivebase.stop()
            bob.left_motor.stop()
            bob.right_motor.stop()
            bob.attachment_motor.stop()
            bob.back_motor.stop()
            return

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
    bob.drivebase.use_gyro(False)

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
            bob.drivebase.use_gyro(True)
            run_module = runs[current_index]
            bob.calibrate(run_module.calibrate_ms())
            gen = run_module.execute(bob)
            run_with_logging(gen, log)
            bob.drivebase.use_gyro(False)
            wait_for_side_buttons_release()
            # After run finishes, advance to next run in order
            if auto_advance:
                order_pos = (order_pos + 1) % len(RUN_ORDER)
                current_index = RUN_ORDER[order_pos]
            hub.display.number(current_index + 1)
            wait(300)

        wait(50)
