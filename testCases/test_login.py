import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pageObjects.LoginPage import Login
from utilities.Logger import LogGenerator



class Test_CredKart_Login:
    log = LogGenerator.loggen()     ### for log import loggerator classb se loggen function #method ko call kiya hai
    def test_page_title_001(self, setup):
        self.driver = setup
        ######## Log Level Example### for ways to write messages
        self.log.debug("this is debug")
        self.log.info("this is info")
        self.log.warning("this is warning")
        self.log.error("this is error")
        self.log.critical("this is critical")

        self.log.info("stared test case test_page_title_001" )         #### give messgae
        self.log.info("Opening the browser")         ##### log sentence
        ####steps log### print replace by self.log.info
        self.driver.get("https://automation.credence.in/")

        self.driver.maximize_window()

        if self.driver.title == "CredKart":
            self.log.info("checking the page title" + self.driver.title)
            self.driver.save_screenshot(".\\Screenshots\\test_page_title_001_pass.PNG")

            self.log.info("taking the screenshots")

            self.driver.close()
            self.log.info("Testcase test_login.py  is passed")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_page_title_001_fail.PNG")
            self.log.info("taking the screenshot")

            self.driver.close()
            self.log.info("Testcase test_login.py is failed")
            assert False

        self.log.info("Testcase is completed")



    def test_Login_002(self, setup):
        self.driver = setup
        self.log.info("Opening the browser")
        self.lp = Login(self.driver)  #### class la boavale   imppppp
        # self.lp.Login_Url               ####get url link
        self.driver.get("https://automation.credence.in/login")
        # self.driver.maximize_window()

        self.lp.Enter_Email("Credence@1test.com")
        self.log.info("Entering the mail")


       # self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Credence@1test.com")
        self.lp.Enter_Password("Credence@9656")
        self.log.info("Entering the Password")
        #self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Credence@9656")
        self.lp.Click_Login_Button()
        self.log.info("click login button")

        print(self.lp.Login_Status())
        self.log.info("checking the login status")

        self.log.info("login is sucessfull")
        time.sleep(3)

        if self.lp.Login_Status() == True:
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_pass.PNG")
            self.log.info("taking the screenshots")

            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_fail.PNG")
            assert False
        self.log.info("Testcase is completed")

        #self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

        #
        # if self.lp.login_Status() == True:
        #     self.driver.save_screenshot(".\\Screenshots\\test_Login_002_pass.PNG")
        #     assert True
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\test_Login_002_pass.PNG")
        #     assert False

        #
        # try:
        #     self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
        #     print("login test is passed")
        #     self.driver.save_screenshot(".\\Screenshots\\test_Login_002_pass.PNG")
        #     self.driver.close()
        #
        #     assert True
        # except:
        #     print("login test is Failed")
        #     self.driver.save_screenshot(".\\Screenshots\\test_Login_002_fail.PNG")
        #     self.driver.close()
        #     assert False

# 100s testcase.....   if you have run it in firefox