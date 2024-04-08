import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_CredKart_Login_params:
    def test_CredKart_Login_parms_003(self, setup, getDataforLogin):

        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(getDataforLogin[0])
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(getDataforLogin[1])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("login test is passed")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_pass.PNG")
            self.driver.close()

            assert True

        except:
            print("login test is Failed")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_fail.PNG")
            self.driver.close()
            assert False




