Team Bob the Builders – FIRST LEGO League Robot Code

Public FIRST LEGO League robot code by Team Bob the Builders.

This repository contains the code for our robot, Jobo, developed using Pybricks on the LEGO SPIKE Prime Hub. The project focuses on a fully open source, modular architecture with precise drivetrain control and reliable autonomous routines. This enables fast iteration, flexible attachment integration, and consistent competition performance.

Primary development branch: main
All related documentation, designs, and resources are openly available.

Project Status and Robot Open Sourcing

We are currently working on fully open sourcing our robot design as well.

Our current progress, including early documentation and build details, is available here:
https://sites.google.com/view/bobthebuilders-/home

The robot open source release is still in progress and will be completed soon. It will include clearer build instructions, improved diagrams, and more polished documentation for both the robot hardware and the codebase.

Key Features

1. IMU based Correction
Maintains precise heading and orientation for accurate movements.

2. Hub Button Controls
Change and select autonomous runs directly from the hub.

3. Color Sensor Detection
Automatically selects the run based on which fixture is attached.

4. Logging and Debug Mode
Records run data and uses AI to analyze performance and provide reliability tips.

5. Modular Functions
Clean, organized, reusable functions for maintainable code.

6. Multiple Movement Types
Supports different motion patterns for flexible and reliable robot behavior.

How to Use Our Code

If you are familiar with GitHub, using an IDE such as VS Code or Cursor, working with the terminal, and programming in Python with Pybricks, you can clone the repository and access the complete codebase directly.

Otherwise, follow the full beginner guide below.

How to Run Jobo’s Code – Full Beginner Guide

Phase 0: Get Your Gear

Get a LEGO SPIKE Prime Hub. Do not skip this.
Build the robot using the instructions in Tab 1. Follow exactly.
If a part is missing or incorrect, the robot will not work as intended.

Phase 1: Install Pybricks on Your Computer

Mac

Open Terminal.
Check Python version using: python3 --version (must be 3.10 or higher).
If Python is not installed, run: brew install python

Create a project folder:
mkdir ~/jobo_robot

Enter the folder:
cd ~/jobo_robot

Create a virtual environment:
python3 -m venv venv

Activate the virtual environment:
source venv/bin/activate

Install Pybricks tools:
pip install pybricks pybricksdev

Windows

Open Command Prompt or PowerShell.
Check Python version using: python --version (must be 3.10 or higher).
If not installed, download from python.org.

Create a project folder:
mkdir C:\jobo_robot

Enter the folder:
cd C:\jobo_robot

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
venv\Scripts\activate

Install Pybricks tools:
pip install pybricks pybricksdev

Linux

Open Terminal.
Check Python version using: python3 --version (must be 3.10 or higher).
If not installed, run:
sudo apt update
sudo apt install python3 python3-venv python3-pip -y

Create a project folder:
mkdir ~/jobo_robot

Enter the folder:
cd ~/jobo_robot

Create a virtual environment:
python3 -m venv venv

Activate the virtual environment:
source venv/bin/activate

Install Pybricks tools:
pip install pybricks pybricksdev

Phase 1.5: Install Pybricks Firmware on the Hub

Turn on the SPIKE Prime Hub.
Connect it to your computer using USB or Bluetooth.
Run the firmware installer:
pybricksdev firmware

Follow the on screen instructions to replace the LEGO firmware with Pybricks.

Warning: This will erase the original LEGO firmware.

Once complete, the hub is ready to run Python code.

Phase 2: Install the IDE and Get the Code

Install an IDE. Cursor is recommended.

Download Cursor from: https://cursor.so
Install it like any normal application.

Open Cursor.
Select Open Project, then Clone from GitHub.
Enter the repository URL:
https://github.com/YourTeam/YourRepoName.git

Choose your project folder:
Mac or Linux: ~/jobo_robot
Windows: C:\jobo_robot

Switch to the robot code branch named jobos_code using Cursor’s Git tools or by running:
git checkout jobos_code

Phase 3: Run the Code on Jobo

Connect the SPIKE Prime Hub using USB or Bluetooth.
Make sure your virtual environment is active.

Mac or Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

Run the main program:
pybricksdev run main.py

Use the hub buttons to select autonomous runs.
Observe robot behavior. If something is wrong, review debug logs and graphs.

Extra Tips and Warnings

Always activate the virtual environment before running Pybricks commands.
Python must be version 3.10 or higher.
If packages are missing, reinstall them using: pip install pybricks pybricksdev
Do not skip steps. Missing a folder, virtual environment, branch, or firmware will break the setup.
Most issues are hardware related. Check wiring, motors, and attachments first.
