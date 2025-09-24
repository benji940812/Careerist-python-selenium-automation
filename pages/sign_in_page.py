from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    EMAIL_FIELD = (By.XPATH, "//input[@id='username' or @type='email']")

    def verify_form_opened(self):
        self.find_element(*self.EMAIL_FIELD)