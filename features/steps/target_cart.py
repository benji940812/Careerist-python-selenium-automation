from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# SEARCH_FIELD = (By.ID, 'search')
# SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
# ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# SIDE_NAV_ADD_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# CART_ICON = (By.XPATH, "//a[contains(@href,'/cart')]")
# CART_ITEM = (By.CSS_SELECTOR, '[data-test="cartItem"]')
# LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
# SIDE_SHEET = (By.CSS_SELECTOR, "[data-test='content-wrapper']")
# VIEW_CART_BTN = (By.XPATH, "//*[@data-test='content-wrapper']//a[contains(@href,'/cart')]")


@given("Open Target homepage")
def open_main(context):
    # context.driver.get("https://www.target.com/")
    context.app.main_page.open_main()

@when("Search for toothbrush")
def search_product(context):
    # WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(SEARCH_FIELD)).send_keys("toothbrush")
    # WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(SEARCH_BTN)).click()
    # WebDriverWait(context.driver, 12).until(EC.presence_of_all_elements_located(LISTINGS))
    context.app.header.search_product("toothbrush")

@when("Click on Add to Cart button")
def click_add(context):
    # btn = WebDriverWait(context.driver, 12).until(EC.element_to_be_clickable(ADD_TO_CART_BTN))
    # context.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
    # btn.click()
    # WebDriverWait(context.driver, 12).until(EC.visibility_of_element_located(SIDE_SHEET))
    # WebDriverWait(context.driver, 12).until(EC.visibility_of_element_located(SIDE_NAV_ADD_BTN))
    context.app.search_results_page.add_first_listing_to_cart()

@when("Confirm Add to Cart button from side navigation")
def confirm_add(context):
    # WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(SIDE_NAV_ADD_BTN)).click() if EC.element_to_be_clickable(SIDE_NAV_ADD_BTN) else None
    # WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable(VIEW_CART_BTN)).click() if EC.element_to_be_clickable(VIEW_CART_BTN) else None
    context.app.search_results_page.confirm_add_from_side_sheet()

@when("Open cart page")
def open_cart(context):
    # sleep(5)
    # context.driver.find_element(*CART_ICON).click()
    context.app.search_results_page.open_cart_from_side_sheet_or_header()

@then("Verify product is in cart")
def verify_cart(context):
    # items = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located(CART_ITEM))
    # assert len(items) > 0, "Cart is empty!"
    # print(f"Cart has {len(items)} item(s)")
    context.app.cart_page.verify_cart_not_empty()