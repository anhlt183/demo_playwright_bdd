import os
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import cart_locators as ca
from pages.base_page import BasePage

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()
        self.base_page = BasePage(page)

        # Cart Page Elements
        self.cart_icon = page.locator(ca.CART_ICON)
        self.cart_page_title = page.locator(ca.CART_PAGE_TITLE)
        self.product_title = page.locator(ca.PRODUCT_TITLE)
        self.continue_shopping = page.locator(ca.CONTINUE_SHOPPING)
        self.checkout = page.locator(ca.CHECKOUT_BUTTON)   

    def click_cart_icon(self):
        self.logger.info("Click on cart icon to navigate to cart page")
        self.cart_icon.click()

    def click_continue_shopping(self):
        self.logger.info("Click on continue shopping button to back to inventory page")
        self.continue_shopping.click()    

    def click_remove_product_from_cart(self, product_name):
        self.logger.info("Click Remove button")
        remove_button = self.base_page.locator_remove_button_cart(product_name)
        remove_button.click()          

    def is_cart_page_open(self):
        self.logger.info("check the cart page is opened")
        try:
            self.click_cart_icon()
            expect(self.cart_page_title).to_have_text(ca.PAGE_TITLE)
            return True
        except Exception as e:
            self.logger.error(f"Can not open cart page: {e}")
            self.base_page.attach_screenshot("Open cart page fail")
            return False

    def click_checkout_button(self):
        self.logger.info("Click on checkout button on cart page")
        self.checkout.click()       
        
    def is_product_add_to_cart(self, product_name):
        self.logger.info("check the product is displayed on cart page")
        try:
            self.is_cart_page_open()
            expect(self.product_title).to_have_text(product_name)
            return True
        except Exception as e:
            self.logger.error(f"can not add product to cart page: {e}")
            self.base_page.attach_screenshot("add product fail")
            return False
        
    def is_product_remove_from_cart(self, product_name):
        self.logger.info("check the product is removed from cart page")
        try:
            self.is_cart_page_open()
            expect(self.product_title.filter(has_text=product_name)).to_have_count(0)
            return True
        except Exception as e:
            self.logger.error(f"Can not remove product from cart: {e}")
            self.base_page.attach_screenshot("Remove fail")
            return False
