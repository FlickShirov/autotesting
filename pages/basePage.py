from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_site import driver
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def open_page(self, url):
        self.browser.get(url)

    def click_button(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

class SignInPage(BasePage):
    def field_input(self, locator, user_input):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(user_input)

    def message_input(self, locator, title):
        page_title = self.wait.until(EC.element_to_be_clickable(locator))
        assert title == page_title.text
