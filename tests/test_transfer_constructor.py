from conftest import driver
from locators import TestLocators
from data import Credentials


class TestTransferConstructor:
    def tests_transfer_by_click_button_constructor(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()

        driver.find_element(*TestLocators.field_email_log).send_keys(Credentials.email)
        driver.find_element(*TestLocators.field_password_log).send_keys(Credentials.password)
        driver.find_element(*TestLocators.button_input).click()

        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.logo_constructor).click()

        text = driver.find_element(*TestLocators.button_place_order)
        assert text.is_displayed(), "Переход не произошел"


    def tests_transfer_by_click_logo(self,driver):
        driver.find_element(*TestLocators.button_personal_account).click()

        driver.find_element(*TestLocators.field_email_log).send_keys(Credentials.email)
        driver.find_element(*TestLocators.field_password_log).send_keys(Credentials.password)
        driver.find_element(*TestLocators.button_input).click()

        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.logo).click()

        text = driver.find_element(*TestLocators.button_place_order)
        assert text.is_displayed(), "Переход не произошел"
