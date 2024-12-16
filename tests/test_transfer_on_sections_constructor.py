from selenium.webdriver.common.by import By
from conftest import driver
from locators import TestLocators


class TestTransferOnSectionsConstructor:
    def tests_transfer_on_section_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_menu_sauces).click()
        name = driver.find_element(By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Соусы"]')
        list = driver.find_element(By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][2]')
        assert name.is_displayed(), "Названи раздела нет"
        assert list.is_displayed(), "Список не отображается"

    def tests_transfer_on_section_breads(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_menu_sauces).click()
        driver.find_element(*TestLocators.button_menu_breads).click()
        name = driver.find_element(By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Булки"]')
        list = driver.find_element(By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]')
        assert name.is_displayed(), "Названи раздела нет"
        assert list.is_displayed(), "Список не отображается"

    def tests_transfer_on_section_fillings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_menu_fillings).click()
        name = driver.find_element(By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Начинки"]')
        list = driver.find_element(By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][3]')
        assert name.is_displayed(), "Названи раздела нет"
        assert list.is_displayed(), "Список не отображается"

