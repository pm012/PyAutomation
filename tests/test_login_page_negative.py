import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    def testnegative_username(self):
        # Test case 2: Negative username test

        # Init webdriver
        driver = webdriver.Chrome()

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        usename_locator = driver.find_element(By.ID, "username")
        usename_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Click Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        time.sleep(2)
        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is valid
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Incorrect error message"

    @pytest.mark.login
    @pytest.mark.negative
    def testnegative_password(self):
        # Test case 2: Negative username test

        # Init webdriver
        driver = webdriver.Chrome()

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        usename_locator = driver.find_element(By.ID, "username")
        usename_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password1234")

        # Click Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        time.sleep(2)
        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is valid
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Incorrect error message"