from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def verify_cart_empty_msg(self):
        expected_text = "Your cart is empty"
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        assert expected_text == actual_text, f"Expected '{expected_text}' but got '{actual_text}'"
