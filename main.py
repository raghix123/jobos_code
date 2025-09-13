from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait
from bob import Bob

hub = PrimeHub()
bob = Bob()

# List of files to cycle through (excluding test.py, main.py, and bob.py)
files = ["mission2akewl"]
current_index = 0
current_file = files[current_index]

# Display current file number
hub.display.number(current_index + 1)

print("File selector ready!")
print("RIGHT button: Next file")
print("LEFT button: Execute current file")
print(f"Current file: {current_file}.py")

while True:
    pressed = hub.buttons.pressed()
    
    # Debug: print what buttons are pressed
    if pressed:
        print(f"Buttons pressed: {pressed}")

    # RIGHT button cycles through files
    if Button.RIGHT in pressed:
        print("RIGHT button detected!")
        current_index += 1
        if current_index >= len(files):
            current_index = 0
        current_file = files[current_index]
        hub.display.number(current_index + 1)
        print(f"Selected: {current_file}.py")
        wait(300)

    # LEFT button executes the current file
    elif Button.LEFT in pressed:
        print("LEFT button detected!")
        print(f"Executing {current_file}.py...")
        bob.execute(current_file)
        wait(300)

    wait(50)
