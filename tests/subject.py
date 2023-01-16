from selene.support.shared import browser


def type_subject(my_browser, selector, value):
    my_browser.element(selector).type(value).press_enter()