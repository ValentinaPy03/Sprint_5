from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from url import url_main_page
from helper import generate_registration_data
import random

class TestRegistration:
    def tests_successful_registration(self, driver):
        email, password = generate_registration_data()
        driver.get(url_main_page)
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.field_name_reg).send_keys('Валя')
        driver.find_element(*TestLocators.field_email_reg).send_keys(email)
        driver.find_element(*TestLocators.field_password_reg).send_keys(password)
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_input))
        button = driver.find_element(*TestLocators.button_input)
        assert button.is_displayed(), "Кнопка 'Войти' не видна на странице."

    def teats_password_less_6_symbols(self, driver):
        driver.get(url_main_page)
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.field_name_reg).send_keys('Валя')
        driver.find_element(*TestLocators.field_email_reg).send_keys(
            f'valiapyreva13{random.randint(000, 999)}@yandex.ru')
        driver.find_element(*TestLocators.field_password_reg).send_keys(random.randint(000, 999))
        driver.find_element(*TestLocators.button_register).click()

        button = driver.find_element(*TestLocators.error_invalid_password)
        assert button.is_displayed(), "Ошибка 'Некорректный пароль' не появилась"







