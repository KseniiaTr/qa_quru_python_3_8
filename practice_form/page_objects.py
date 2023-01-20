from selene import command, have
from selene.support.shared import browser
from model import dropdown, datepicker, checkboxes
from model import radiobutton
from utilits import upload_image, advertisement


def hide_adv():
    advertisement.remove_ads('[id^=google_ads][id$=container__]')


def type_personal_info(first_name, last_name, user_email, user_number):
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(user_email)
    browser.element('#userNumber').type(user_number)


def radio_button_gender(value):
    radiobutton.choose_gender('[name=gender]', value)


def click_data():
    browser.element('#dateOfBirthInput').click()


def select_month(month):
    datepicker.pick_month('.react-datepicker__month-select', month)


def select_year(year):
    datepicker.pick_year('.react-datepicker__year-select', year)


def select_day(day):
    datepicker.pick_data(f'.react-datepicker__day--00{day}')


def type_subject(text):
    browser.element('#subjectsInput').type(text).press_enter()


def checkbox_hobby(value):
    checkboxes.choose_hobbies('[type=checkbox][id=hobbies-checkbox-3]+label', value)


def upload_img(path):
    upload_image.add_image('#uploadPicture', path)


def type_address(address):
    browser.element('#currentAddress').perform(command.js.set_value(address))


def dropdown_state(state):
    dropdown.choose_dropdown('#react-select-3-input', state)


def dropdown_city(city):
    dropdown.choose_dropdown('#react-select-4-input', city)


def button_submit():
    browser.element('#submit').perform(command.js.click)


def check_form(*all_text):
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(all_text))


