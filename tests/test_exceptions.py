import pytest
import logging
from tests.page_objects.exceptions_page import ExceptionsPage

logger = logging.getLogger(__name__)

class TestExceptions:
    """
Exceptions Homework 1.
Test case 1: NoSuchElementException

    1. Open page
    2. Click Add button
    3. Verify Row 2 input field is displayed

Row 2 doesn’t appear immediately. This test will fail with org.openqa.selenium.NoSuchElementException without proper wait"""

    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_no_such_element_exception(self, driver):
        # Test case 1: NoSuchElementException
        # 1. Open page
        exceptions_page = ExceptionsPage(driver)
        exceptions_page._open()

        # 2. Click Add button
        exceptions_page._add_btn_click()
        logger.info("Add button clicked")

        # 3. Verify Row 2 input field is displayed                
        assert exceptions_page._verify_row2_input_is_displayed(), "Row 2 should be displayed, but it's not"

    """Test case 2: ElementNotInteractableException

    1. Open page
    2. Click Add button
    3. Wait for the second row to load
    4. Type text into the second input field
    5. Push Save button using locator By.name(“Save”)
    6. Verify text saved

This page contains two elements with attribute name=”Save”.
The first one is invisible. So when we are trying to click on the invisible element, we get ElementNotInteractableException.

The same action used to throw ElementNotVisibleException, but now it throws a different exception (not sure if it’s a bug in Selenium or a feature)"""

    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Test case 2: ElementNotInteractableException
        # 1. Open page
        exceptions_page = ExceptionsPage(driver)
        exceptions_page._open()

        # 2. Click Add button
        exceptions_page._add_btn_click()
        logger.info("Add button clicked")

        # 3. Verify Row 2 input field is displayed
        exceptions_page._verify_row2_input_is_displayed()

        # 4. Type text into the second input field
        # 5. Push Save button using locator By.name("Save")
        exceptions_page._set_text_to_row2_input("Text to row2 input")

        # 6. Verify text is saved
        assert exceptions_page._get_confirmation_message() == "Row 2 was saved", "Confirmation message is incorrect"

    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        # Test case 3: InvalidElementStateException
        # 1. Open page
        exceptions_page = ExceptionsPage(driver)
        exceptions_page._open()

        # 2. Clear input
        # 3 Type text into the input1 field
        exceptions_page._modify_row1_input("Text for input1")

        # 4. Verify that text has been changed
        input_text = exceptions_page._get_row1_input_value()
        assert input_text == "Text for input1", "The text was not changed"

        #5 Click Save button and verify that text was saved.
        assert exceptions_page._get_confirmation_message() == "Row 1 was saved", "Confirmation message is incorrect"

    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_stale_element_exception(self, driver):
            # Test case 4: StaleElementException
            # 1. Open page
            exceptions_page = ExceptionsPage(driver)
            exceptions_page._open()

            # 2. Find the instructions text element (id=instructions)
            # 3 Press add button
            exceptions_page._add_btn_click()

            # 4. Verify instructions text element is no longer displayed
            assert not exceptions_page._verify_instructions_are_not_shown(), "Instruction text element should not be displayed"
            
            
    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
            # Test case 5: InvalidElementStateException
            # 1. Open page
            exceptions_page = ExceptionsPage(driver)
            exceptions_page._open()

            # 2. Click Add button
            exceptions_page._add_btn_click()

            # 3. Wait for 3 seconds for the second input field to be displayed
            # 4. Verify second input field is displayed
            assert  exceptions_page._verify_row2_input_is_displayed(), "Row 2 input should be displayed, but it's not"

        