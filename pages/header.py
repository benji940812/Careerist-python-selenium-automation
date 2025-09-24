from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    ACCOUNT_BTN = (By.XPATH, "//*[@data-test='accountNav-Account' or @data-test='@web/AccountLink']")
    SIDE_SIGNIN_BTN = (By.XPATH, "//*[@data-test='accountNav-signIn' or @data-test='accountNav-signInButton']")


    def search_product(self, term):
        self.input_text(term, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def open_account_menu(self):
        self.click(*self.ACCOUNT_BTN)

    def click_side_signin(self):
        self.click(*self.SIDE_SIGNIN_BTN)