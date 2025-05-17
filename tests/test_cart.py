import pytest

from pages.Loginpage import LoginPage
from tests.Basetest import BaseTest


class TestCart(BaseTest):

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_cart_page(self):
        login_page=LoginPage(self.driver)
        login_page.enter_details("standard_user","secret_sauce")
        home_page=login_page.click_login_button()
        cart_page=home_page.add_items() #here we added method from homepage
        cart_page.click_checkout_button()