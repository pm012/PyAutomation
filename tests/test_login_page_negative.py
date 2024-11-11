from selenium.webdriver.common.by import By
import pytest
import logging
from page_objects.login_page import LoginPage

logger = logging.getLogger(__name__)

class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "Password1234", "Your password is invalid!")]) # Each tuple in brackets after parameter names contains set of parameters to run the test
    def test_negative_username(self, driver, username, password, expected_error_message):
        
        # Test case 2: Negative username test
        # Open page
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)

        # Verify correct error message is 
        assert login_page.get_error_message() == expected_error_message
        
    