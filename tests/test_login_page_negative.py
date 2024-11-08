import time

from selenium.webdriver.common.by import By
import pytest


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "Password1234", "Your password is invalid!")]) # Each tuple in brackets after parameter names contains set of parameters to run the test
    def test_negative_username(self, driver, username, password, expected_error_message):
        # Test case 2: Negative username test
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Click Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        time.sleep(2)
        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is valid
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Incorrect error message"

    def testnegative_username(self, driver):
        # Test case 2: Negative username test
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

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

    def testnegative_password(self, driver):
        # Test case 2: Negative username test
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

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
