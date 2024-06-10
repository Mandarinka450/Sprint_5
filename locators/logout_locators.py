from selenium.webdriver.common.by import By


class LogoutLocators:
    LOGOUT_BUTTON = (By.XPATH, './/button[contains(text(), "Выход")]')  # кнопка "Выход"
    TITLE_LOGIN = (By.XPATH, './/div[@class="Auth_login__3hAey"]/h2[contains(text(), "Вход")]')  # заголовок "Вход"