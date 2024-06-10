import pytest
from selenium import webdriver
from data_user import DataUser
from generators_data_user import generate_login_user, generate_password_user
from locators.login_locators import LoginLocators
from urls import UrlsPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(UrlsPage.base_url + UrlsPage.login_page)
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(DataUser.login_user)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(DataUser.password_user)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()


@pytest.fixture()
# генерация данных пользователя
def generate_data_user():
    name = 'Настя'
    email = generate_login_user()
    password = generate_password_user()
    return name, email, password
