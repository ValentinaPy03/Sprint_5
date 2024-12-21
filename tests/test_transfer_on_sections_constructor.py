from conftest import driver
from locators import TestLocators

class TestTransferOnSectionsConstructor:
    def tests_transfer_on_section_sauces(self, driver):
        driver.find_element(*TestLocators.button_menu_sauces).click()
        name = driver.find_element(*TestLocators.name_section_sauces)
        list = driver.find_element(*TestLocators.list_sauces)
        assert name.is_displayed(), "Названи раздела нет"
        assert list.is_displayed(), "Список не отображается"

    def tests_transfer_on_section_breads(self, driver):
        driver.find_element(*TestLocators.button_menu_sauces).click()
        driver.find_element(*TestLocators.button_menu_breads).click()
        name = driver.find_element(*TestLocators.name_section_breads)
        list = driver.find_element(*TestLocators.list_bread)
        assert name.is_displayed(), "Названи раздела нет"
        assert list.is_displayed(), "Список не отображается"

    def tests_transfer_on_section_fillings(self, driver):
        driver.find_element(*TestLocators.button_menu_fillings).click()
        name = driver.find_element(*TestLocators.name_section_fillings)
        list = driver.find_element(*TestLocators.list_fillings)
        assert name.is_displayed(), "Названи раздела нет"
        assert list.is_displayed(), "Список не отображается"

