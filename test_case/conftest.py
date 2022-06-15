import pytest,time
from selenium import webdriver
from selenium.webdriver import ChromeOptions

@pytest.fixture(scope="session")
def wd():
    option = ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    wd = webdriver.Chrome(options=option)  # avoid check
    wd.maximize_window()
    wd.get("https://www.baidu.com")
    time.sleep(5)

    yield wd
    wd.quit()
