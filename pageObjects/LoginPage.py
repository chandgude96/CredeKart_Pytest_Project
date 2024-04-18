import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    Login_URL = "https://automation.credence.in/login"                ### variables
    Text_Email_XPATH = (By.XPATH, "//input[@id='email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='password']")
    Click_Login_Button_XPATH = (By.XPATH,"//button[@type='submit']")
    login_Status = (By.XPATH,"//h2[normalize-space()='CredKart']")


    def __init__(self,driver):           #### constructors
        self.driver = driver

    def Login_Url(self):
        self.driver.get(*Login.Login_Url)

    def Enter_Email(self, email):

        self.driver.find_element(*Login.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Login.Text_Password_XPATH).send_keys(password)  #### call krne only click

    def Click_Login_Button(self):
        self.driver.find_element(*Login.Click_Login_Button_XPATH).click()

    def Login_Status(self):
        time.sleep(3)
        try:
            self.driver.find_element(*Login.login_Status)
            return True
        except:
            return False




