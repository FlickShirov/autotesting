from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_site import driver


class BasePage():
    def __init__(self, driver):
        self.browser = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.browser.get(url)

    def click_button(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

class SignInPage(BasePage):
    def field_input(self, locator, input):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(input)