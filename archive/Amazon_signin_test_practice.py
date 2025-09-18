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

# open the Amazon Sign-In page (for some reason i can't get the URL for the sign-in page)
driver.get("https://www.amazon.com")
sleep(5)

# top right corner "Account & Lists" click since it won't let me get to the sign-in page right away for some reason
driver.find_element(By.XPATH, '//a[@id="nav-link-accountList"]').click()
sleep(5)

# click "Sign in" inside the flyout (this actually navigates to the Sign-In page)
driver.find_element(By.XPATH, '//a[@id="nav-flyout-ya-signin-button"]').click()
sleep(5)

####### Amazon Sign-In page - locator verification test#########

# Amazon logo - by class a-icon-logo
driver.find_element(By.XPATH, '//i[contains(@class,"a-icon-logo")]')

Email field - by id ap_email
driver.find_element(By.XPATH, '//i[contains(@class,"a-icon-logo")]')
