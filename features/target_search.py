from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
sleep(5)

# Search:
account_button = driver.find_element(By.XPATH, '//a[@id="account-sign-in"]')
account_button.click()
sleep(3)

# navigate to Sign In page from Account menu
driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]''').click()
sleep(3)

# Verify : "Sign in or create account" texts are shown
driver.find_element(By.XPATH, '//*[contains(text(), "Sign in or create account")]')
print("Verified: 'Sign in or create account' text is displayed on the page.")

# Verify : "Sign in (Continue)" button is shown
driver.find_element(By.XPATH, '//*[contains(text(), "Continue")]')
print("Verified: 'Sign in (Continue)' text is displayed on the page.")

# Close the browser after verificaiton
driver.quit()