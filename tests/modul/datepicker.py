from selene.support.shared import browser


def pick_date():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('May')
    browser.element('.react-datepicker__year-select').send_keys('1991')
    browser.element(f'.react-datepicker__day--00{7}').click()