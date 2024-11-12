import logging

from selenium.webdriver.common.by import By

from tests.page_objects.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class ExceptionsPage(BasePage):
    _logger = logging.getLogger(__name__)
    __url_exceptions = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _open(self):
        super()._open_url(self.__url_exceptions)
        self._logger.info("Page opened: https://practicetestautomation.com/practice-test-exceptions/")

    def _add_btn_click(self, driver: WebDriver):
        self._find(self.__add_button_locator).click()
        self._logger.info("Add button is clicked")



    def _verify_row2_input_is_displayed(self):
        pass

