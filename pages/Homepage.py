from selenium.webdriver.common.by import By

from pages.Cartpage import CartPage


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    add_item_01_id="add-to-cart-sauce-labs-backpack"
    add_item_02_id="add-to-cart-sauce-labs-bike-light"
    cart_box_id="shopping_cart_container"
    validation_cart="title"

    def click_add_item__01(self):
        self.driver.find_element(By.ID,self.add_item_01_id).click()

    def click_add_item_02(self):
        self.driver.find_element(By.ID,self.add_item_02_id).click()

    def click_cart_box(self):
        self.driver.find_element(By.ID,self.cart_box_id).click()
        return CartPage(self.driver)

    def cart_validation(self):
        return self.driver.find_element(By.CLASS_NAME,self.validation_cart).is_displayed()

    def add_items(self):
        self.click_add_item__01()
        self.click_add_item_02()
        self.click_cart_box()
        return CartPage(self.driver)











