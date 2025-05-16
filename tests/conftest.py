
import pytest
from selenium import webdriver

from configurations import Readconfigurations


@pytest.fixture()

def setup(request):
    driver=None
    browser=Readconfigurations.read_config("info","browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver=webdriver.Edge()
    elif browser == "firefox":
        driver=webdriver.Firefox()
    else:
        raise Exception(f"enter valid browser")

    url=Readconfigurations.read_config("info","url")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()