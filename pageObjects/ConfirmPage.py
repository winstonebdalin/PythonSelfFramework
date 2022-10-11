from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    SelectCountry = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirmbutton = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    displaymsg = (By.CLASS_NAME, "alert-success")

    def getcountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getSelectCountry(self):
        return self.driver.find_element(*ConfirmPage.SelectCountry)

    def getcheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getconfirmbutton(self):
        return self.driver.find_element(*ConfirmPage.confirmbutton)

    def getdisplaymsg(self):
        return self.driver.find_element(*ConfirmPage.displaymsg)