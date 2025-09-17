import os
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import overview_locators as ov
from pages.base_page import BasePage

class OverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()
        self.base_page = BasePage(page)

        # Overview Page Elements
        self.overview_page_title = page.locator(ov.OVERVIEW_PAGE_TITLE)
        self.product_title = page.locator(ov.PRODUCT_TITLE)
        self.finish_button = page.locator(ov.FINISH_BUTTON)

    def is_overview_page_open(self):
        self.logger.info("check the overview page is opened")
        try:
            expect(self.overview_page_title).to_have_text(ov.PAGE_TITLE)
            return True
        except Exception as e:
            self.logger.error(f"Can not open overview page: {e}")
            self.base_page.attach_screenshot("Navigate overview page fail")
            return False
        
    def is_product_correct_in_overview(self, product_name):
        self.logger.info("check the product is displayed on overview page")
        try:
            self.is_overview_page_open()
            expect(self.product_title).to_have_text(product_name)
            return True
        except Exception as e:
            self.logger.error(f"can not add product to overview page: {e}")
            self.base_page.attach_screenshot("add product overview fail")
            return False
        
    def click_finish_button(self):
        self.logger.info("click finish button")
        self.finish_button.click()
