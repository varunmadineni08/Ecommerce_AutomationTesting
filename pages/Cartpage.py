from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Basepage import BasePage
from pages.Checkoutpage import CheckoutPage


class CartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    checkout_button_id='checkout'

    def click_checkout_button(self):
        self.click_element("checkout_button_id",self.checkout_button_id)
        # self.driver.find_element(By.ID,self.checkout_button_id).click()
        return CheckoutPage(self.driver)

