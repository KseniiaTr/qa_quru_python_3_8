import os

from selene.support.shared import browser


def add_image(selector, path_to):
    browser.element(selector).set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), path_to)
        )
    )