from pages.Homepage import HomePage
from pages.Loginpage import LoginPage


class TestHome:

    def test_home(self,setup):
        login_page=LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        home_page=HomePage(self.driver)
        home_page.click_add_item__01()
        home_page.click_add_item_02()
        home_page.click_cart_box()
        assert home_page.cart_validation()

