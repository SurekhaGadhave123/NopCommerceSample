from selenium import webdriver
import pytest
from selenium.webdriver.common.service import Service


@pytest.fixture()
def setup(browser):
        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        driver.implicitly_wait(10)



def pytest_addoption(parser):           # This will get the value of browser from CLI/hooks
        parser.addoption("--browser")

@pytest.fixture()
def browser(request):           #this will return browser value to setup method
        return request.config.getoption("--browser")


# # pytest html reprot
# # It is hook for adding environment info to html report
# def pytest_configure(config):
#         config._metadata['Project Name']='NopCommerceApp'
#         config._metadata['Module Name']='Login'
#         config._metadata['Tester']='Surekha'
#
# # it is hook for delete/modify environgment info to html report
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#         metadata.pop("JAVA_HOME",None)
#         metadata.pop("Plugins",None)