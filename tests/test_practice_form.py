from selene.support.shared import browser
from selene import have
from selene import command
from tests import personal_info, adress, button, subject
from tests.modul import checkboxes, datepicker, dropdown, upload_image


def test_practice_form(size_browser):
    browser.open('https://demoqa.com/automation-practice-form')

    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=5).wait_until(have.size_greater_than_or_equal(3))
    ads.perform(command.js.remove)

    personal_info.type_personal_info(browser, '#firstName', 'Alex')
    personal_info.type_personal_info(browser, '#lastName', 'Alekseev')
    personal_info.type_personal_info(browser, '#userEmail', 'alexalekseev@gmail.com')
    personal_info.type_personal_info(browser, '#userNumber', '8910123121')

    checkboxes.choose_gender(browser, '[name=gender]', 'Male')
    datepicker.pick_date(browser)
    subject.type_subject(browser, '#subjectsInput', 'History')
    checkboxes.choose_hobbies(browser, '[type=checkbox][id=hobbies-checkbox-3]+label', 'Music')

    upload_image.add_image(browser, '#uploadPicture', '../resources/Photo_test_yellow.png')

    adress.print_adress(browser, '#currentAddress', 'Delhi, Pyatnitskaya st 12/12')

    dropdown.city_state(browser, '#react-select-3-input', 'NCR')
    dropdown.city_state(browser, '#react-select-4-input', 'Delhi')

    button.button_submit(browser, '#submit')


def test_check_info_in_table():
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Alex Alekseev', 'alexalekseev@gmail.com', 'Male', '8910123121',
        '07 May,1991', 'History', 'Music', 'Photo_test_yellow.png', 'Delhi, Pyatnitskaya st 12/12', 'NCR Delhi'))
