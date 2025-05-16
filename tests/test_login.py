
from pages.Loginpage import LoginPage
from tests.Basetest import BaseTest


class TestLogin(BaseTest):

    def test_login_with_valid_credentials(self):
        login_page=LoginPage(self.driver)
        login_page.enter_details("standard_user","secret_sauce")
        login_page.click_login_button()
        assert login_page.check_loggined()

    def test_with_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.enter_details("varun", "1234567")
        login_page.click_login_button()
        assert login_page.invalid_warning_msg()

    def test_without_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.enter_details("", "")
        login_page.click_login_button()
        assert login_page.empty_credentials_warning()

