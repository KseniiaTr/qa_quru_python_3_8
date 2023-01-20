from selene.support.shared import browser


def pick_month(selector, month):
    browser.element(selector).send_keys(month)


def pick_year(selector, year):
    browser.element(selector).send_keys(year)


def pick_data(day):
    browser.element(day).click()
