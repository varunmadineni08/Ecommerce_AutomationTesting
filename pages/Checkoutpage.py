from selenium.webdriver.common.by import By

from pages.Basepage import BasePage


class CheckoutPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    first_id="first-name"
    last_id="last-name"
    zipcode_id="postal-code"
    continue_button_id="continue"
    finish_button_id="finish"
    backhome_button_id="back-to-products"
    home_coming_class="app_logo"

    def enter_firstname(self,firstname):
        # self.driver.find_element(By.ID, self.firstname_id).clear()
        self.enter_text(firstname,"first_id",self.first_id)
        # self.driver.find_element(By.ID,self.firstname_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        # self.driver.find_element(By.ID, self.lastname_id).clear()
        self.enter_text(lastname,"last_id", self.last_id)
        # self.driver.find_element(By.ID,self.lastname_id).send_keys(lastname)

    def enter_zipcode(self,zipcode):
        self.driver.find_element(By.ID,self.zipcode_id).clear()
        self.enter_text(zipcode, "zipcode_id", self.zipcode_id)
        # self.driver.find_element(By.ID,self.zipcode_id).send_keys(zipcode)

    def click_continue(self):
        self.click_element("continue_button_id",self.continue_button_id)
        # self.driver.find_element(By.ID,self.continue_button_id).click()

    def click_finish(self):
        self.click_element("finish_button_id", self.finish_button_id)
        # self.driver.find_element(By.ID,self.finish_button_id).click()

    def click_backhome(self):
        self.click_element("backhome_button_id", self.backhome_button_id)
        # self.driver.find_element(By.ID,self.backhome_button_id).click()

    def home_app(self):
        return self.display_status("home_coming_class",self.home_coming_class)
        # return self.driver.find_element(By.CLASS_NAME,self.home_coming_class).is_displayed()

    def enter_info_and_checkout(self,firstname,lastname,zipcode):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_zipcode(zipcode)
        self.click_continue()
        self.click_finish()
        self.click_backhome()