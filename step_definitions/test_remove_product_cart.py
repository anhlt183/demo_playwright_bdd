from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_detail_page import ProductDetailPage
from step_definitions.common_steps import *

scenarios('remove_product_cart.feature')

# When Steps - Actions being performed
@when(parsers.parse('I click on Remove button on inventory page of {product_name}'))
def step_remove_inventory(home_page: HomePage, product_name):
    home_page.click_remove_product_from_inventory(product_name.strip('"'))

@when(parsers.parse('I click on Remove button on cart page of {product_name}'))
def step_remove_cart(cart_page: CartPage, product_name):
    cart_page.click_remove_product_from_cart(product_name.strip('"'))    

@when('I click on continue shopping button to navigate back to Inventory page')
def step_back_to_inventory_from_cart(cart_page: CartPage):
    cart_page.click_continue_shopping()
    
# Then Steps - Verification/Expected outcomes
@then('The number of product in cart should be disappear')
def step_check_number_product_in_cart(home_page: HomePage):
    assert home_page.is_cart_badge_not_displayed(), "Can not remove product from cart"

@then(parsers.parse('The Add to cart button of {product_name} is displadyed'))
def step_check_add_to_cart_button_display(home_page: HomePage, product_name):
    assert home_page.is_add_to_cart_button_display(product_name.strip('"')), "add to cart button is not displayed after click remove button"    

@then(parsers.parse('The product {product_name} is removed from cart page'))  
def step_check_product_remove_cart_page(cart_page: CartPage, product_name):
    assert cart_page.is_product_remove_from_cart(product_name.strip('"')), f"Can not remove product {product_name} from cart page"      
    