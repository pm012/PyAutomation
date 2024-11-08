import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
    def test_no_such_element_exception(self, driver):
        # Test case 1: NoSuchElementException
        # 1. Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        logger.info("Page opened: https://practicetestautomation.com/practice-test-exceptions/")

        # 2. Click Add button
        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()
        logger.info("Add button clicked")

        wait = WebDriverWait(driver, 10) 
        # Excplicit wait
        row2_input_el = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@id='row2']/input"))) # provide locator as tuple

        # 3. Verify Row 2 input field is displayed                
        assert row2_input_el.is_displayed(), "Row 2 should be displayed, but it's not"

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

    #@pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Test case 2: ElementNotInteractableException
        # 1. Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        logger.info("Page opened: https://practicetestautomation.com/practice-test-exceptions/")

        # 2. Click Add button
        add_button = driver.find_element(By.ID, "add_btn")
        add_button.click()
        logger.info("Add button clicked")

        # 3 Wait for the second input field
        wait = WebDriverWait(driver, 20)        
        row2_input = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@id='row2']/input"))) # provide locator as tuple

        # 4. Type text into the second input field
        row2_input.send_keys("some text")

        # 5. Push Save button using locator By.name("Save")
        driver.find_element(By.NAME, "Save").clik()
        
        # 6. Verify text is saved
        message_el = driver.find_element(By.ID, 'confirmation')
        assert message_el.text == 'Row 2 was saved', "Confirmation message is not as it expected"
        

        
        