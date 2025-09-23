from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


    def search_product(self, term):
        self.input_text(term, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)
