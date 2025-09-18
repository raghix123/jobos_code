from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait
import run1, run2, run3, run4, run5, run6, run7, run8, run9, run10
from bob import Bob


hub = PrimeHub()
bob = Bob()

total_number_of_runs = 3
    
number = 1
hub.display.number(number)

while True:
    pressed = hub.buttons.pressed()
    
    # Debug: print what buttons are pressed
    if pressed:
        print(f"Buttons pressed: {pressed}")

    # RIGHT button cycles through files
    if Button.RIGHT in pressed:
        print("RIGHT button detected!")
        current_index += 1
        if current_index > total_number_of_runs:
            current_index = 0
        hub.display.number(current_index + 1)
        print(f"Selected: {current_index}.py")
        wait(300)

    # LEFT button executes the current file
    elif Button.LEFT in pressed:
        if number == 1:
            run1.execute(bob=bob)
        elif number == 2:
            run2.execute(bob=bob)
        elif number == 3:
            run3.execute(bob=Bob)
        elif number == 4:
            run4.execute(bob=Bob)
        elif number == 5:
            run5.execute(bob=Bob)
        elif number == 6:
            run5.execute(bob=Bob)
        elif number == 7:
            run5.execute(bob=Bob) 
        elif number == 8:
            run5.execute(bob=Bob) 
        elif number == 9:
            run5.execute(bob=Bob) 
        elif number == 10:
            run5.execute(bob=Bob)     
        wait(300)

    wait(50)
