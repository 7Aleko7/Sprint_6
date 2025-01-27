from pages.order_page import OrderPage
from pages.base_page import BasePageLocators
from pages.order_page import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data import TestOrder
import allure
import pytest

class TestOrderPage:
    parameters=[(BasePageLocators.HEADER_BUTTON_ORDER, TestOrder.name[0], TestOrder.second_name[0],TestOrder.address[0], TestOrder.underground[0], TestOrder.phone[0],TestOrder.date[0], OrderPageLocators.TWENTY_FIFTH_DAY_OF_MONTH, OrderPageLocators.RENTAL_PERIOD_DAY, OrderPageLocators.CHECKBOX_BLACK, TestOrder.comment[0]),
                (MainPageLocators.FOOTER_BUTTON_ORDER ,TestOrder.name[1], TestOrder.second_name[1], TestOrder.address[1], TestOrder.underground[1], TestOrder.phone[1], TestOrder.date[1], OrderPageLocators.SECOND_DAY_OF_MONTH, OrderPageLocators.RENTAL_PERIOD_ONE_WEEK, OrderPageLocators.CHECKBOX_GREY, TestOrder.comment[1])
    ]

    @allure.description('Заполняем формы, Для кого самокат и Про аренды, оформления заказа валидными данными и проверяем что заказ оформился')
    @allure.title('Оформление заказа, с заполнением всех возможных полей валидными данными')
    @pytest.mark.parametrize("order_button_locator, name, second_name, address, underground, phone, date, day_locator, period_locator, color_locator, comment", parameters)
    def test_successful_order(self, driver, open_main_page, order_button_locator, name, second_name, address, underground, phone, date, day_locator, period_locator, color_locator, comment):
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.scroll_and_click_button(order_button_locator)
        order_page.filling_first_order_form(name, second_name, address, underground, phone)
        order_page.filling_second_order_form(date, day_locator, period_locator, color_locator, comment)
        order_page.check_successful_order_window()

    @allure.description('На странице оформления заказа кликаем на логотип Самоката и проверяем что происходит переход на главную страницу Яндекс Самоката')
    @allure.title('После клика на логотип Самоката, происходит переход на главную страницу Яндекс Самоката')
    def test_click_scooter_logo(self, driver, open_order_page):
        order_page = OrderPage(driver)
        order_page.click_scooter_logo()
        order_page.check_scooter_url()