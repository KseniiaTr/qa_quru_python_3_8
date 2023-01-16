from selene import command
from selene.support.shared import browser


def print_adress(my_browser, selector, value):
    my_browser.element(selector).perform(command.js.set_value(value))

