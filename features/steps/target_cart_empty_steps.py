from behave import given, when, then
from selenium.webdriver.common.by import By


CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.XPATH, "//div[./span{contains(text(), 'subtotal')]]")


@given("I open Target main page")
def open_main(context):
    context.app.main_page.open_main()


@when ("I click the Cart icon")
def click_cart(context):
    context.app.header.click_cart()


@then('I should see "Your cart is empty"')
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_cart_empty_msg()