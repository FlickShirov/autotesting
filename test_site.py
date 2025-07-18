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
    browser.implicitly_wait(3)
    yield browser
    time.sleep(2)
    browser.close()

def test_open_nigger(driver):
    driver.get(links.magento)
    Argus = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[3]/div/div[2]/div[3]/div/div/ol/li[3]/div/div/strong/a")
    Argus.click()
    title = driver.find_element(By.CLASS_NAME, 'base')
    assert title.text == 'Argus All-Weather Tank'

def test_niggers_prize(driver):
    driver.get(links.magento)
    Argus = driver.find_element(By.XPATH,"//*[@id='maincontent']/div[3]/div/div[2]/div[3]/div/div/ol/li[3]/div/div/strong/a")
    Argus.click()
    price = driver.find_element(By.CLASS_NAME, 'price')
    assert price.text == '$22.00'