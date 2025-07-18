import links
from pages.basePage import *
from locators.locators import *

def test_signIn(driver):
    basepage, signpage = BasePage(driver), SignInPage(driver)
    basepage.open_page(links.magento)
    basepage.click_button(authorization)
    signpage.field_input(input_email, 'fatalmc14@gmail.com')
    signpage.field_input(input_password, '148814881488')
    signpage.click_button(submit)
    signpage.message_input(message, 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')