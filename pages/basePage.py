from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_site import driver


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def click_button(self, locator):
        self.driver.find_element(locator).click()

class SignInPage(BasePage):
    def field_input(self, locator, input):
        self.driver.find_element(locator).send_keys(input)