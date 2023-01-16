import os

from selene.support.shared import browser


def add_image(my_browser, selector, path_to):
    my_browser.element(selector).set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), path_to)
        )
    )