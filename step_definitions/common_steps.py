from pytest_bdd import scenarios, then, given, when, parsers
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_detail_page import ProductDetailPage

# LOGIN
@given(parsers.parse('I already logged in with username is "{username}" and password is "{password}"'))
def step_verify_user_already_logged_in(login_page : LoginPage, username, password):
    login_page.login(username, password)

# Check login form is visible
@then('the login form should still be visible')
def step_verify_login_form_visible(login_page: LoginPage):
    assert login_page.is_login_form_visible(), "Login form is not visible"     

#HOME PAGE
# Check is in Home page
@given('I should be redirected to the Home page')
@then('I should be redirected to the Home page')
def step_verify_home_page_redirect(login_page : LoginPage):
    assert login_page.is_login_successful(), "Login was not successful"

# Check is in Inventory page
@given('The inventory page is opened')
@when('I open inventory page')
@then('I navigate back to Inventory page')
def step_verify_inventory_page_is_open(home_page: HomePage):
    assert home_page.is_inventory_page_open(), "Product list isn't displayed"    

# Check product images are visible
@given('all product images should be visible')
@then('all product images should be visible')
def step_verify_product_images_are_visible(home_page: HomePage):
    assert home_page.are_product_images_visible(), "System can not load the image"

# Click on product image
@when(parsers.parse('I click on the image of {option}'))
def step_click_product_image(home_page: HomePage, option):
    home_page.click_product_image(option.strip('"'))

# Click on Add to cart button
@given(parsers.parse('I already click on Add to cart button on inventory page of {product_name}'))
@when(parsers.parse('I click on Add to cart button on inventory page of {product_name}'))
def step_add_to_cart_inventory(home_page: HomePage, product_name):
    home_page.click_add_product_to_cart(product_name.strip('"'))        

#PRODUCT DETAIL PAGE
# Check is in Inventory page
@when(parsers.parse('I am in the product detail page of {expect}'))
@then(parsers.parse('I should be redirected to the product detail page for {expect}'))
def step_verify_correct_product_detail(product_detail_page: ProductDetailPage, expect):
    assert product_detail_page.is_open_correct_product(expect.strip('"')), "User can not be redirected to the product detail page"

#CART PAGE
# Check is in Cart page
@when(parsers.parse('I navigate to the cart page of {product_name}'))  
def step_verify_cart_page_redirect(cart_page: CartPage, product_name):
    assert cart_page.is_product_add_to_cart(product_name.strip('"')), "Can not open cart page"           