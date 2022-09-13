from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,"Email").clear()
        self.driver.find_element(By.ID,"Email").send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,"Password").clear()
        self.driver.find_element(By.ID,"Password").send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,"Logout").click()