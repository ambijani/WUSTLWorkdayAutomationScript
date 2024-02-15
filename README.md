# WUSTLWorkdayAutomationScript

This repository contains Python scripts for automating the clock-in and clock-out process on a web-based workday portal using Selenium WebDriver. It's designed to ease the daily routine of logging work hours AND ONLY WORKS ON CAMPUS OR VIA VPN. YOU MUST BE CONNECTED TO WASHU WIFI

## Features

- **Automatic Clock-In**: Logs you into the workday portal and performs the clock-in operation automatically.
- **Automatic Clock-Out**: Logs you into the workday portal and performs the clock-out operation automatically.
- **Position Selection**: Allows for selection of job positions during the clock-in process using a positions list.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Code Editor
- ChromeDriver

## Setup Instructions

1. **Install Python and Selenium**:
   Ensure [Python](https://www.python.org/downloads/) 3.x is installed on your system, then use [pip](https://pypi.org/project/pip/) to install Selenium with `pip install selenium`.

2. **ChromeDriver**:
   Download ChromeDriver that matches your Chrome browser's version from the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/) and note its path.

3. **Install Code Editor**:
   Download and install [Visual Studio Code](https://code.visualstudio.com/) or another Python friendly editor. VS Code is recommended for editing Python scripts due to its rich set of features including syntax highlighting, code completion, and debug support.

4. **Configuration**:
   - Update the scripts with the path to your ChromeDriver and the URLs, IDs, or classes specific to your workday portal's login and clock-in/out buttons.

## Usage

- Edit the `positions.txt` file to include the positions (full name) you may need to clock in for, each on a new line.
- Edit the variable inside the '' `chrome_driver_path = ''` with the path of your Chromedriver executable file (try searching for    chromedriver.exe) [Find ChromeDriver Path](#finding-your-chromedriver-path)
- Edit the variables `username_field.send_keys('')` and `password_field.send_keys('')` with your username and password inside the ''
- Run `clockin.py` or `clockout.py` from the command line, providing the line number of your position in `positions.txt` as an argument for clock-in. 
    - For clockin: `python clockin.py <Line Number>`
    - For clockout: `python clockout.py`


## Finding Your ChromeDriver Path

- **Windows**: Place your ChromeDriver in a directory and use the path, e.g., `C:\Path\To\ChromeDriver\chromedriver.exe`.
- **Mac/Linux**: Place it in `/path/to/chromedriver` or `/usr/local/bin` for global access. Ensure it's executable with `chmod +x /path/to/chromedriver`.

## Contributions

Contributions to improve the tool or fix issues are welcome. Please submit a pull request or open an issue for discussion.
