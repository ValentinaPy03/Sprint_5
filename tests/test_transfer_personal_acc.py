from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators
from data import Credentials

class TestTransferPersonalAcc:
    def tests_transfer_personal_acc(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.field_email_log).send_keys(Credentials.email)
        driver.find_element(*TestLocators.field_password_log).send_keys(Credentials.password)
        driver.find_element(*TestLocators.button_input).click()
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.button_profile))
        button = driver.find_element(*TestLocators.button_profile).text
        assert button == 'Профиль'