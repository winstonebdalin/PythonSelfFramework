from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    cardfooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutitems = (By.XPATH, "//button[@class='btn btn-success']")

    # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    # product.find_element(By.XPATH, "div/button").click()

    def getproducts(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getcardfooter(self):
        return self.driver.find_element(*CheckOutPage.cardfooter)

    def getcheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def getcheckoutitems(self):
        return self.driver.find_element(*CheckOutPage.checkoutitems)