import pytest

from pages.Homepage import HomePage
from pages.Loginpage import LoginPage
from tests.Basetest import BaseTest


class TestHome(BaseTest):

    def test_home(self):
        login_page=LoginPage(self.driver)
        login_page.enter_details("standard_user","secret_sauce")
        home_page=login_page.click_login_button()
        home_page.add_items()
        assert home_page.cart_validation()

