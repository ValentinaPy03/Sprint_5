from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from conftest import driver

class TestLocators:
    button_personal_account = By.LINK_TEXT, "Личный Кабинет" #кнопка "Личный кабинет" на главном экране
    button_open_registration_form = By.LINK_TEXT, "Зарегистрироваться" #кнопка перехода на форму регистрации
    field_name_reg = By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']" #поле Имя на форме регистрации
    field_email_reg = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']" #поле Email на форме регистрации
    field_password_reg = By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']"  # поле Пароль на форме регистрации
    button_register = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]" #кнопка Зарегистрироваться на форме регистрации
    button_input_reg = By.CLASS_NAME, "Auth_link__1fOlj" # кнопка Войти на форме регистрации
    error_invalid_password = By.CLASS_NAME, "input__error text_type_main-default" #ошибка Некорректный пароль
    button_place_order = By.XPATH, "//button[contains(text(), 'Оформить заказ')]" # кнопка Оформить заказ
    button_profile = By.XPATH, '//a[@href="/account/profile"]'

    button_log_in_account = By.XPATH, "//button[text()='Войти в аккаунт']" #кнопка Войти в аккаунт на главном экране
    field_email_log = By.XPATH, "//input[@name='name']"#поле Email на форме Вход
    field_password_log = By.XPATH, "//input[@name='Пароль']"  # поле Пароль на форме Вход
    button_input = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and contains(text(), 'Войти')]" # кнопка Войти на форме Вход
    button_recover_password = By.XPATH, "//a[text()='Восстановить пароль']" # кнопка Восстановить пароль на форме входа
    button_input_recover = By.XPATH, "//a[text()='Войти']" # кнопка Войти на форме восстановления пароля

    logo = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
    logo_constructor = By.LINK_TEXT, "Конструктор" # кнопка Конструктор
    button_log_out = By.XPATH, "//button[text()='Выход']" #кнопка Выйти на странице профиля

    button_menu_sauces = By.XPATH, "//span[text()='Соусы']" # кнопка раздела Соусы в меню
    name_section_sauces = By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Соусы"]'
    list_sauces = By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][2]'

    button_menu_fillings = By.XPATH, "//span[text()='Начинки']" # кнопка раздела Начинки в меню
    list_fillings = By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][3]'
    name_section_fillings = By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Начинки"]'

    button_menu_breads = By.XPATH, "//span[text()='Булки']" # кнопка раздела Булки в меню
    list_bread = By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]'
    name_section_breads = By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Булки"]'

