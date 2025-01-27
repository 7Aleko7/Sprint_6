from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import pytest
import  allure


class TestMainPage:

    questions = [(MainPageLocators.COST_AND_PAY_QUESTION, MainPageLocators.COST_AND_PAY_ANSWER),
                 (MainPageLocators.FEW_SCOOTERS_QUESTION, MainPageLocators.FEW_SCOOTERS_ANSWER),
                 (MainPageLocators.RENTAL_TIME_QUESTION, MainPageLocators.RENTAL_TIME_ANSWER),
                 (MainPageLocators.ORDER_TODAY_QUESTION, MainPageLocators.ORDER_TODAY_ANSWER),
                 (MainPageLocators.EXTENSION_OR_REFUND_QUESTION, MainPageLocators.EXTENSION_OR_REFUND_ANSWER),
                 (MainPageLocators.CHARGING_QUESTION, MainPageLocators.CHARGING_ANSWER),
                 (MainPageLocators.ORDER_CANCEL_QUESTION, MainPageLocators.ORDER_CANCEL_ANSWER),
                 (MainPageLocators.BEYOND_MKAD_QUESTION, MainPageLocators.BEYOND_MKAD_ANSWER)
                 ]

    @allure.description('На главное странице, в блоке Вопросы о важном, кликаем на каждый вопрос и проверяем появление ответа с корректной информацией')
    @allure.title('Проверка отображения корректного ответа, при клике на вопрос в блоке Вопросы о важном')
    @pytest.mark.parametrize("question, answer", questions)
    def test_click_on_question(self, driver, open_main_page, question, answer):
        main_page = MainPage(driver)
        main_page.scroll_page_down()
        main_page.click_on_question(question)
        main_page.check_answer(answer)

    @allure.description('На главной странице кликаем на логотип Яндекса и проверяем что в новом окне открылась главная страница Яндекса(дзен)')
    @allure.title('После клика на логотип Яндекса, в новом окне открывается главная страница Яндекса(дзен)')
    def test_click_yandex_logo(self, driver, open_main_page):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.open_second_window()
        main_page.wait_yandex_main_page_url()
        main_page.check_yandex_main_page_url()