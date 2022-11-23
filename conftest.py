import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function")
def screen_config():
    browser.open('https://www.google.com').driver.maximize_window()
#добавляем фикстуру применяемую к каждой функции, открываем браузер и раскрываем его на весь экран