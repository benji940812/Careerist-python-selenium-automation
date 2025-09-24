from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    CART_ITEM = (By.CSS_SELECTOR, '[data-test="cartItem"]')

    def verify_cart_empty_msg(self):
        expected_text = "Your cart is empty"
        actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

    def verify_cart_not_empty(self):
            items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.CART_ITEM)
            )
            assert len(items) > 0, "Cart is empty!"