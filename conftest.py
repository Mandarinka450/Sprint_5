import pytest
from selenium import webdriver
from data_user import DataUser
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
    driver.get(UrlsPage.login_page)
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(DataUser.login_user)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(DataUser.password_user)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

