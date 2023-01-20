from selene.support.shared import browser
from practice_form import page_objects


def test_practice_form(size_browser):
    browser.open('https://demoqa.com/automation-practice-form')

    page_objects.hide_adv()

    page_objects.type_personal_info('Alex', 'Alekseev', 'alexalekseev@gmail.com', '8910123121')
    page_objects.radio_button_gender('Male')

    page_objects.click_data()
    page_objects.select_month('May')
    page_objects.select_year('1991')
    page_objects.select_day('7')

    page_objects.type_subject('History')
    page_objects.checkbox_hobby('Music')

    page_objects.upload_img('tests/resources/Photo_test_yellow.png')

    page_objects.type_address('Delhi, Pyatnitskaya st 12/12')
    page_objects.dropdown_state('NCR')
    page_objects.dropdown_city('Delhi')

    page_objects.button_submit()


def test_check_info_table():
    page_objects.check_form('Alex Alekseev', 'alexalekseev@gmail.com', 'Male', '8910123121',
        '07 May,1991', 'History', 'Music', 'Photo_test_yellow.png', 'Delhi, Pyatnitskaya st 12/12', 'NCR Delhi')

