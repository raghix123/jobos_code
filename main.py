from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait
import run1, run2, run3, run4, run5, run6, run7, run8, run9, run10
from bob import Bob


hub = PrimeHub()
bob = Bob()

total_number_of_runs = 10
    
current_index = 1
hub.display.number(current_index)

def calibrate_and_wait_until_still():
    # 1. Reset immediately when the user presses the button
    hub.imu.reset_heading(angle=0)
    bob.drivebase.reset()

    # 2. Visually indicate we are waiting for stillness
    hub.display.text("...") 
    
    # 3. Wait in a loop UNTIL the sensor reports it is stationary
    # This might take 0.2s or 1.5s depending on how fast you move your hand.
    while not hub.imu.stationary():
        wait(10) 

    # 4. We are now still. Proceed with the run.
    hub.speaker.beep(frequency=1000, duration=100)
    wait(100) # Short final confirmation delay

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
        calibrate_and_wait_until_still()
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
