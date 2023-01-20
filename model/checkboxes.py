from selene import have
from selene.support.shared import browser


def choose_hobbies(selector, text):
    browser.element(selector).should(have.exact_text(text)).click()
