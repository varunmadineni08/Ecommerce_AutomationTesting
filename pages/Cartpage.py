from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self,driver):
        self.driver=driver

    checkout_button_id="checkout"

    # def verify_cart_items(self):
    #     wait=WebDriverWait(self.driver,10)
    #     return wait.until(EC.visibility_of_element_located((By.ID,self.cart_list_id))).is_displayed()


    def click_checkout_button(self):
        self.driver.find_element(By.ID,self.checkout_button_id).click()

