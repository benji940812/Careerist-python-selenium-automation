from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given("I open Target homepage")
# def step_open_target(context):
#     context.driver.get("https://www.target.com/")
#     sleep(3)
def step_open_target(context):
    context.app.main_page.open_main()

@when("I click the Account icon on top right")
# def step_click_account_icon(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]').click()
#     sleep(1)
def step_click_account_icon(context):
    context.app.header.open_account_menu()

@when("I click the Sign in or create account button")
# def step_click_sign_in_menu(context):
#     context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
#     sleep(3)
def step_click_sign_in_menu(context):
    context.app.header.click_side_signin()

@then("I should see the Sign In form")
# def step_verify_sign_in_form(context):
#     sign_in_input = context.driver.find_element(By.XPATH, "//input[@id='username']")
#     assert sign_in_input.is_displayed(), "Sign In form not displayed"
#     print("Sign In form is displayed as expected")
#     context.driver.quit()
def step_verify_sign_in_form(context):
    context.app.sign_in_page.verify_form_opened()