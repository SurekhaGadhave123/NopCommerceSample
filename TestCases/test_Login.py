from PageObject.Login_Page import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()  #we will use this logger obj to send msg in logs file

    def test_homePageTitle(self, setup):
        self.logger.info("**********************Test_001_Login********************")
        self.logger.info("**********************Verify Home Page Title********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********************Home Page Title test is passed ********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**********************Home Page Title test is failed ********************")
            assert False

    def test_login(self, setup):
        self.logger.info("**********************Verifying Login Test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**********************Login Test is Passed********************")
            self.driver.close()
        else:

            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("**********************Login Test is failed********************")
            assert False