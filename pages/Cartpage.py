from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Checkoutpage import CheckoutPage


class CartPage:
    def __init__(self,driver):
        self.driver=driver

    checkout_button_id='checkout'

    def click_checkout_button(self):
        self.driver.find_element(By.ID,self.checkout_button_id).click()
        return CheckoutPage(self.driver)

