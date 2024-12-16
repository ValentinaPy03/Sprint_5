import random
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators

class TestImput:
    def tests_imput_button_log_in_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.field_name_reg).send_keys('Валя')
        rand_email = f'valiapyreva13{random.randint(000, 999)}@yandex.ru'
        driver.find_element(*TestLocators.field_email_reg).send_keys(rand_email)
        rand_password = random.randint(000000, 999999)
        driver.find_element(*TestLocators.field_password_reg).send_keys(rand_password)
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]")))
        driver.find_element(*TestLocators.logo).click()

        driver.find_element(*TestLocators.button_log_in_account).click()

        driver.find_element(*TestLocators.field_email_log).send_keys(rand_email)
        driver.find_element(*TestLocators.field_password_log).send_keys(rand_password)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

        driver.quit()

    def tests_imput_button_personal_acc(self, driver):
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
        driver.find_element(*TestLocators.logo).click()
        driver.find_element(*TestLocators.button_personal_account).click()

        driver.find_element(*TestLocators.field_email_log).send_keys(rand_email)
        driver.find_element(*TestLocators.field_password_log).send_keys(rand_password)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        driver.quit()

    def tests_imput_by_form_registration(self, driver):
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

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
        driver.find_element(By.XPATH, "//button[text()='Выход']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться")))
        driver.find_element(*TestLocators.button_open_registration_form).click()
        driver.find_element(*TestLocators.button_input_reg).click()

        driver.find_element(*TestLocators.field_email_log).send_keys(rand_email)
        driver.find_element(*TestLocators.field_password_log).send_keys(rand_password)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        driver.quit()


    def tests_imput_by_form_recover_password(self, driver):
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

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
        driver.find_element(By.XPATH, "//button[text()='Выход']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Восстановить пароль']")))

        driver.find_element(*TestLocators.button_recover_password).click()
        driver.find_element(By.XPATH, '//a[text()="Войти"]').click()
        driver.find_element(*TestLocators.field_email_log).send_keys(rand_email)
        driver.find_element(*TestLocators.field_password_log).send_keys(rand_password)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        driver.quit()




