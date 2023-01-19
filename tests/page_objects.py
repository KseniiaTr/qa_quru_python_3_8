import os

from selene import have, command
from selene.support.shared import browser
from tests.modul import dropdown, datepicker, checkboxes, radiobutton, upload_image


def type_personal_info(first_name, last_name, user_email, user_number):
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(user_email)
    browser.element('#userNumber').type(user_number)


def radio_button_gender(selector, value):
    radiobutton.choose_gender(selector, value)


def data_picker():
    datepicker.pick_date()


def type_subject(selector, text):
    browser.element(selector).type(text).press_enter()


def checkbox_hobby(selector, value):
    checkboxes.choose_hobbies(selector, value)


def upload_img():
    upload_image.add_image('#uploadPicture', '../resources/Photo_test_yellow.png')


def type_address(selector, address):
    browser.element(selector).perform(command.js.set_value(address))


def dropdown_state(selector, state):
    dropdown.choose_dropdown(selector, state)


def dropdown_city(selector, city):
    dropdown.choose_dropdown(selector, city)


def button_submit(selector):
    browser.element(selector).perform(command.js.click)



