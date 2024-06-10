from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_IN_ACCOUNT = (By.XPATH, './/button[contains(text(), "Войти в аккаунт")]') # кнопка "Войти в аккаунт"
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/following-sibling::input') # инпут для ввода почты
    PASSWORD_INPUT = (By.XPATH, './/*[text()="Пароль"]/following-sibling::input') # инпут для ввода пароля
    LOGIN_BUTTON = (By.XPATH, './/button[contains(text(), "Войти")]') # кнопка "Войти"
    PERSONAL_ACCOUNT = (By.XPATH, './/p[contains(text(), "Личный Кабинет")]/parent::a') # ссылка "Личный кабинет"
    LOGIN = (By.XPATH, './/*[text()="Логин"]/following-sibling::input') # инпут со значением "Логин"
    NAME = (By.XPATH, './/*[text()="Имя"]/following-sibling::input') # инпут со значением "Имя"
    LOGIN_LINK = (By.XPATH, './/a[@class="Auth_link__1fOlj"]') # ссылка "Вход" на страницу ввода логина и пароля
    PROFILE_TITLE = (By.XPATH, './/a[contains(text(), "Профиль")]') # ссылка на профиль



