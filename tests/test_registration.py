import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators


class TestRegistration:
    def tests_successful_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.field_name_reg).send_keys('Валя')
        driver.find_element(*TestLocators.field_email_reg).send_keys(f'valiapyreva13{random.randint(000, 999)}@yandex.ru')
        driver.find_element(*TestLocators.field_password_reg).send_keys(random.randint(000000, 999999))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                          "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        button = driver.find_element(*TestLocators.button_input)
        assert button.is_displayed(), "Кнопка 'Войти' не видна на странице."
        driver.quit()

    def teats_password_less_6_symbols(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.field_name_reg).send_keys('Валя')
        driver.find_element(*TestLocators.field_email_reg).send_keys(
            f'valiapyreva13{random.randint(000, 999)}@yandex.ru')
        driver.find_element(*TestLocators.field_password_reg).send_keys(random.randint(000, 999))
        driver.find_element(*TestLocators.button_register).click()

        button = driver.find_element(By.CLASS_NAME, "input__error text_type_main-default")
        assert button.is_displayed(), "Ошибка 'Некорректный пароль' не появилась"
        driver.quit()






