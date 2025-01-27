import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()

@pytest.fixture
def open_main_page(driver):
    driver.get(Urls.BASE_URL)

@pytest.fixture
def open_order_page(driver):
    driver.get(Urls.ORDER_URL)