from selene import have
from selene.support.shared import browser


def choose_gender(my_browser, selector, value):
    my_browser.all(selector).element_by(have.value(value)).element('..').click()


def choose_hobbies(my_browser, selector, text):
    my_browser.element(selector).should(have.exact_text(text)).click()
