from selenium import webdriver
import pytest
from util import config_util 



@pytest.fixture(autouse=True, scope="function")
def setup_teardown(request: pytest.FixtureRequest):

    brows = config_util.read_config('basic info', 'browser')
    if brows == "chrome":
        driver = webdriver.Chrome()
    elif brows == "firefox":
        driver = webdriver.Firefox()
    elif brows == "edge":
        driver = webdriver.Edge()
    else:
        print("This is not a valid browser name")
    driver.maximize_window()
    ur = config_util.read_config('basic info', 'url')
    driver.get(ur)
    request.cls.driver = driver
    yield
    driver.quit()
