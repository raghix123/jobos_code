from pybricks.tools import wait  # type: ignore
from bob import Bob

# Initialize Bob (which includes the color sensor on port E)
bob = Bob()

# Continuously read and display color sensor output every 100ms
print("Starting color sensor readings (every 100ms)...")
while True:
    try:
        # Read the color
        color = bob.color_sensor.color()
        
        # Print to terminal with clear formatting
        print(color)
        
    except Exception as e:
        print(f"Error reading sensor: {e}")
    
    # Wait 100ms before next reading
    wait(100)