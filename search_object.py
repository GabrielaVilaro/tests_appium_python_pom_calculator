from appium import webdriver
import unittest
from activity_index import ActivityIndex
from activity_birthday import ActivityBirthday

class Conection(unittest.TestCase):
    #pre-condiciones
    def setUp(self):
        self.driver = {
          "platformName": "Android",
          "platformVersion": "9",
          "deviceName": "lavender",
          "automationName": "UiAutomator2",
          "appPackage": "com.miui.calculator",
          "appActivity": "com.miui.calculator.cal.CalculatorActivity"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.driver)
        self.activity_index = ActivityIndex(self.driver)
        self.activity_birthday = ActivityBirthday(self.driver)


    def test_one_result(self):
        self.activity_index.push_button()
        self.assertEqual(self.activity_index.get_text(), '= 9')

    def test_years_old(self):
        self.activity_birthday.push_button()
        self.assertEqual(self.activity_birthday.get_text(), '')

    def test_next_birthday(self):
        self.activity_birthday.push_button()
        self.assertEqual(self.activity_birthday.get_text(), '')

    #post-condiciones
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()