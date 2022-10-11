from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self, setup):

        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        confirmpage = ConfirmPage(self.driver)

        products = checkoutpage.getproducts()
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            print(productName)
            if productName == 'Blackberry':
                checkoutpage.getcardfooter().click()

        checkoutpage.getcheckout().click()
        checkoutpage.getcheckoutitems().click()
        confirmpage.getcountry().send_keys("ind")

        self.verifyLinkPresence("India")
        confirmpage.getSelectCountry().click()

        confirmpage.getcheckbox().click()
        confirmpage.getconfirmbutton().click()
        #sucessText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        sucessText = confirmpage.getdisplaymsg().text
        assert "Success! Thank you!" in sucessText
