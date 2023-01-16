from selene.support.shared import browser




def pick_date(my_browser):
    my_browser.element('#dateOfBirthInput').click()
    my_browser.element('.react-datepicker__month-select').send_keys('May')
    my_browser.element('.react-datepicker__year-select').send_keys('1991')
    my_browser.element(f'.react-datepicker__day--00{7}').click()