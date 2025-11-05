from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait
import run1, run2, run3, run4, run5, run6, run7, run8, run9, run10
import new_run4
from bob import Bob

hub = PrimeHub()
bob = Bob()

total_number_of_runs = 10
    
current_index = 1
hub.display.number(current_index)

def run_steps(bob, steps):
    bob.drivebase.reset(distance=0, angle=0)
    bob.attachment_motor.reset_angle(angle=0)
    bob.back_motor.reset_angle(angle=0)

    wait(500)

    for step in steps:
        step.execute(bob=bob)

while True:
    pressed = hub.buttons.pressed()
    
    # Debug: print what buttons are pressed
    if pressed:
        print(f"Buttons pressed: {pressed}")

    # RIGHT button cycles through files
    if Button.RIGHT in pressed:
        print("RIGHT button detected!")
        if current_index > total_number_of_runs:
            current_index = 0
        else:
            current_index += 1
        hub.display.number(current_index)
        print(f"Selected: {current_index}.py")
        wait(300)

    # LEFT button executes the current file
    elif Button.LEFT in pressed:
        if current_index == 1:
            run1.execute(bob=bob)
        elif current_index == 2:
            run2.execute(bob=bob)
        elif current_index == 3:
            run3.execute(bob=bob)
        elif current_index == 4:
            run_steps(bob=bob, steps=new_run4.steps)
        elif current_index == 5:
            run5.execute(bob=bob)
        elif current_index == 6:
            run6.execute(bob=bob)
        elif current_index == 7:
            run7.execute(bob=bob)
        elif current_index == 8:
            run8.execute(bob=bob)
        elif current_index == 9:
            run9.execute(bob=bob)
        elif current_index == 10:
            run10.execute(bob=bob)


    wait(50)
