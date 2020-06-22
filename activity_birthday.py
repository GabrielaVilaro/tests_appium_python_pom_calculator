from activity_index import ActivityIndex
from appium.webdriver.common.touch_action import TouchAction

class ActivityBirthday(ActivityIndex):

    def __init__(self, driver):
        self.driver = driver
        self.button_next_activity = 'com.miui.calculator:id/iv_tab_life'
        self.button_years_old = ''
        self.button_date_of_birth = ''
        # selecciono dia , mes, año de nacimiento que quiero saber la edad
        self.button_select_date_of_bith_day = ''
        self.button_select_date_of_bith_month = ''
        self.button_select_date_of_bith_year = ''
        self.button_select_to_acept = 'android:id/button1'
        self.button_selec_date_today = ''
        # selecciono dia, mes, año de la fecha actual
        self.button_select_date_of_bith_day_today = ''
        self.button_select_date_of_bith_month_today = ''
        self.button_select_date_of_bith_year_today = ''
        self.button_select_to_acept_today = ''
        self.result_of_years_old = ''
        self.result_of_next_birthday = ''

    def scroling_date(self):
        actions = TouchAction(self.driver)
        actions.move_to(self.button_select_date_of_bith_day, 10, 100)
        actions.press(10, 100)
        actions.perform()

#heredo los métodos de activityIndex para no repetir
activityBirthday = ActivityBirthday()
activityBirthday.push_button()
activityBirthday.get_text()