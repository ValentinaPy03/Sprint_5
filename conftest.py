from selenium import webdriver
import pytest
from url import *

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(url_main_page)
    yield driver
    driver.quit()



