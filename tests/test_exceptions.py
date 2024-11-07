"""
Homework 2.
Test case 1: NoSuchElementException

    1. Open page
    2. Click Add button
    3. Verify Row 2 input field is displayed

Row 2 doesn’t appear immediately. This test will fail with org.openqa.selenium.NoSuchElementException without proper wait"""
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)

class TestNoSuchElementException:

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

        # 3. Verify Row 2 input field is displayed
        try:
            row2_input = driver.find_element(By.XPATH, "//div[@id='row2']/input-example")
            driver.verify(row2_input.is_displayed())
        except NoSuchElementException:
            logger.error("Row 2 input field is not displayed")