from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Заголовок "Для кого самокат"
    HEADER_ORDER_PAGE = By.XPATH, "//div[@placeholder='Для кого самокат']"

    # Инпут Имя
    INPUT_NAME = By.XPATH, "//input[@placeholder='* Имя']"

    # Инпут Фамилия
    INPUT_SECOND_NAME = By.XPATH, "//input[@placeholder='* Фамилия']"

    # Инпут Адрес
    INPUT_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"

    # Инпут Станция метро
    INPUT_UNDERGROUND = By.XPATH, "//input[@placeholder='* Станция метро']"

    # Селектор Метро
    SELECTOR_UNDERGROUND=By.CLASS_NAME, 'select-search__select'

    # Инпут Телефон
    INPUT_PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"

    # Кнопка "Далее"
    BUTTON_FURTHER = By.XPATH, ".//button[text()='Далее']"

    #Заголовок формы Про аренду
    HEADER_FORM_ABOUT_RENT=By.XPATH, ".//div[text()='Про аренду']"

    # Инпут Когда привезти самокат
    INPUT_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"

    # 25 число месяца
    TWENTY_FIFTH_DAY_OF_MONTH=By.CLASS_NAME, 'react-datepicker__day--025'

    # 2 число месяца
    SECOND_DAY_OF_MONTH = By.CLASS_NAME, 'react-datepicker__day--002'

    # Поле список Срок аренды
    FIELD_RENTAL_PERIOD=By.XPATH, "//div[text()='* Срок аренды']"

    # Срок аренды сутки
    RENTAL_PERIOD_DAY=By.XPATH, "//div[text()='сутки']"

    # Срок аренды неделя
    RENTAL_PERIOD_ONE_WEEK = By.XPATH, "//div[text()='семеро суток']"

    # Чекбокс Цвет самоката - черный
    CHECKBOX_BLACK=By.ID, 'black'

    # Чекбокс Цвет самоката - серый
    CHECKBOX_GREY = By.ID, 'grey'

    # Инпут Комментарий
    INPUT_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"

    # Кнопка Заказать
    BUTTON_ORDER = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"

    # Заголовок формы "Хотите оформить заказ?"
    HEADER_WANT_PLACE_ORDER = By.XPATH, "//div[text()='Хотите оформить заказ?']"

    # Кнопка Да
    BUTTON_YES = By.XPATH, ".//button[text()='Да']"

    # Заголовок формы "Хотите оформить заказ?"
    HEADER_PLACED_ORDER = By.XPATH, "//div[text()='Заказ оформлен']"

















