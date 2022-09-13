import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from PageObject.Login_Page import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen

@allure.severity(allure.severity_level.NORMAL) #decorators at class level to add severity
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()  #we will use this logger obj to send msg in logs file

    @allure.severity(allure.severity_level.MINOR)
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
        else:
            assert False
        self.driver.close()


    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False


