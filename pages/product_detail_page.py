import os
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import product_detail_locators as pro
from pages.base_page import BasePage

class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()
        self.base_page = BasePage(page)

        # Product Detail Page Elements
        self.product_title = page.locator(pro.PRODUCT_TITLE)
        self.add_to_cart_button = page.locator(pro.ADD_TO_CART_BUTTON)


    def is_open_correct_product(self, expected):
        self.logger.info("Verify product title is correct")
        try:
            expect(self.product_title).to_have_text(expected)
            return True
        except Exception as e:
            self.logger.error(f"can not navigate to correct product detail: {e}")
            self.base_page.attach_screenshot("navigate fail")
            return False
        
    def click_add_to_cart_product_detail(self):
        self.logger.info("Click Add to cart button on product detail page")
        self.add_to_cart_button.click()
          





        
        

    