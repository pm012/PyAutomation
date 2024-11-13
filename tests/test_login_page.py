import pytest
from page_objects.login_page import LoginPage
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage

class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        # navigate to webpage
        login_page.open()        
        # Type username to Username input
        # Type password
        # Click Submit button
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)        
        
        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/        
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        
        # Verify new page contains expected text ('Congratulations' or successfully
        assert logged_in_page.header == "Logged In Successfully", "Header is not as expected"

        # Verify Log out button is present on new page
        assert logged_in_page.is_logout_button_displayed(), "Log out button was not displayed"
        
