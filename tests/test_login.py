from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_user import DataUser
from locators.login_locators import LoginLocators
from urls import UrlsPage


class TestLogin:

    #  Тест проверки входа в аакаунт через кнопку "Войти в аккаунт" на главной странице
    def test_login_in_account_via_button_on_main_page(self, driver):
        driver.get(UrlsPage.main_page)

        # вход пользователя через кнопку на главной странице "Войти в аккаунт"
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.LOGIN_IN_ACCOUNT)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(DataUser.login_user)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(DataUser.password_user)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        # переход на страницу профиля пользователя
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))

        name_current_user = driver.find_element(*LoginLocators.NAME).get_attribute("value")
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute("value")

        # проверка того, что залогинились под конкретным пользователем
        assert name_current_user == DataUser.name_user and login_current_user == DataUser.login_user

    # Тест проверки входа в аккаунт через кнопку "Личный кабинет"
    def test_login_in_account_via_button_personal_account(self, driver):
        driver.get(UrlsPage.main_page)

        # вход пользователя через кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(DataUser.login_user)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(DataUser.password_user)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        # переход на страницу профиля пользователя
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))

        name_current_user = driver.find_element(*LoginLocators.NAME).get_attribute("value")
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute("value")

        # проверка того, что залогинились под конкретным пользователем
        assert name_current_user == DataUser.name_user and login_current_user == DataUser.login_user

    # Тест проверки входа в аккаунт через кнопку в форме регистрации
    def test_login_in_account_via_button_on_registration_page(self, driver):
        driver.get(UrlsPage.registration_page)

        # вход пользователя по кнопке через форму регистрации
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.LOGIN_LINK)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(DataUser.login_user)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(DataUser.password_user)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        # переход на страницу профиля пользователя
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))

        name_current_user = driver.find_element(*LoginLocators.NAME).get_attribute("value")
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute("value")

        # проверка того, что залогинились под конкретным пользователем
        assert name_current_user == DataUser.name_user and login_current_user == DataUser.login_user

    # Тест проверки входа в аккаунт через кнопку в форме восстановления пароля
    def test_login_in_account_via_button_on_forgot_password_page(self, driver):
        driver.get(UrlsPage.forgot_password_page)

        # вход пользователя по кнопке через форму восстановления пароля
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.LOGIN_LINK)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(DataUser.login_user)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(DataUser.password_user)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        # переход на страницу профиля пользователя
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))

        name_current_user = driver.find_element(*LoginLocators.NAME).get_attribute("value")
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute("value")

        # проверка того, что залогинились под конкретным пользователем
        assert name_current_user == DataUser.name_user and login_current_user == DataUser.login_user

    # Тест проверки перехода в Личный кабинет
    def test_click_button_to_personal_account(self, driver, login):
        # ожидание кликабельности кнопки "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))
        current_url = driver.current_url

        # проверка того, адрес текущей страницы совпадает с ожидаемым
        assert current_url == UrlsPage.profile_page
