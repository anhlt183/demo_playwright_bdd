Feature: Validate for adding/removing product to/from cart
  As a logged in user
  I want to validate for adding/removing product to/from cart

  # Background: Steps that run before each scenario
  Background:
    Given I already logged in with username is "standard_user" and password is "secret_sauce"
    And The inventory page is opened
    And all product images should be visible

  Scenario: Verify that user can add product from inventory page
    When I click on Add to cart button on inventory page of "Sauce Labs Backpack"
    Then The Remove button of "Sauce Labs Backpack" is displadyed
    And The number of product in cart should be "1"
    And The product "Sauce Labs Backpack" is displayed in cart page

  Scenario: Verify that user can add product from product detail page
    When I click on the image of "Sauce Labs Backpack"
    And I am in the product detail page of "Sauce Labs Backpack"
    And I click on Add to cart button on product detail page
    Then The number of product in cart should be "1"
    And The product "Sauce Labs Backpack" is displayed in cart page

  Scenario Outline: Verify that user can add product from inventory page with other product
    When I click on Add to cart button on inventory page of "<product_name>"
    Then The number of product in cart should be "<expect_count>"
    And The product "<product_name>" is displayed in cart page

    # Examples: Data table for Scenario Outline
    Examples:
      | product_name                  |expect_count |            
      | Sauce Labs Bike Light         |1            | 
      | Sauce Labs Fleece Jacket      |1            | 
