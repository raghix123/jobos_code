#!/usr/bin/env python3
"""
Test Runner - Runs a specific FLL robot run with logging and saves output.

Usage:
    python testrun.py <run_number>           # Run and save to testlogs/testrun_<N>_<epoch>.txt
    python testrun.py <run_number> --clear   # Clear old sessions for this run first
    
Example:
    python testrun.py 3           # Creates testlogs/testrun_3_1737734400.txt
    python testrun.py 3 --clear   # Deletes old testrun_3_*.txt files first
"""

import sys
import os
import time
import subprocess
from pathlib import Path

# Directory to store test logs
LOG_DIR = Path(__file__).parent / "testlogs"


def create_temp_runner(run_number: int) -> str:
    """Create a temporary main file that runs a specific run with logging."""
    content = f'''from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait

import run{run_number}
from bob import Bob

hub = PrimeHub()
bob = Bob(hub)

LOG_INTERVAL_MS = 100
STEP_WAIT_MS = 10


def calibrate_and_wait_until_still():
    hub.imu.reset_heading(0)
    bob.drivebase.reset()
    hub.display.text("?")  # Show waiting indicator
    hub.light.on(Color.YELLOW)
    
    # Wait for IMU to be stationary, with timeout
    timeout = 5000  # 5 seconds max
    elapsed = 0
    while not hub.imu.stationary() and elapsed < timeout:
        wait(10)
        elapsed += 10
    
    hub.light.on(Color.ORANGE)
    hub.speaker.beep(1000, 100)


def run_with_logging(gen):
    elapsed = 0
    last_log = -LOG_INTERVAL_MS

    print("=== RUN {run_number} START ===")
    print(bob.log_header())

    while True:
        try:
            next(gen)
        except StopIteration:
            # Final log at end
            print(bob.log_row(elapsed))
            break

        if elapsed - last_log >= LOG_INTERVAL_MS:
            print(bob.log_row(elapsed))
            last_log = elapsed

        wait(STEP_WAIT_MS)
        elapsed += STEP_WAIT_MS

    print("=== RUN {run_number} END ===")


# Auto-select run {run_number}, loop for multiple trials
trial_count = 0

def wait_for_no_buttons():
    while hub.buttons.pressed():
        wait(50)

def show_ready():
    hub.display.number({run_number})
    hub.light.on(Color.GREEN)

show_ready()
print("Run {run_number} ready. Press LEFT to start a trial, CENTER to exit.")

while True:
    pressed = hub.buttons.pressed()
    
    if Button.LEFT in pressed:
        hub.light.on(Color.ORANGE)
        trial_count += 1
        print(f"\\n--- TRIAL {{trial_count}} ---")
        calibrate_and_wait_until_still()
        gen = run{run_number}.execute(bob)
        run_with_logging(gen)
        hub.speaker.beep(800, 200)
        print(f"Trial {{trial_count}} complete. Press LEFT for another trial, CENTER to exit.")
        
        # Wait for button release before accepting new input
        wait_for_no_buttons()
        wait(300)  # Extra debounce delay
        show_ready()
    
    elif Button.CENTER in pressed:
        break
    
    wait(50)

hub.light.off()
print(f"\\nSession complete! Ran {{trial_count}} trial(s) of run {run_number}.")
'''
    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python testrun.py <run_number> [--clear]")
        print("Example: python testrun.py 3")
        print("         python testrun.py 3 --clear  # Clear previous trials first")
        sys.exit(1)
    
    try:
        run_number = int(sys.argv[1])
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid run number")
        sys.exit(1)
    
    clear_first = "--clear" in sys.argv
    
    if run_number < 1 or run_number > 10:
        print(f"Error: Run number must be between 1 and 10, got {run_number}")
        sys.exit(1)
    
    # Check that the run file exists
    run_file = Path(__file__).parent / f"run{run_number}.py"
    if not run_file.exists():
        print(f"Error: {run_file} does not exist")
        sys.exit(1)
    
    # Create log directory if it doesn't exist
    LOG_DIR.mkdir(exist_ok=True)
    
    # Create temp runner file
    temp_runner = Path(__file__).parent / "_temp_testrun.py"
    temp_runner.write_text(create_temp_runner(run_number))
    
    # Each session gets a unique file with epoch time
    # Multiple trials within the session append to the same file
    epoch_time = int(time.time())
    output_file = LOG_DIR / f"testrun_{run_number}_{epoch_time}.txt"
    
    # Clear old files for this run number if requested
    if clear_first:
        for old_file in LOG_DIR.glob(f"testrun_{run_number}_*.txt"):
            old_file.unlink()
            print(f"Cleared {old_file.name}")
    
    print(f"Running run{run_number}.py with logging...")
    print(f"Output will be saved to: {output_file}")
    print("-" * 50)
    
    output_lines = []
    
    try:
        # Run pybricksdev and capture output
        # Using subprocess to capture both stdout and display in real-time
        process = subprocess.Popen(
            ["pybricksdev", "run", "ble", str(temp_runner)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            cwd=Path(__file__).parent
        )
        
        for line in process.stdout:
            print(line, end='')  # Print in real-time
            output_lines.append(line)
        
        process.wait()
        
    except FileNotFoundError:
        print("Error: pybricksdev not found. Make sure it's installed and in your PATH.")
        print("Try: pip install pybricksdev")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nSession ended by user (Ctrl+C)")
        process.terminate()
    finally:
        # Clean up temp file
        if temp_runner.exists():
            temp_runner.unlink()
        
        # Always save the output file if we have any data
        if output_lines:
            print("-" * 50)
            print("\nSession complete! Add your observations about this run.")
            print("(What worked? What didn't? Any issues you noticed?)")
            print("Press Enter twice when done, or just Enter to skip.\n")
            
            # Collect user notes
            user_notes = []
            try:
                while True:
                    line = input("> ")
                    if line == "" and (len(user_notes) == 0 or user_notes[-1] == ""):
                        break
                    user_notes.append(line)
            except (KeyboardInterrupt, EOFError):
                pass
            
            # Remove trailing empty lines
            while user_notes and user_notes[-1] == "":
                user_notes.pop()
            
            # Save to file
            with open(output_file, 'w') as f:
                f.write(f"# Test Session for run{run_number}.py\n")
                f.write(f"# Started: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))}\n")
                f.write(f"# Epoch: {epoch_time}\n")
                f.write("#" + "=" * 49 + "\n\n")
                
                # Add user notes at the top if any
                if user_notes:
                    f.write("## USER OBSERVATIONS\n")
                    for note in user_notes:
                        f.write(f"{note}\n")
                    f.write("\n" + "#" + "-" * 49 + "\n\n")
                
                f.write("## RUN DATA\n")
                f.writelines(output_lines)
                f.write("\n")
            
            print("-" * 50)
            print(f"Output saved to: {output_file}")
            print(f"\nTo analyze this run in Cursor, reference:")
            print(f"  @{output_file.name} and @run{run_number}.py with @AGENTS.md")
        else:
            print("No output captured.")


if __name__ == "__main__":
    main()
