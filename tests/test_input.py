from data import Credentials
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators

class TestImput:
    def tests_imput_button_log_in_account(self, driver):

        driver.find_element(*TestLocators.button_log_in_account).click()

        driver.find_element(*TestLocators.field_email_log).send_keys(Credentials.email)
        driver.find_element(*TestLocators.field_password_log).send_keys(Credentials.password)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_place_order))
        text = driver.find_element(*TestLocators.button_place_order)
        assert text.is_displayed(), "Кнопка Оформить заказ не появилась"

    def tests_imput_button_personal_acc(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()

        driver.find_element(*TestLocators.field_email_log).send_keys(Credentials.email)
        driver.find_element(*TestLocators.field_password_log).send_keys(Credentials.password)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_place_order))
        text = driver.find_element(*TestLocators.button_place_order)
        assert text.is_displayed(), "Кнопка Оформить заказ не появилась"

    def tests_imput_by_form_registration(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_open_registration_form))
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.button_input_reg).click()

        driver.find_element(*TestLocators.field_email_log).send_keys(Credentials.email)
        driver.find_element(*TestLocators.field_password_log).send_keys(Credentials.password)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_place_order))
        text = driver.find_element(*TestLocators.button_place_order)
        assert text.is_displayed(), "Кнопка Оформить заказ не появилась"

    def tests_imput_by_form_recover_password(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_recover_password))

        driver.find_element(*TestLocators.button_recover_password).click()
        driver.find_element(*TestLocators.button_input_recover).click()
        driver.find_element(*TestLocators.field_email_log).send_keys(Credentials.email)
        driver.find_element(*TestLocators.field_password_log).send_keys(Credentials.password)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_place_order))
        text = driver.find_element(*TestLocators.button_place_order)
        assert text.is_displayed(), "Кнопка Оформить заказ не появилась"
