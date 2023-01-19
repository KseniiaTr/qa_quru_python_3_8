from selene.support.shared import browser
from selene import have
from selene import command
from tests import page_objects


def test_practice_form(size_browser):
    browser.open('https://demoqa.com/automation-practice-form')

    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=5).wait_until(have.size_greater_than_or_equal(3))
    ads.perform(command.js.remove)

    page_objects.type_personal_info('Alex', 'Alekseev', 'alexalekseev@gmail.com', '8910123121')
    page_objects.radio_button_gender('[name=gender]', 'Male')

    page_objects.data_picker()

    page_objects.type_subject('#subjectsInput', 'History')
    page_objects.checkbox_hobby('[type=checkbox][id=hobbies-checkbox-3]+label', 'Music')

    page_objects.upload_img()

    page_objects.type_address('#currentAddress', 'Delhi, Pyatnitskaya st 12/12')
    page_objects.dropdown_state('#react-select-3-input', 'NCR')
    page_objects.dropdown_city('#react-select-4-input', 'Delhi')

    page_objects.button_submit('#submit')


def test_check_info_in_table():
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Alex Alekseev', 'alexalekseev@gmail.com', 'Male', '8910123121',
        '07 May,1991', 'History', 'Music', 'Photo_test_yellow.png', 'Delhi, Pyatnitskaya st 12/12', 'NCR Delhi'))
