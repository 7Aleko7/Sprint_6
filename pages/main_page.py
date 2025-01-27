from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, question):
        self.click_on_element(question)

    @allure.step('Проверяем появившейся ответ')
    def check_answer(self, answer):
        assert self.wait_visibility_of_element(answer)