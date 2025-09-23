from behave import given, when, then

@given('Open Target main page')
def open_main(context):
    context.app.main_page.open_main()

@when('Search for {search_word}')
def search_product(context, search_word):
    context.search_word = search_word
    context.app.header.search_product(search_word)

@then('Verify search results are shown for tea')
def verify_results(context):
    context.app.search_results_page.verify_search_results('tea')