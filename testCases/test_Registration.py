import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_CredKart_Login:
    def test_page_title_001(self):
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/")
        driver.maximize_window()
        if driver.title == "CredKart":
            assert True
        else:
            assert False

    def test_Login_002(self):
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/login")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Credence@1test.com")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Credence@9656")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("login test is passed")
            assert True
        except:
            print("login test is Failed")
            assert False
