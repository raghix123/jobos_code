Public FIRST LEGO League robot code by Team Bob the Builders. This repository contains the code for our robot, Jobo, developed using Pybricks on the LEGO SPIKE Prime hub. The project focuses on a fully open-source, modular architecture with precise drivetrain control and reliable autonomous routines, enabling fast iteration, flexible attachment integration, and consistent competition performance. The primary development branch is main, and all related documentation, designs, and resources are openly available.

Our code best features are:

  1. IMU-based Correction: Maintains precise heading and orientation for accurate movements.
  2. Hub Button Controls: Change and select autonomous runs on the fly.
  3. Color Sensor Detection: Auto selects the run based on what fixture is on the robot.
  4. Logging & Debug Mode: Records data and uses AI to analyze runs and give relibility tips.
  5. Modular Functions: Organized code with reusable functions for clean, maintainable logic.
  6. Multiple Movement Types: Supports various motion patterns for flexible and reliable robot behavior.




How to use our code:
If you’re familiar with GitHub, using an IDE such as VS Code or Cursor, working with the terminal, and programming in Python with Pybricks, you can clone the repository and access the complete codebase directly. Otherwise, you can scroll down for detailed instructions. This allows anyone to explore our implementation, learn from it, or build upon it for their own projects.

How to Run Jobo’s Code – Full Beginner Guide
Phase 0: Get Your Gear
    Get a LEGO SPIKE Prime Hub. Do not skip this.
    Build your robot using the instructions in Tab 1. Follow exactly. If you miss a piece, it won’t work.
    Phase 1: Install Pybricks on Your Computer
    Mac:
    Open Terminal (search Spotlight → Terminal).
    Check Python: python3 –version (must be 3.10+)
    If not installed → brew install python
    Make a folder: mkdir ~/jobo_robot
    Go into it: cd ~/jobo_robot
    Create virtual environment: python3 -m venv venv
    Activate it: source venv/bin/activate (you should see (venv) in front of the prompt)
    Install Pybricks dev tools: pip install pybricks pybricksdev
    Windows:
    Open Command Prompt or PowerShell.
    Check Python: python –version (must be 3.10+)
    If not → install from https://www.python.org/downloads/windows/
    Make a folder: mkdir C:\jobo_robot
    Go into it: cd C:\jobo_robot
    Create virtual environment: python -m venv venv
    Activate it: venv\Scripts\activate
    Install Pybricks dev tools: pip install pybricks pybricksdev
    Linux:
    Open Terminal.
    Check Python: python3 –version (must be 3.10+)
    If not → sudo apt updatesudo apt install python3 python3-venv python3-pip -y
    Make a folder: mkdir ~/jobo_robot
    Go into it: cd ~/jobo_robot
    Create virtual environment: python3 -m venv venv
    Activate it: source venv/bin/activate
    Install Pybricks dev tools: pip install pybricks pybricksdev
Phase 1.5: Install Pybricks Firmware on the Hub
    Turn on your SPIKE Prime Hub.
    Connect it via USB or Bluetooth to your computer.
    Run Pybricks firmware installer: pybricksdev firmware
    Follow instructions to replace LEGO firmware with Pybricks.
    Warning: This erases the old LEGO firmware.
    When finished, your hub is ready to run Python code.
Phase 2: Install the IDE and Get the Code
    Install the IDE (Cursor recommended)
    Go to https://cursor.so and download the version for your OS.
    Install it like any normal program.
    Open Cursor IDE
    Clone the GitHub repository into Cursor
    In Cursor, select “Open Project” → “Clone from GitHub”
    Enter the repository URL: https://github.com/YourTeam/YourRepoName.git
    Choose the folder you made earlier (~/jobo_robot or C:\jobo_robot)
    Switch to the main robot code branch: jobos_code
    Use Cursor’s Git tools or run git checkout jobos_code
Phase 3: Run the Code on Jobo
    Connect your SPIKE Prime Hub via USB or Bluetooth.
    Make sure your virtual environment is active:
    Mac/Linux: source venv/bin/activate
    Windows: venv\Scripts\activate
    Run the main program: pybricksdev run main.py
    Use the hub buttons to select different autonomous runs.
    Watch the robot move. If it doesn’t behave as expected, check debug logs and graphs.
Extra Tips / Warnings
  1. Always activate your virtual environment before running Pybricks commands.
  2. Python must be version 3.10 or higher.
  3. If you see an error about missing packages, run: pip install pybricks pybricksdev again.
  4. Don’t skip steps; missing a folder, venv, branch, or firmware will break everything.
  5. Most errors are hardware issues: check wiring, motors, and attachments first.
