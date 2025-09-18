from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(7)

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()

@then("Verify results contain {expected_product}")
def verify_result(context, expected_product):
    body = context.driver.page_source.lower()
    assert expected_product.lower() in body, f"'{expected_product}' not found in search results"
    print(f"'{expected_product}' found in search results.")
    context.driver.quit()