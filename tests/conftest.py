
import pytest
from selenium import webdriver

from utils.Logs import generate_logs

from configurations import Readconfigurations

@pytest.fixture(scope="function", autouse=True)
def logger():
    logger = generate_logs()
    logger.info("==== Test Session Started ====")
    yield logger
    logger.info("==== Test Session Finished ====")

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