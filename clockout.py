from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


# Initialize the browser
options = Options()
browser = webdriver.Chrome(options)
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
    skip_button = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.css-h019vb'))
        )
    skip_button.click()
    print('Login success')

    # Find and click the "Check Out" button by XPath
    check_out_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='css-1c82jai' and span[text()='Check Out']]"))
    )
    check_out_button.click()

    # Confirm the clock-out action by clicking the "OK" button
    ok_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[@data-automation-id='wd-CommandButton' and @title='OK']"
        ))
        )
    ok_button.click()

    print('you successfully clocked out')

    
except Exception as e:
    print(f"An error occurred: {e}")

finally: 
    time.sleep(5)
    browser.quit()
    print('You successfully clocked-out')
