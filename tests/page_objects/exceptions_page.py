import logging

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

class ExceptionsPage(BasePage):
    _logger = logging.getLogger(__name__)
    __url_exceptions = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row2_input_locator = (By.XPATH, "//div[@id='row2']/input")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    def _open(self):
        super()._open_url(self.__url_exceptions)
        self._logger.info(f"Page opened: {self.__url_exceptions}")

    def _add_btn_click(self):
        self._find(self.__add_button_locator).click()
        self._logger.info("Add button is clicked")
        super()._wait_until_element_is_visible(self.__row2_input_locator)


    def _verify_row2_input_is_displayed(self):        
        row2_input_el = super()._find(self.__row2_input_locator)
        assert row2_input_el.is_displayed(), "Row 2 should be displayed, but it's not"
        self._logger.info("Row 2 input is displayed")
        
    
    

