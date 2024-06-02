import string
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.login_locators import LoginLocators
from locators.registration_locators import RegistrationLocators
from urls import UrlsPage


class TestRegistration:

    # Генератор уникального пароля
    @staticmethod
    def generate_password_user():
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(1, 7))
        return password

    # Генератор уникального логина
    @staticmethod
    def generate_login_user():
        first_names = ['maksim', 'nastya', 'dasha', 'daniil', 'sasha']
        last_names = ['efimov', 'korotenko', 'sibirskix', 'pashkevich', 'savchenko']
        domains = ['@mail.ru', '@yandex.ru']
        return random.choice(first_names) + random.choice(last_names) + '9' + str(random.randrange(100, 999)) + random.choice(domains)

    # тест на проверку успешной регистрации
    def test_registration_user_with_correct_data(self, driver):
        driver.get(UrlsPage.registration_page)

        name = 'Настя'
        email = self.generate_login_user()
        password = self.generate_password_user()

        # регистрация пользователя
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationLocators.TITLE_REGISTRATION))
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

        # авторизация только что зарегистрированного пользователя
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationLocators.TITLE_LOGIN))
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        # переход в профиль
        driver.find_element(*LoginLocators.PERSONAL_ACCOUNT).click()

        name_current_user = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LoginLocators.NAME)).get_attribute('value')
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute('value')

        # проверка того, что данные зарегистрированного пользователя совпадают
        assert name_current_user == name and login_current_user == email

    # тест на проверку неуспешной регистрации: пароль не соответствует требованиям (длина меньше 6 символов)
    def test_registration_with_password_less_six_symbols(self, driver):
        driver.get(UrlsPage.registration_page)

        name = 'Настя'
        email = self.generate_login_user()
        wrong_password = '123'

        # регистрация пользователя с некорректным паролем (меньше 6 символов)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationLocators.TITLE_REGISTRATION))
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(wrong_password)
        driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

        error_message = driver.find_element(*RegistrationLocators.ERROR_MESSAGE).text

        # проверка того, что появилось сообщение об ошибке
        assert error_message == 'Некорректный пароль'