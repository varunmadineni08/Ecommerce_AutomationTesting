import pytest
from selenium import webdriver

@pytest.fixture()

def setup(request):
    driver=None
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()