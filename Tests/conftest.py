import pytest
from selenium import webdriver
from pages.basePage import *

@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.close()



