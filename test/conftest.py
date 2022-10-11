import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")

        service_obj = Service("C:\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    elif browser_name == "firefox":

        service_obj = Service("C:\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == "edge":

        service_obj = Service("C:\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()

