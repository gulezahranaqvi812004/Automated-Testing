import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
with open('test_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            driver.get("https://practicetestautomation.com/practice-test-login/")
            driver.find_element(By.ID, "username").send_keys(row['username'])
            driver.find_element(By.ID, "password").send_keys(row['password'])
            driver.find_element(By.ID, "submit").click()
            time.sleep(5)
            try:
                driver.find_element(By.ID, "logout")  
                # print(f"Login successful for user: {row['username']}")
                driver.get("https://practicetestautomation.com/practice-test-login/")
                print("Redirected back to the login page.")
            except Exception:
                print(f"Login failed for user: {row['username']}")
        except Exception as e:
            print(f"Error: {e}")

driver.quit()
