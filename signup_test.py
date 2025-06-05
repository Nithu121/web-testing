import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Load the Excel file
signup_data = pd.read_excel('test_cases.xlsx', sheet_name='Signup')
login_data = pd.read_excel('test_cases.xlsx', sheet_name='Login')

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed

# Iterate through each user in the signup data
for index, row in signup_data.iterrows():
    driver.get('C:/Users/91849/Desktop/b/project/signup.html')  # Update the path
    time.sleep(2)  # Wait for the signup page to load

    # Fill out the signup form
    driver.find_element(By.ID, 'username').send_keys(row['Username'])
    time.sleep(1)
    driver.find_element(By.ID, 'email').send_keys(row['Email'])
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys(row['Password'])
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[text()="Sign Up"]').click()
    time.sleep(3)  # Wait for the alert to appear

    # Handle the signup alert message
    try:
        alert = Alert(driver)
        alert_message = alert.text  # Get the alert message text
        alert.accept()  # Click OK on the alert
        print(f"Alert accepted: {alert_message}")

        # Check if the signup was successful
        success_message = "Signup successful"  # Replace with the actual success message expected after signup
        if success_message in alert_message:
            print(f"Signup successful for {row['Username']}")

            # Now, proceed to login
            for login_index, login_row in login_data.iterrows():
                driver.get('C:/Users/91849/Desktop/b/project/login.html')  # Navigate to the login page
                time.sleep(3)  # Wait for the page to load

                # Fill out the login form
                driver.find_element(By.ID, 'loginEmail').send_keys(login_row['Email'])
                time.sleep(1)
                driver.find_element(By.ID, 'loginPassword').send_keys(login_row['Password'])
                time.sleep(1)
                driver.find_element(By.XPATH, '//button[text()="Login"]').click()
                time.sleep(3)  # Wait for the login process to complete

                # Handle the login alert message
                try:
                    alert = Alert(driver)
                    login_alert_message = alert.text  # Get the login alert message text
                    alert.accept()  # Click OK on the alert
                    print(f"Login alert accepted: {login_alert_message}")

                    # Verify login success
                    login_success_message = "Welcome"  # Replace with the actual success message after login
                    time.sleep(2)  # Wait to ensure the page is fully loaded
                    if login_success_message in driver.page_source:
                        print(f"Login successful for {login_row['Email']}")
                    else:
                        print(f"Login failed for {login_row['Email']}")

                except Exception as e:
                    print(f"No alert after login for {login_row['Email']} or error: {e}")
                    time.sleep(2)  # Additional wait time

        else:
            print(f"Signup failed for {row['Username']}")

    except Exception as e:
        print(f"No alert for {row['Username']} or error: {e}")
        time.sleep(3)  # Wait before moving to the next user

driver.quit()
