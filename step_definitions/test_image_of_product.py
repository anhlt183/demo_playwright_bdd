from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from step_definitions.common_steps import *

scenarios('image_of_product.feature')

# Then Steps - Verification/Expected outcomes
@then('all product images should have valid src and alt attributes')
def step_verify_attributes_product_image(home_page: HomePage):
    assert home_page.are_product_images_valid(), "The image has invalid src and alt attribute"
