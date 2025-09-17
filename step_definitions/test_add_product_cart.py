from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_detail_page import ProductDetailPage
from step_definitions.common_steps import *

scenarios('add_product_cart.feature')

# When Steps - Actions being performed
@when(parsers.parse('I click on Add to cart button on product detail page'))
def step_add_to_cart_product_detail(product_detail_page: ProductDetailPage):
    product_detail_page.click_add_to_cart_product_detail()    

# Then Steps - Verification/Expected outcomes
@then(parsers.parse('The Remove button of {product_name} is displadyed'))
def step_check_remove_button_display(home_page: HomePage, product_name):
    assert home_page.is_remove_button_display(product_name.strip('"')), f"Can not add product {product_name} to cart page"

@then(parsers.parse('The number of product in cart should be {expect_count}'))
def step_check_number_product_in_cart(home_page: HomePage, expect_count):
    assert home_page.is_cart_badge_count_correct(expect_count.strip('"')), "The number of product in cart is incorrect"

@then(parsers.parse('The product {product_name} is displayed in cart page'))  
def step_check_product_display_cart_page(cart_page: CartPage, product_name):
    assert cart_page.is_product_add_to_cart(product_name.strip('"')), f"Can not add product {product_name} to cart page"      
    