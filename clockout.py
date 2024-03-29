from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver_path = '' # Specify the path to your chromedriver.exe in ''

# Set the ChromeDriver executable path using ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--webdriver={chrome_driver_path}')

# Initialize the browser
browser = webdriver.Chrome(options=chrome_options)
login_url = 'https://one.wustl.edu/launch-task/all/workday'

# Open the login page
browser.get(login_url)

try:
    username_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'ucWUSTLKeyLogin_txtUsername'))
    )
    password_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'ucWUSTLKeyLogin_txtPassword'))
    )

    # Input your credentials
    username_field.send_keys('') # Input your USERNAME in ''
    password_field.send_keys('') # Input your PASSWORD in ''

    # Submit the login form
    browser.find_element(By.ID,'ucWUSTLKeyLogin_btnLogin').click()
    
    #press skip auth button
    skip_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.css-h019vb'))
    )
    skip_button.click()
    print('Login success')

    # Find and click the "Check Out" button by CSS Selector
    check_out_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Check Out"]'))
    )
    check_out_button.click()

    ok_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-automation-id="wd-CommandButton_uic_okButton"]'))
    )
    ok_button.click()

    print('you successfully clocked out')

    
except Exception as e:
    print(f"An error occurred: {e}")

finally: 
    time.sleep(5)
    browser.quit()
    print('you did it!')
