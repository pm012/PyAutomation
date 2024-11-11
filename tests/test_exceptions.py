import pytest
import logging
from selenium.webdriver.common.by import By
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
        row2_input_el = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@id='row2']/input")))[0] # provide locator as tuple

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

    @pytest.mark.exceptions    
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
        row2_input = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@id='row2']/input")))[0] # provide locator as tuple
        
        # 4. Type text into the second input field
        row2_input.send_keys("some text")

        # 5. Push Save button using locator By.name("Save")
        # driver.find_element(By.NAME, "Save").click() # to get element not interractible because the element is duplicated with the first row button
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()
        
        # 6. Verify text is saved
        message_el = wait.until(ec.visibility_of_element_located((By.ID, 'confirmation')))
        #driver.find_element(By.ID, 'confirmation')
        logger.info(message_el.text)
        assert message_el.text == 'Row 2 was saved', "Confirmation message is not as it expected"

    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        # Test case 3: InvalidElementStateException
        # 1. Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        logger.info("Page opened: https://practicetestautomation.com/practice-test-exceptions/")

        # 2. Clear input 
        row1_edit_btn = driver.find_element(By.ID, "edit_btn") # Comment out these 2 rows to get InvalidElementStateException
        row1_edit_btn.click()

        row1_field_el = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 20)        
        row2_input = wait.until(ec.element_to_be_clickable(row1_field_el))

        
        row1_field_el.clear()
        logger.info("The field is cleared")
        

        # 3 Type text into the input field
        row1_field_el.send_keys("Sandwich")
        
        # 4. Verify that text has been changed
        input_text = row1_field_el.get_attribute("value")
        logger.info(f"The text in the input is {input_text}")
        assert input_text == "Sandwich", "The text was not changed"

        #5 Click Save button and verify that text was saved.
        row1_save_btn = driver.find_element(By.ID,"save_btn")
        row1_save_btn.click()

        confirmation_message = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_text = confirmation_message.text
        assert confirmation_text == "Row 1 was saved", "Confirmation message is incorrect"


    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
            # Test case 3: InvalidElementStateException
            # 1. Open page
            driver.get("https://practicetestautomation.com/practice-test-exceptions/")
            logger.info("Page opened: https://practicetestautomation.com/practice-test-exceptions/")

            # 2. Find the instructions text element (id=instructions) 
            #instructions_el = driver.find_element(By.ID, "instructions")            # we don't need it with wait
            

            # 3 Press add button
            add_btn = driver.find_element(By.ID, "add_btn")
            add_btn.click()
            
            
            # 4. Verify instructions text element is no longer displayed
            # To avoid stale element exception the element absense should be checked using waits
            wait = WebDriverWait(driver, 10)
            assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")), "Instructions are present") # invisibility_of_element() will result the same stale element exception
            # assert not instructions_el.is_displayed(), "Instructions are present" #-will result in stale element exeption
            
            
    #@pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
            # Test case 3: InvalidElementStateException
            # 1. Open page
            driver.get("https://practicetestautomation.com/practice-test-exceptions/")
            logger.info("Page opened: https://practicetestautomation.com/practice-test-exceptions/")


            # Click Add button
            add_btn = driver.find_element(By.ID, "add_btn")
            add_btn.click()
            

            # Wait for 3 seconds for the second input field to be displayed
            wait = WebDriverWait(driver, 6)        # to get timeout exception use wait = WebDriverWait(driver, 3)        
        
            # Verify second input field is displayed
            row2_input = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@id='row2']/input")))[0] # provide locator as tuple
        

        
        