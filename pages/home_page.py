import os
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import home_locators as ho
from pages.base_page import BasePage
class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()
        self.base_page = BasePage(page)

        # Home Page Elements
        self.product_sort_dropdown = page.locator(ho.PRODUCT_SORT_DROPDOWN)
        self.product_name_list = page.locator(ho.PRODUCT_NAME_LIST)
        self.product_price_list = page.locator(ho.PRODUCT_PRICE_LIST)
        self.product_image_list = page.locator(ho.PRODUCT_ITEM_IMAGE)
        self.product_page_title = page.locator(ho.PRODUCT_PAGE_TITLE)
        self.active_option = page.locator(ho.ACTIVE_OPTION)
        self.cart_badge = page.locator(ho.CART_BADGE)

    def is_product_sort_container_visible(self):
        return self.product_sort_dropdown.is_visible()
    
    def is_inventory_page_open(self):
        self.logger.info("check the page title")
        try:
            expect(self.product_page_title).to_have_text(ho.PAGE_TITLE)
            return True
        except Exception as e:
            self.logger.error(f"Can not open inventory page: {e}")
            self.base_page.attach_screenshot("Open inventory page fail")
            return False

    def are_product_images_visible(self):
        self.logger.info("check the product image is visible")
        count = self.product_image_list.count()
        if count == 0:
            self.logger.warning("No product images found on the page.")
            return False
        for i in range(count):
            image = self.product_image_list.nth(i)
            try:
                expect(image).to_be_visible(timeout=5000)
            except Exception as e:
                self.logger.error(f"Image at index {i} is not visible: {e}")
                return False
        return True
    
    def are_product_images_valid(self):
        self.logger.info("check the product image is valid")
        count = self.product_image_list.count()
        for i in range(count):
            image = self.product_image_list.nth(i)
            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            if not src or not src.strip():
                self.logger.error(f"image at index {i} has empty 'src'")
                return False
            if not alt or not alt.strip():
                self.logger.error(f"image at index {i} has empty 'alt'")
                return False
        self.logger.info(f"All {count} have valid 'src' and 'alt'")
        return True    

    def get_product_name(self):
        self.logger.info("Getting product names")
        return self.product_name_list.all_text_contents()

    def get_product_price(self):
        self.logger.info("Getting product prices")
        prices = self.product_price_list.all_text_contents()
        return [float(price.replace('$', '').strip()) for price in prices]

    def select_sorting_order_option(self, option):
        self.logger.info(f"Selecting option: {option}")
        self.product_sort_dropdown.select_option(label=option)

    def is_sort_by_name_desc(self):
        self.logger.info("Verifying product sort Z to A")
        try:
            expect(self.active_option).to_have_text("Name (Z to A)")
            names = self.get_product_name()
            expected = sorted(names, reverse=True)
            self.logger.info(f"Actual: {names}, Expected: {expected}")
            if names != expected:
                self.base_page.attach_screenshot("Sort_Z_to_A_Fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Sort verification failed: {e}")
            self.attach_screenshot("Sort_Z_to_A_Fail")
            return False
        
    def is_sort_by_name_asc(self):
        self.logger.info("Verifying product sort A to Z")
        try:
            expect(self.active_option).to_have_text("Name (A to Z)")
            names = self.get_product_name()
            expected = sorted(names)
            self.logger.info(f"Actual: {names}, Expected: {expected}")
            if names != expected:
                self.base_page.attach_screenshot("Sort_A_to_Z_Fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Sort verification failed: {e}")
            self.base_page.attach_screenshot("Sort_A_to_Z_Fail")
            return False

    def is_sort_by_price_asc(self):
        self.logger.info("Verifying product sor t Low to High")
        try:
            expect(self.active_option).to_have_text("Price (low to high)")
            prices = self.get_product_price()
            expected = sorted(prices)
            self.logger.info(f"Actual: {prices}, Expected: {expected}")
            if prices != expected:
                self.base_page.attach_screenshot("Sort_Low_to_High_Fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Sort verification failed: {e}")
            self.base_page.attach_screenshot("Sort_Low_to_High_Fail")
            return False

    def is_sort_by_price_desc(self):
        self.logger.info("Verifying product sort High to Low")
        try:
            expect(self.active_option).to_have_text("Price (high to low)")
            prices = self.get_product_price()
            expected = sorted(prices, reverse=True)
            self.logger.info(f"Actual: {prices}, Expected: {expected}")
            if prices != expected:
                self.base_page.attach_screenshot("Sort_High_to_Low_Fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Sort verification failed: {e}")
            self.base_page.attach_screenshot("Sort_High_to_Low_Fail")
            return False
        
    def click_product_image(self, option):
        self.logger.info(f"Click on {option} image")
        self.page.get_by_alt_text(option).click()

    def is_add_to_cart_button_display(self, product_name):
        self.logger.info("Check add to cart button is displayed")
        add_to_cart_button = self.base_page.locator_add_to_cart_button_inventory(product_name)
        try:
            self.is_inventory_page_open()
            expect(add_to_cart_button).to_be_visible()
            return True
        except Exception as e:
            self.logger.error(f"Add to cart button is not displayed: {e}")
            self.base_page.attach_screenshot("Add to cart not found")
            return False        

    def click_add_product_to_cart(self, product_name):
        self.logger.info("Click Add to cart button")
        add_to_cart_button = self.base_page.locator_add_to_cart_button_inventory(product_name)
        add_to_cart_button.click()

    def is_remove_button_display(self, product_name):
        self.logger.info("Check remove button is displayed")
        remove_button = self.base_page.locator_remove_button_inventory(product_name)
        try:
            expect(remove_button).to_be_visible()
            return True
        except Exception as e:
            self.logger.error(f"Remove button is not displayed: {e}")
            self.base_page.attach_screenshot("Remove not found")
            return False    

    def click_remove_product_from_inventory(self, product_name):
        self.logger.info("Click Remove button")
        remove_button = self.base_page.locator_remove_button_inventory(product_name)
        remove_button.click()

    def get_cart_badge_count(self):
        self.logger.info("Get the number of the cart")
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0
    
    def is_cart_badge_count_correct(self, expect_count):
        self.logger.info("Verify the cart badge count is correct")
        try:
            actual_count = self.get_cart_badge_count()
            expected_number = int(expect_count)
            self.logger.info(f"Actual: {actual_count}, Expected: {expected_number}")
            if actual_count != expected_number:
                self.base_page.attach_screenshot("Add to card fail")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Can not add to product to cart: {e}")
            self.base_page.attach_screenshot("Add to card fail")
            return False

    def is_cart_badge_not_displayed(self):
        self.logger.info("Verify the cart badge count is disappear") 
        try:
            expect(self.cart_badge).to_have_count(0)
            return True
        except Exception as e:
            self.logger.error(f"Can not remove product from cart: {e}")
            self.base_page.attach_screenshot("Remove fail")
            return False
   



