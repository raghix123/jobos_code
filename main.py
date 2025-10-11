from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait
import run1, run2, run3, run4, run6, run7, run8, run9, run10
from bob import Bob


hub = PrimeHub()
bob = Bob()

total_number_of_runs = 10
    
current_index = 1
hub.display.number(current_index)

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
            run4.execute(bob=bob)
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
        wait(300)

    wait(50)
