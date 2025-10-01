from behave import given, when, then
from time import sleep


@given("Open sign in page")
def open_sign_in(context):
    context.app.sign_in_page.open_signin()


@when("Store original window")
def store_window(context):
    context.original_window = context.app.page.get_original_window()
    print('Original window: ', context.original_window)


@when("Click on Target terms and conditions link")
def click_terms_link(context):
    context.app.sign_in_page.click_terms_link()
    sleep(2)


@when("Switch to the newly opened window")
def switch_window(context):
    context.app.page.switch_to_newly_opened_window([context.original_window])


@then("Verify Terms and Conditions page is opened")
def verify_tnc_opened(context):
    context.app.sign_in_page.verify_terms_page_opened()


@then("User can close new window and switch back to original")
def return_to_original(context):
    context.app.page.close()
    context.app.page.switch_to_window_by_id(context.original_window)
    sleep(2)
