from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators=OrderPageLocators

    @allure.step('Вводим имя')
    def filling_name(self, name):
        self.send_keys_to_input(self.locators.INPUT_NAME, name)

    @allure.step('Вводим фамилию')
    def filling_second_name(self, second_name):
        self.send_keys_to_input(self.locators.INPUT_SECOND_NAME, second_name)

    @allure.step('Вводим адрес')
    def filling_address(self, address):
        self.send_keys_to_input(self.locators.INPUT_ADDRESS, address)

    @allure.step('Вводим и выбираем станцию метро')
    def filling_and_click_on_underground(self, underground):
        self.send_keys_to_input(self.locators.INPUT_UNDERGROUND, underground)
        self.click_on_element(self.locators.SELECTOR_UNDERGROUND)

    @allure.step('Вводим телефон')
    def filling_phone(self, phone):
        self.send_keys_to_input(self.locators.INPUT_PHONE, phone)

    @allure.step('Кликаем на кнопку Далее')
    def click_on_button_further(self):
        self.click_on_element(self.locators.BUTTON_FURTHER)

    @allure.step('Ожидаем загрузки формы Про аренду')
    def wait_visibility_of_form_about_rent(self):
        self.wait_visibility_of_element(self.locators.HEADER_FORM_ABOUT_RENT)

    @allure.step('Заполняем все поля на форме Для кого самокат и нажимаем далее')
    def filling_first_order_form(self, name, second_name, address, underground,phone):
        self.filling_name(name)
        self.filling_second_name(second_name)
        self.filling_address(address)
        self.filling_and_click_on_underground(underground)
        self.filling_phone(phone)
        self.click_on_button_further()
        self.wait_visibility_of_form_about_rent()


    @allure.step('Вводим и выбираем дату Когда привезти самокат')
    def filling_and_click_on_date(self, date, day_locator):
        self.send_keys_to_input(self.locators.INPUT_DATE, date)
        self.click_on_element(day_locator)

    @allure.step('Выбираем Срок аренды')
    def choosing_rental_period(self, period_locator):
        self.click_on_element(self.locators.FIELD_RENTAL_PERIOD)
        self.click_on_element(period_locator)

    @allure.step('Выбираем цвет самоката')
    def click_on_color_scooter(self, color_locator):
        self.click_on_element(color_locator)

    @allure.step('Вводим комментарий курьеру')
    def filling_comment(self, comment):
        self.send_keys_to_input(self.locators.INPUT_COMMENT, comment)

    @allure.step('Кликаем на кнопку Заказать')
    def click_on_button_order(self):
        self.click_on_element(self.locators.BUTTON_ORDER)

    @allure.step('Ожидаем загрузки формы Хотите оформить заказ')
    def wait_visibility_of_form_want_place_order(self):
        self.wait_visibility_of_element(self.locators.HEADER_WANT_PLACE_ORDER)

    @allure.step('Кликаем кнопку Да')
    def click_on_button_yes(self):
        self.click_on_element(self.locators.BUTTON_YES)

    @allure.step('Заполняем все поля на форме Про аренду и оформляем заказ')
    def filling_second_order_form(self, date, day_locator, period_locator, color_locator, comment):
        self.filling_and_click_on_date(date, day_locator)
        self.choosing_rental_period(period_locator)
        self.click_on_color_scooter(color_locator)
        self.filling_comment(comment)
        self.click_on_button_order()
        self.wait_visibility_of_form_want_place_order()
        self.click_on_button_yes()


    @allure.step('Проверяем появление окна Заказ оформлен')
    def check_successful_order_window(self):
        assert self.wait_visibility_of_element(self.locators.HEADER_PLACED_ORDER)




