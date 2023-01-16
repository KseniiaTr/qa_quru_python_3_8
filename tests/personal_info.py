from selene.support.shared import browser


def type_personal_info(my_browser, selector, value):
    my_browser.element(selector).type(value)




