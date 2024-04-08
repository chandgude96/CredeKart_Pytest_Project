import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Test_CredKart_Login:
    def test_page_title_001(self, setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in/")
        self.driver.maximize_window()
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\Screenshots\\test_page_title_001_pass.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_page_title_001_fail.PNG")
            self.driver.close()
            assert False


    def test_Login_002(self, setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Credence@1test.com")
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Credence@9656")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("login test is passed")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_pass.PNG")
            self.driver.close()

            assert True
        except:
            print("login test is Failed")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_fail.PNG")
            self.driver.close()
            assert False

# 100s testcase.....   if you have run it in firefox