Feature: Validate for checkout function
  As a logged in user
  I want to validate for checkout function

  # Background: Steps that run before each scenario
  Background:
    Given I already logged in with username is "standard_user" and password is "secret_sauce"
    And I already click on Add to cart button on inventory page of "Sauce Labs Backpack"

  Scenario: Verify that user can checkout the product
    When I navigate to the cart page of "Sauce Labs Backpack"
    And I click on the Checkout button
    Then The Your Information page is displayed
    When I enter First Name "Anh", Last Name "Le", Zip "700000"
    And I click on Continue button
    Then The Overview page of "Sauce Labs Backpack" is displayed
    When I click on Finish button
    Then The Complete page is displayed
    And The Thank you message is displayed

  Scenario: Verify that user can cancel the checkout
    When I navigate to the cart page of "Sauce Labs Backpack"
    And I click on the Checkout button
    And I enter First Name "Anh", Last Name "Le", Zip "700000"
    And I click on Continue button
    And I click on Cancel button on Complete page
    Then I navigate back to Inventory page

