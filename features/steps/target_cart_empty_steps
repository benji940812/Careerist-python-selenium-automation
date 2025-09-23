from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("I open Target main page")
def open_main(context):
    context.driver.get("https://www.target.com/")
    sleep(3)


@when ("I click the Cart icon")
def click_cart(context):
    context.driver.find_element(By.XPATH,'//a[@data-test="@web/CartLink"]').click()
    sleep(3)


@then('I should see "Your cart is empty"')
def verify_empty_cart_msg(context):
    actual_text = context.driver.find_element(By.XPATH, '//*[contains(text(), "Your cart is empty")]').text
    expected_text = "Your cart is empty"
    assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
    context.driver.quit()