import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from urls import Urls

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим страницу вниз')
    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Если элемент виден кликаем на него, если нет скроллим до него, а затем кликаем')
    def scroll_and_click_button(self, locator):
        element = self.driver.find_element(*locator)
        if element.is_displayed():
            self.click_on_element(locator)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.click_on_element(locator)


    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)


    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидаем прогрузки страницы главной страницы Яндекса(дзен)')
    def wait_yandex_main_page_url(self):
        return WebDriverWait(self.driver, 6).until(expected_conditions.url_contains(Urls.YANDEX_MAIN_PAGE))


    def get_current_url(self):
        current_url=self.driver.current_url
        return current_url

    @allure.step('Кликаем по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_on_element(BasePageLocators.LOGO_SCOOTER)

    @allure.step('Кликаем по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_on_element(BasePageLocators.LOGO_YANDEX)

    @allure.step('Переходим на вторую вкладку')
    def open_second_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверяем урл главной страницы Яндекса(дзен)')
    def check_yandex_main_page_url(self):
        assert self.get_current_url() == Urls.YANDEX_MAIN_PAGE

    @allure.step('Проверяем урл главной страницы Яндекс Самоката')
    def check_scooter_url(self):
        assert self.get_current_url() == Urls.BASE_URL

    @allure.step('Принимаем Куки')
    def accept_cookies(self):
        self.click_on_element(BasePageLocators.COOKIE_BUTTON)

