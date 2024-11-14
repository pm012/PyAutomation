import logging

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class ExceptionsPage(BasePage):
    _logger = logging.getLogger(__name__)
    __url_exceptions = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row1_input_locator = (By.XPATH, "//div[@id='row1']/input")
    __row2_input_locator = (By.XPATH, "//div[@id='row2']/input")
    __save_button_row1_locator = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __save_button_row2_locator = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __save_confirmation_message = (By.ID, 'confirmation')
    __edit_btn = (By.ID, "edit_btn")
    __instructions_locator = (By.ID, "instructions")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _open(self):
        super()._open_url(self.__url_exceptions)
        self._logger.info(f"Page opened: {self.__url_exceptions}")

    def _add_btn_click(self):
        self._find(self.__add_button_locator).click()
        self._logger.info("Add button is clicked")
        super()._wait_until_element_is_visible(self.__row2_input_locator)

    def _get_confirmation_message(self) -> str:
        super()._wait_until_element_is_visible(self.__save_confirmation_message)
        return super()._get_text(self.__save_confirmation_message)

    def _verify_row2_input_is_displayed(self) -> bool:
        row2_input_el = super()._find(self.__row2_input_locator)
        return row2_input_el.is_displayed()

    def _verify_instructions_are_not_shown(self) -> bool:
        return super()._is_displayed(self.__instructions_locator)

    def _set_text_to_row2_input(self, txt: str):
        super()._type(self.__row2_input_locator, txt)
        super()._click(self.__save_button_row2_locator)
        super()._wait_until_element_is_visible(self.__save_confirmation_message)

    def _modify_row1_input(self, txt: str):
        super()._click(self.__edit_btn)
        # Comment out the 2 rows above to get InvalidElementStateException
        super()._wait_until_element_is_clickable(self.__row1_input_locator)
        super()._clear(self.__row1_input_locator)
        super()._type(self.__row1_input_locator, txt)
        super()._click(self.__save_button_row1_locator)
        super()._wait_until_element_is_visible(self.__save_confirmation_message)

        self._logger.info("The row 1 field is cleared")

    def _get_row1_input_value(self)->str:
        row2_input_val = super()._get_attribute_value(self.__row1_input_locator, "value")
        self._logger.info(f"The text in the input is {row2_input_val}")
        return row2_input_val


        
    
    

