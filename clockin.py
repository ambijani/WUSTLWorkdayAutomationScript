import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def main(position_line_number):
    positions_file = 'positions.txt'  # The file where positions are listed

    # Read the position name from the file based on the provided line number
    try:
        with open(positions_file, 'r') as file:
            position_name = None
            for i, line in enumerate(file, start=1):
                if i == position_line_number:
                    position_name = line.strip()
                    break
            if position_name is None:
                print(f"Line number {position_line_number} exceeds the number of lines in the file.")
                sys.exit(1)
    except FileNotFoundError:
        print(f"File {positions_file} not found.")
        sys.exit(1)

    # Initialize the browser
    options = Options()
    browser = webdriver.Chrome(options)

    login_url = 'https://one.wustl.edu/launch-task/all/workday'
    browser.get(login_url)
    browser.maximize_window()

    try:
        # Login process
        username_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'ucWUSTLKeyLogin_txtUsername'))
        )
        password_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'ucWUSTLKeyLogin_txtPassword'))
        )
        # Input your credentials
        username_field.send_keys('') # Input your USERNAME in ''
        password_field.send_keys('') # Input your PASSWORD in ''
        browser.find_element(By.ID,'ucWUSTLKeyLogin_btnLogin').click()
        
        # Skip auth button
        skip_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.css-h019vb'))
        )
        skip_button.click()
        print('Login success')

        # Clock-in button
        checkin_button = WebDriverWait(browser, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, 'button.css-1yxsbie')) )
        
        dropdown = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "56$233036-input--uid12-input"))
        )
        dropdown.click()

        xpath_expression = f"//div[@aria-label='{position_name}']"

        # Wait for the element to be clickable and then click on it
        position_option = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        browser.execute_script("arguments[0].scrollIntoView();", position_option) # scroll into element view
        position_option.click()

        ok_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[@data-automation-id='wd-CommandButton' and @title='OK']"
        ))
        )
        ok_button.click()

        print('You successfully clocked-in')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally: 
        time.sleep(5)  
        browser.quit()
        print('You did it!')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clockin.py <Line Number>")
        sys.exit(1)
    try:
        position_line_number = int(sys.argv[1])
        main(position_line_number)
    except ValueError:
        print("Please enter a valid line number as an integer.")
        sys.exit(1)
