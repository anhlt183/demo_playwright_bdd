from pytest_bdd import scenarios, given, when, then, parsers
from pages.cart_page import CartPage
from pages.your_information_page import InformationPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage
from step_definitions.common_steps import *

scenarios('checkout.feature')

# When Steps - Actions being performed
@when('I click on the Checkout button')
def step_click_checkout_button(cart_page: CartPage):
    cart_page.click_checkout_button()

@when(parsers.parse('I enter First Name {firstname}, Last Name {lastname}, Zip {zip}'))
def step_enter_your_information(your_information_page: InformationPage, firstname, lastname, zip):
    your_information_page.enter_firstname(firstname.strip('"'))
    your_information_page.enter_lastname(lastname.strip('"'))
    your_information_page.enter_zip(zip.strip('"'))

@when('I click on Continue button')
def step_click_continue_button(your_information_page: InformationPage):
    your_information_page.click_continue_button()

@when('I click on Finish button')
def step_click_finish_button(overview_page: OverviewPage):
    overview_page.click_finish_button()        
@when('I click on Cancel button on Complete page')
def step_click_cancel_button(complete_page: CompletePage):
    complete_page.click_cancel_button()
    
# Then Steps - Verification/Expected outcomes
@then('The Your Information page is displayed')
def step_check_your_information_display(your_information_page: InformationPage):
    assert your_information_page.navigate_to_your_information_page(), "User can not navigate to your information page"

@then(parsers.parse('The Overview page of {product_name} is displayed'))
def step_check_overview_page_display(overview_page: OverviewPage, product_name):
    assert overview_page.is_product_correct_in_overview(product_name.strip('"')), f"The overview page include {product_name} is not displayed"

@then('The Complete page is displayed')
def step_check_complete_page_display(complete_page: CompletePage):
    assert complete_page.is_complete_page_open(), "The complete page is not displayed"

@then('The Thank you message is displayed')
def step_check_success_message(complete_page: CompletePage):
    assert complete_page.is_successfull_message_display(), "The checkout is unsuccessfull"             

