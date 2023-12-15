import time

import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # navigate to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type usename to Username input
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # click Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button.click()
        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        url = driver.current_url
        assert url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page conains expected text ('Congratulations' or successfully
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify Log out button is present on new page
        log_out_btn = driver.find_element(By.XPATH, "//a[text() = 'Log out']")
        assert log_out_btn.is_displayed()
