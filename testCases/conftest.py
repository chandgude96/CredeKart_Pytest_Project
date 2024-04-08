import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

### add argument
def pytest_addoption(parser):
    parser.addoption("--browser")

### passing the value to --browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# here we passing actual value to --browser
@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("headlessmode")
        chrome_options = webdriver.ChromeOptions
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)



    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://automation.credence.in")
    return driver













def pytest_metadata(metadata):
    metadata["Class"] = "Credence"           ##### to add
    metadata["Batch"] = "ct15"
    metadata["URL"] = "https://automation.credence.in/login"
    metadata.pop("Platform", None) ######### to remove
    metadata["Name"] = "Nikhil"
    metadata["Middle Name"] = "Ashok"
    metadata["Surname"] = "Chandgude"
    metadata.pop("Batch", None)


#### How to edit summery in your report
@pytest.fixture(params=[
    ("Credence@1test.com","Credence@9656"),
    ("Credence@1test.com","Credence@1256"),
    ("Credence@234test.com","Credence@9656"),
    ("Credence@3test.com","Credence@5556")
])
def getDataforLogin(request):
    return request.param








