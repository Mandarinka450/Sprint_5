from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from locators.logout_locators import LogoutLocators
from urls import UrlsPage


class TestLogout:
    # Тест проверки выхода из аккаунта по кнопке "Выход" в личном кабинете
    def test_logout_via_button_on_personal_account_page(self, driver, login):
        # переход в Линый кабинет
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LogoutLocators.LOGOUT_BUTTON)).click()
        title_login = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LogoutLocators.TITLE_LOGIN)).text
        current_url = driver.current_url
        assert current_url == UrlsPage.base_url + UrlsPage.login_page and title_login == 'Вход'