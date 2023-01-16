from selene import command
from selene.support.shared import browser


def button_submit(my_browser, selector):
    my_browser.element(selector).perform(command.js.click)