Feature: Target product search

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <product>
    Then Verify results contain <expected_product>

  Examples:
    | product     | expected_product |
    | dish soap   | dish soap        |
    | socks       | socks            |
    | watermelon  | watermelon       |