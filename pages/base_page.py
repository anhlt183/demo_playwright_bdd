import os
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from datetime import datetime
from pages.locators import base_locators as ba
from pages.locators import home_locators as ho
from pages.locators import cart_locators as ca

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

    #attach screenshot
    def attach_screenshot(self, name="Screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        path = os.path.join("screenshots", filename)
        self.page.screenshot(path=path)
        print(f"[Saved Screenshot] {path}")     

    #define locator of add to cart button on inventory page  
    def locator_add_to_cart_button_inventory(self, product_name):
        slug = ba.PRODUCT_SLUGS.get(product_name)
        if not slug:
            raise ValueError(f"Product name '{product_name}' không có trong PRODUCT_SLUGS")
        return self.page.locator(ho.ADD_TO_CART_BUTTON.format(slug))
    
    #define locator of remove button on inventory page
    def locator_remove_button_inventory(self, product_name):
        slug = ba.PRODUCT_SLUGS.get(product_name)
        if not slug:
            raise ValueError(f"Product name '{product_name}' không có trong PRODUCT_SLUGS")
        return self.page.locator(ho.REMOVE_BUTTON.format(slug))
    
    #define locator of remove button on inventory page
    def locator_remove_button_cart(self, product_name):
        slug = ba.PRODUCT_SLUGS.get(product_name)
        if not slug:
            raise ValueError(f"Product name '{product_name}' không có trong PRODUCT_SLUGS")
        return self.page.locator(ca.REMOVE_BUTTON.format(slug))
