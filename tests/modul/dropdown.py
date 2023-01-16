from selene.support.shared import browser


def city_state(my_browser, selector, value):
    my_browser.element(selector).send_keys(value).press_enter()


