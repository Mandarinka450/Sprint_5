from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from locators.section_constructor_locators import SectionConstructionLocators
from urls import UrlsPage


class TestSectionConstruction:

    # Тест проверки перехода в раздел "Булки"
    def test_get_section_rolls(self, driver):
        driver.get(UrlsPage.main_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(SectionConstructionLocators.TITLE_CONSTRUCTOR))
        rolls_class_active = driver.find_element(*SectionConstructionLocators.ROLLS_SECTION).get_attribute('class')

        assert 'tab_tab_type_current__2BEPc' in rolls_class_active

    # Тест проверки перехода в раздел "Соусы"
    def test_get_section_sauces(self, driver):
        driver.get(UrlsPage.main_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(SectionConstructionLocators.TITLE_CONSTRUCTOR))
        sauces = driver.find_element(*SectionConstructionLocators.SAUCES_SECTION)
        sauces.click()
        sauces_class_active = sauces.get_attribute('class')

        assert 'tab_tab_type_current__2BEPc' in sauces_class_active

    # Тест проверки перехода в раздел "Начинки"
    def test_get_section_fillings(self, driver):
        driver.get(UrlsPage.main_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(SectionConstructionLocators.TITLE_CONSTRUCTOR))
        fillings = driver.find_element(*SectionConstructionLocators.FILLINGS_SECTION)
        fillings.click()
        fillings_class_active = fillings.get_attribute('class')

        assert 'tab_tab_type_current__2BEPc' in fillings_class_active

    # Тест проверки перехода из личного кабинета в рааздел "Конструктор" по клику на кнопку "Конструктор"
    def test_click_constructor_via_button_from_personal_account(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))
        driver.find_element(*SectionConstructionLocators.LINK_CONSTRUCTOR).click()

        title_constructor = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(SectionConstructionLocators.
                                                                                            TITLE_CONSTRUCTOR)).text

        assert title_constructor == 'Соберите бургер'

    # Тест проверки перехода из личного кабинета в раздел "Конструктор" по клику на логотип
    def test_click_logo_to_constructor_from_personal_account_page(self, driver, login):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))
        driver.find_element(*SectionConstructionLocators.LOGO_CONSTRUCTOR).click()

        title_constructor = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(SectionConstructionLocators.
                                                                                            TITLE_CONSTRUCTOR)).text

        assert title_constructor == 'Соберите бургер'
