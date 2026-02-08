import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop, Color, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import run1, run2, run3, run4, run5, run6, run7, run8, run9, run10
from bob import Bob

# Initializing hub
hub = PrimeHub()
color_sensor = ColorSensor(Port.E)
x = True
bob = Bob(hub)   
total_number_of_runs = 10
current_index = 1
last_pressed = set()
ref = color_sensor.reflection()


#Colors
while x:
    detected_color = color_sensor.color()
    pressed = set(hub.buttons.pressed())

    if detected_color == Color.RED:
        hub.display.number(current_index)

        # RIGHT = increment menu
        if Button.RIGHT in pressed and Button.RIGHT not in last_pressed:
            current_index += 1
            if current_index > total_number_of_runs:
                current_index = 1

        # LEFT = run
        elif Button.LEFT in pressed and Button.LEFT not in last_pressed:
                run1.execute(bob=bob)
                wait(500)

    elif detected_color == Color.BLUE:
        hub.display.number(2)
        print("insert fixture")

    elif detected_color == Color.YELLOW:
        hub.display.number(3)
        if Button.LEFT in pressed and Button.LEFT not in last_pressed:
            run3.execute(bob=bob)

    elif detected_color == Color.GREEN:
        hub.display.number(4)
        if Button.LEFT in pressed and Button.LEFT not in last_pressed:
            run4.execute(bob=bob)

    elif detected_color == Color.WHITE:
        hub.display.number(5)
        if Button.LEFT in pressed and Button.LEFT not in last_pressed:
            run5.execute(bob=bob)

    elif ref < 5:
        #black
        hub.display.number(6)
        if Button.LEFT in pressed and Button.LEFT not in last_pressed:
            run6.execute(bob=bob)

    elif detected_color == Color.CYAN:
        hub.display.number(7)
        if Button.LEFT in pressed and Button.LEFT not in last_pressed:
            run7.execute(bob=bob)

    elif detected_color == Color.ORANGE:
        hub.display.number(8)
        if Button.LEFT in pressed and Button.LEFT not in last_pressed:
            run8.execute(bob=bob)

    elif detected_color == Color.MAGENTA:
        hub.display.number(9)
        if Button.LEFT in pressed and Button.LEFT not in last_pressed:
            run9.execute(bob=bob)


    # 👇 THIS MUST ALWAYS RUN
    last_pressed = pressed
    wait(100)