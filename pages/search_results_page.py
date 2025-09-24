from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    LISTINGS           = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    ADD_TO_CART_BTN    = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_SHEET         = (By.CSS_SELECTOR, "[data-test='content-wrapper']")
    SIDE_ADD_BTN       = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    VIEW_CART_BTN      = (By.XPATH, "//*[@data-test='content-wrapper']//a[contains(@href,'/cart')]")
    CART_ICON_HEADER   = (By.XPATH, "//a[contains(@href,'/cart')]")

    def verify_search_results(self, product):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert product in actual_text, f'Error. Expected text {product} but got {actual_text}'

    def add_first_listing_to_cart(self):
        WebDriverWait(self.driver, 12).until(EC.presence_of_all_elements_located(self.LISTINGS))
        btn = WebDriverWait(self.driver, 12).until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        btn.click()
        WebDriverWait(self.driver, 12).until(EC.visibility_of_element_located(self.SIDE_SHEET))

    def confirm_add_from_side_sheet(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SIDE_ADD_BTN)).click()
        except Exception:
            pass

    def open_cart_from_side_sheet_or_header(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.VIEW_CART_BTN)).click()
        except Exception:
            self.click(*self.CART_ICON_HEADER)