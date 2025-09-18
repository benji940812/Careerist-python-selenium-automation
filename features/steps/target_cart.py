from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
CART_ICON = (By.XPATH, "//a[@href='/cart']")
CART_ITEM = (By.CSS_SELECTOR, '[data-test="cartItem"]')


@given("Open Target homepage")
def open_main(context):
    context.driver.get("https://www.target.com/")


@when("Search for toothbrush")
def search_product(context):
    sleep(2)
    context.driver.find_element(*SEARCH_FIELD).send_keys("toothbrush")
    context.driver.find_element(*SEARCH_BTN).click()


@when("Click on Add to Cart button")
def click_add(context):
    sleep(12)
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when("Confirm Add to Cart button from side navigation")
def confirm_add(context):
    sleep(2)
    context.driver.find_element(*SIDE_NAV_ADD_BTN).click()


@when("Open cart page")
def open_cart(context):
    sleep(5)
    context.driver.find_element(*CART_ICON).click()


@then("Verify product is in cart")
def verify_cart(context):
    sleep(3)
    items = context.driver.find_elements(*CART_ITEM)
    assert len(items) > 0, "Cart is empty!"
    print(f"Cart has {len(items)} item(s)")
