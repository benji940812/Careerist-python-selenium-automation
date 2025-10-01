from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_URL = "https://www.target.com/orders?lnk=acct_nav_my_account"
    EMAIL_FIELD = (By.XPATH, "//input[@id='username' or @type='email']")
    TERMS_LINK = (By.XPATH,
        "//a[contains(@href,'terms-conditions') or " 
        "contains(normalize-space(.), 'Terms and Conditions') or " 
        "contains(normalize-space(.), 'Terms & Conditions')]"
    )

    def open_signin(self):
        self.open_url(self.SIGN_IN_URL)
        self.wait_until_element_appear(*self.EMAIL_FIELD)

    def click_terms_link(self):
        self.wait_until_clickable_click(*self.TERMS_LINK)

    def verify_terms_page_opened(self):
        self.wait_until_url_contains('terms-conditions')
