# https://demoblaze.com/
# https://magento.softwaretestingboard.com/
# https://www.qa-practice.com/
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import links



@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    time.sleep(10)
    browser.close()

def test_open_nigger(driver):
    driver.get(links.magento)
    Argus = driver.find_element(By.LINK_TEXT, 'Argus All-Weather Tank')
    Argus.click()
    title = driver.find_element(By.CLASS_NAME, 'base')
    assert title.text == 'Argus All-Weather Tank'