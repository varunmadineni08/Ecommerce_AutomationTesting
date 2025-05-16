from selenium.webdriver.common.by import By

from pages.Basepage import BasePage
from pages.Homepage import HomePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    username_id="user-name"
    password_id="password"
    login_button_id="login-button"
    validation_title_class="title"
    invalid_warning_xpath="//div[contains(@class,'error-message-container')]"
    empty_credentials_warning_xpath="//div[contains(@class,'error-message-container')]"



    def enter_username(self,username):
        self.enter_text(username,"username_id",self.username_id)
        # self.driver.find_element(By.ID,self.username_id).clear()
        # self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def enter_password(self,password):
        self.enter_text(password, "password_id", self.password_id)
        # self.driver.find_element(By.ID,self.password_id).clear()
        # self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def click_login_button(self):
        self.click_element("login_button_id",self.login_button_id)
        # self.driver.find_element(By.ID,self.login_button_id).click()
        return HomePage(self.driver)

    def check_loggined(self):
        return self.display_status("validation_title_class",self.validation_title_class)
        # return self.driver.find_element(By.CLASS_NAME,self.validation_title_class).is_displayed()

    def invalid_warning_msg(self):
        return self.display_status("invalid_warning_xpath", self.invalid_warning_xpath)
        # return self.driver.find_element(By.XPATH,self.invalid_warning_xpath).is_displayed()

    def empty_credentials_warning(self):
        return self.display_status("empty_credentials_warning_xpath", self.empty_credentials_warning_xpath)
        # return self.driver.find_element(By.XPATH,self.empty_credentials_warning_xpath).is_displayed()

    def enter_details(self,username,password):
        self.enter_username(username)
        self.enter_password(password)


