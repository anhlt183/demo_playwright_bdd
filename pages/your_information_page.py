import os
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import your_information_locators as yo
from config.config import Config
from pages.base_page import BasePage

class InformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()
        self.base_page = BasePage(page)
        
    # locator
        self.firstname_field = page.get_by_placeholder(yo.FIRSTNAME_FIELD)
        self.lastname_field = page.get_by_placeholder(yo.LASTNAME_FIELD)
        self.zip_field = page.get_by_placeholder(yo.ZIP_FIELD)
        self.continue_button = page.locator(yo.CONTINUE_BUTTON)

    def navigate_to_your_information_page(self):
        self.logger.info(f"Navigating to your information page")
        try:
            expect(self.firstname_field).to_be_visible()
            return True
        except Exception as e:
            self.logger.error(f"Can not open your information page: {e}")
            self.base_page.attach_screenshot("Open your information fail")
            return False
        
    def enter_firstname(self, firstname):
        self.logger.info(f"Entering username: {firstname}")
        self.firstname_field.fill(firstname)

    def enter_lastname(self, lastname):
        self.logger.info(f"Entering lastname: {lastname}")
        self.lastname_field.fill(lastname) 

    def enter_zip(self, zip):
        self.logger.info(f"Entering lastname: {zip}")
        self.zip_field.fill(zip)

    def click_continue_button(self):
        self.logger.info("click Continue button")
        self.continue_button.click()


