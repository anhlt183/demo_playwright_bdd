import os
from utils.logger import get_logger
from playwright.sync_api import Page, expect
from pages.locators import complete_locators as co
from pages.base_page import BasePage

class CompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()
        self.base_page = BasePage(page)

        # Complete Page Elements
        self.complete_page_title = page.locator(co.COMPLETE_PAGE_TITLE)
        self.complete_message = page.locator(co.COMPLETE_MESSAGE)
        self.cancel_button = page.locator(co.CANCEL_BUTTON)

    def is_complete_page_open(self):
        self.logger.info("check the complete page is opened")
        try:
            expect(self.complete_page_title).to_have_text(co.PAGE_TITLE)
            return True
        except Exception as e:
            self.logger.error(f"Can not navigate to complete page: {e}")
            self.base_page.attach_screenshot("Navigate complete page fail")
            return False
        
    def is_successfull_message_display(self):
        self.logger.info("check the successfull message is displayed")
        try:
            self.is_complete_page_open()
            expect(self.complete_message).to_have_text(co.MESSAGE)
            return True
        except Exception as e:
            self.logger.error(f"can not finish the check out: {e}")
            self.base_page.attach_screenshot("finish checkou fail")
            return False
        
    def click_cancel_button(self):
        self.logger.info("click on Cancel button")
        self.cancel_button.click()

