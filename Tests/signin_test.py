import links
from pages.basePage import *
from locators.locators import *

def test_signIn(driver):
    page1, page2 = BasePage(driver), SignInPage(driver)
    page1.open_page(links.magento)
    page1.click_button(authorization)
    page2.field_input(input_email, 'fatalmc14@gmail.com')
    page2.field_input(input_password, '148814881488')
    page2.click_button(submit)