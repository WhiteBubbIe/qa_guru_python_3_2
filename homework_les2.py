
from selene import be, have
from selene.support.shared import browser


def test_search_positive(screen_config):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element("[id='search']").should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
# тест на поиск из первого дз

def test_negative_search_(screen_config):
    browser.element('[name="q"]').should(be.blank).type('fujg9rj450urj9409j8b6j8rjh0049').press_enter()
    browser.element('p[aria-level]').should(have.text('По запросу fujg9rj450urj9409j8b6j8rjh0049 ничего не найдено'))
# негативный тест, на поиск белиберды