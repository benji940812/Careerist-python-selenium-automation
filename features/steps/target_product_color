from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-54475621 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/men-s-straight-fit-jeans-goodfellow-co-153/-/A-54475621?preselect=88011565#lnk=sametab')
    sleep(5)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Jet Black', 'Indigo', 'Light Blue Denim', 'Medium Blue']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for c in colors:
        c.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'