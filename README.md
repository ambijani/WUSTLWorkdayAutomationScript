# WUSTLWorkdayAutomationScript

This repository contains Python scripts for automating the clock-in and clock-out process on a web-based workday portal using Selenium WebDriver. It's designed to ease the daily routine of logging work hours **AND ONLY WORKS ON CAMPUS OR VIA VPN. YOU MUST BE CONNECTED TO WASHU WIFI**

## Features

- **Automatic Clock-In**: Logs you into the workday portal and performs the clock-in operation automatically.
- **Automatic Clock-Out**: Logs you into the workday portal and performs the clock-out operation automatically.
- **Position Selection**: Allows for selection of job positions during the clock-in process using a positions list.

## Hotfix Documentation

For a detailed list of hotfixes, including descriptions, dates applied, and contributors, please see our [Hotfixes Documentation](HOTFIXES.md).


## Prerequisites

- Python 3.x
- Selenium WebDriver
- Code Editor

## Setup Instructions

1. **Install Python and Selenium**:
   Ensure [Python](https://www.python.org/downloads/) 3.x is installed on your system, then use [pip](https://pypi.org/project/pip/) to install Selenium with `pip install selenium`.

2. **Install Code Editor**:
   Download and install [Visual Studio Code](https://code.visualstudio.com/) or another Python friendly editor. VS Code is recommended for editing Python scripts due to its rich set of features including syntax highlighting, code completion, and debug support.

3. **Configuration**:
   - Update the scripts with your wustl key and password as well as the positions.txt file with your positions.

## Usage

- Edit the `positions.txt` file to include the positions (full name) you may need to clock in for, each on a new line.
- Edit the variables `username_field.send_keys('')` and `password_field.send_keys('')` with your username and password inside the ''
- Run `clockin.py` or `clockout.py` from the command line, providing the line number of your position in `positions.txt` as an argument for clock-in. 
    - For clockin: `python clockin.py <Line Number>`
    - For clockout: `python clockout.py`

### Demo Video

You can watch a demo video of the WUSTLWorkdayAutomationScript in action below:

https://github.com/user-attachments/assets/96587769-7ebb-42a6-96b3-00c2e2ee15bc






## Contributions
Contributions to improve the tool or fix issues are welcome. Please submit a pull request or open an issue for discussion.
