###DDT

import pytest
from pageObjects.LoginPage import Login
from utilities.Logger import LogGenerator
from utilities import XLutils


class Test_CredKart_Login_DDT:
    XlPath = "C:\\Users\nikhi\\PycharmProjects\\CredeKart_Pytest_Project\\Testdata\\TestLogin.xlsx"


    def test_CredKart_Login_ddt_006(self, setup):
        self.driver = setup  ###3 browser open
        self.lp = Login(self.driver)
        self.lp.Login_URL()     ###linnk

        self.row = XLutils.RowCount(self.XlPath,"Sheet1")  ## file and sheetname  EXCEL sheet count
        print("Number of rows in excel is" + str(self.row))

        for r in range(2,self.row + 1):
            self.email = XLutils.ReadData(self.XlPath,"sheet1", r, 2)  ## fix column
            self.password = XLutils.ReadData(self.XlPath,"Sheet1",  r, 3)
            self.exp_result = XLutils.ReadData(self.XlPath,"sheet1",  r,4)







        self.lp.Enter_Email(self.email)    ###enter sel.email "Credence@1test.com"

        self.lp.Enter_Password(self.password)
        self.lp.Click_Login_Button()
        if self.lp.Login_Status() == True:
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_pass.PNG")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_fail.PNG")
            assert False



