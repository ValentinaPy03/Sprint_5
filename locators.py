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

    button_log_in_account = By.XPATH, "//button[text()='Войти в аккаунт']" #кнопка Войти в аккаунт на главном экране
    field_email_log = By.XPATH, "//input[@name='name']"#поле Email на форме Вход
    field_password_log = By.XPATH, "//input[@name='Пароль']"  # поле Пароль на форме Вход
    button_input = By.XPATH, "//button[text()='Войти']" # кнопка Войти на форме Вход
    button_recover_password = By.XPATH, "//a[text()='Восстановить пароль']" # кнопка Восстановить пароль на форме входа
    button_input_recover = By.XPATH, "//button[text()='Войти']" # кнопка Войти на форме восстановления пароля

    logo = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
    logo_constructor = By.LINK_TEXT, "Конструктор" # кнопка Конструктор

    button_menu_sauces = By.XPATH, "//span[text()='Соусы']"
    button_menu_fillings = By.XPATH, "//span[text()='Начинки']"
    button_menu_breads = By.XPATH, "//span[text()='Булки']"
