import time
from TestCases.conftest import setup
from PageObject.Login_Page import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()  #we will use this logger obj to send msg in logs file

    def test_login_DDT(self,setup):
        self.logger.info("**************************Test_002_DDT_Login*****************************")
        self.logger.info("**********************Verifying Login DDT Test **************************")
        # self.logger.info(self.driver)
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.logger.info("***********Stop********************")
        self.lp = LoginPage(self.driver)


        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in Excel:", self.rows)

        lst_status=[]       #Empty list variable

        for r in range (2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("**********Passed***************")
                    self.lp.clickback()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("**********Failed***************")
                    self.lp.clickback()
                    lst_status.append("Fail")
            elif act_title!= exp_title:
                if self.exp=="Pass":
                    self.logger.info ("************Test is Failed*************")
                    lst_status.append("Fail")
                    self.lp.clickback()
                elif self.exp=="Fail":
                    self.logger.info("************Test is Passed*************")
                    lst_status.append("Pass")
                    self.lp.clickback()
        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info ("********Login DDT test case is passed**********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********Login DDT test case is Failed**********")
            self.driver.close()
            assert False

        self.logger.info("************End of Login DDT Test**************")
        self.logger.info("************Completed Test_002_DDT_Login**************")

