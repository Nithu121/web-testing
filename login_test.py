import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load the Excel file
login_data = pd.read_excel('test_cases.xlsx', sheet_name='Login')

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed

for index, row in login_data.iterrows():
    driver.get('C:/Users/91849/Desktop/b/project/login.html')  # Update the path

    # Fill out the login form
    driver.find_element(By.ID, 'loginEmail').send_keys(row['Email'])
    time.sleep(1)
    driver.find_element(By.ID, 'loginPassword').send_keys(row['Password'])
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    time.sleep(1)
    # Add assertion or verification here

driver.quit()