import time

from pages.Loginpage import LoginPage
from tests.Basetest import BaseTest


class TestCheckout(BaseTest):

    def test_checkoutpage(self):
        login_page = LoginPage(self.driver)
        login_page.enter_details("standard_user","secret_sauce")
        home_page=login_page.click_login_button()
        cart_page=home_page.add_items()
        checkout_page=cart_page.click_checkout_button()
        checkout_page.enter_info_and_checkout("varun","madineni","507000")
        assert checkout_page.home_app()
