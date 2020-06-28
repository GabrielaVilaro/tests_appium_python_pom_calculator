from appium import webdriver
import unittest
from activity_index import ActivityIndex

class Conection(unittest.TestCase):

    def setUp(self):
        self.driver = {
          "platformName": "Android",
          "platformVersion": "9",
          "deviceName": "lavender",
          "automationName": "UiAutomator1",
          "appPackage": "com.miui.calculator",
          "appActivity": "com.miui.calculator.cal.CalculatorActivity"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.driver)
        self.activity_index = ActivityIndex(self.driver)


    def test_one_result(self):
        self.activity_index.push_button()
        self.assertEqual(self.activity_index.get_text(), '= 9')

if __name__ == '__main__':
    unittest.main()