import random
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators


class TestTransferConstructor:
    def tests_transfer_by_click_button_constructor(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.field_name_reg).send_keys('Валя')
        rand_email = f'valiapyreva13{random.randint(000, 999)}@yandex.ru'
        driver.find_element(*TestLocators.field_email_reg).send_keys(rand_email)
        rand_password = random.randint(000000, 999999)
        driver.find_element(*TestLocators.field_password_reg).send_keys(rand_password)
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(*TestLocators.field_email_log).send_keys(rand_email)
        driver.find_element(*TestLocators.field_password_log).send_keys(rand_password)
        driver.find_element(*TestLocators.button_input).click()

        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.logo_constructor).click()

        el = driver.find_element(By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')

        assert el.is_displayed(), "Переход не произошел"

    def tests_transfer_by_click_logo(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.field_name_reg).send_keys('Валя')
        rand_email = f'valiapyreva13{random.randint(000, 999)}@yandex.ru'
        driver.find_element(*TestLocators.field_email_reg).send_keys(rand_email)
        rand_password = random.randint(000000, 999999)
        driver.find_element(*TestLocators.field_password_reg).send_keys(rand_password)
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(*TestLocators.field_email_log).send_keys(rand_email)
        driver.find_element(*TestLocators.field_password_log).send_keys(rand_password)
        driver.find_element(*TestLocators.button_input).click()

        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.logo).click()

        el = driver.find_element(By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')

        assert el.is_displayed(), "Переход не произошел"
