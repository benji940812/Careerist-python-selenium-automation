from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@given("Open target main page")
def open_main(context):
    context.driver.get("https://www.target.com/")
    sleep(3)

@when("Click on Target Circle link")
def click_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='TargetCircle']").click()
    sleep(3)

@then("Verify there are at least {expected_amount:d} benefit cells")
def verify_benefit_cells(context, expected_amount):
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='CellsComponent/Link']")
    assert len(cells) >= expected_amount, f"Expected at least {expected_amount} cells, but got {len(cells)}"
    print(f"Found {len(cells)} benefit cells (>= {expected_amount})")
    context.driver.quit()

