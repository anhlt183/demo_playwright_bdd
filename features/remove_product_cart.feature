Feature: Validate for adding/removing product to/from cart
  As a logged in user
  I want to validate for adding/removing product to/from cart

  # Background: Steps that run before each scenario
  Background:
    Given I already logged in with username is "standard_user" and password is "secret_sauce"
    And I already click on Add to cart button on inventory page of "Sauce Labs Backpack"

  Scenario: Verify that user can remove product from inventory page
    When I click on Remove button on inventory page of "Sauce Labs Backpack"
    Then The number of product in cart should be disappear
    And The Add to cart button of "Sauce Labs Backpack" is displadyed
    And The product "Sauce Labs Backpack" is removed from cart page

  Scenario: Verify that user can remove product from cart page  
    When I navigate to the cart page of "Sauce Labs Backpack"
    And I click on Remove button on cart page of "Sauce Labs Backpack"
    Then The product "Sauce Labs Backpack" is removed from cart page
    When I click on continue shopping button to navigate back to Inventory page
    Then The Add to cart button of "Sauce Labs Backpack" is displadyed