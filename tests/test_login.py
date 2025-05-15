
from pages.Loginpage import LoginPage


class TestLogin:

    def test_login_with_valid_credentials(self,setup):
        login_page=LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert login_page.check_loggined()

    def test_with_invalid_credentials(self,setup):
        login_page = LoginPage(self.driver)
        login_page.enter_username("varun")
        login_page.enter_password("1234567")
        login_page.click_login_button()
        assert login_page.invalid_warning_msg()

    def test_without_credentials(self,setup):
        login_page = LoginPage(self.driver)
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login_button()
        assert login_page.empty_credentials_warning()

