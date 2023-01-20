from selene.support.shared import browser


def choose_dropdown(selector, value):
    browser.element(selector).send_keys(value).press_enter()


