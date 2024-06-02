from selenium.webdriver.common.by import By


class RegistrationLocators:
    NAME_INPUT = (By.XPATH, './/*[text()="Имя"]/following-sibling::input')  # инпут для ввода имени юзера
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/following-sibling::input')  # инпут для ввода почты
    PASSWORD_INPUT = (By.XPATH, './/*[text()="Пароль"]/following-sibling::input')  # инпут для ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, './/button[contains(text(), "Зарегистрироваться")]')  # кнопка "Зарегистрироваться"
    TITLE_LOGIN = (By.XPATH, './/h2[contains(text(), "Вход")]')  # заголовок "Вход"
    ERROR_MESSAGE = (By.XPATH, './/p[contains(text(), "Некорректный пароль")]')  # сообщение об ошибке: некорректный пароль
    TITLE_REGISTRATION = (By.XPATH, './/h2[contains(text(), "Регистрация")]')  # заголовок страницы регистрации

