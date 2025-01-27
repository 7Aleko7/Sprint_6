from selenium.webdriver.common.by import By

class BasePageLocators:
    # Логотип Яндекс
    LOGO_YANDEX=By.XPATH, ".//img[@alt='Yandex']"

    # Логотип Самокат
    LOGO_SCOOTER = By.XPATH, ".//img[@alt='Scooter']"

    # Кнопка Заказать в заголовке
    HEADER_BUTTON_ORDER = By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']"

    # Кнопка Куки
    COOKIE_BUTTON = By.XPATH, ".//button[text()='да все привыкли']"
