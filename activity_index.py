from selenium.webdriver.common.by import By

class ActivityIndex:

    def __init__(self, driver):
        self.driver = driver
        # al abrir la app aparece un cartel de términos y condiciones que hay que seleccionar para poder continuar
        self.button_tyc = (By.ID, 'android:id/button1')
        self.button_clear = (By.ID, 'com.miui.calculator:id/btn_c_s')
        self.button_seven = (By.ID, 'com.miui.calculator:id/btn_7_s')
        self.button_two = (By.ID, 'com.miui.calculator:id/btn_2_s')
        self.button_sum = (By.ID, 'com.miui.calculator:id/btn_plus_s')
        self.button_equal = (By.ID, 'com.miui.calculator:id/btn_equal_s')
        # resultado de la operación
        self.result = (By.ID, 'com.miui.calculator:id/result')

    def push_button(self):
        self.driver.find_element(self.button_tyc).click()
        self.driver.find_element(self.button_clear).click()
        self.driver.find_element(self.button_seven).click()
        self.driver.find_element(self.button_sum).click()
        self.driver.find_element(self.button_two).click()
        self.driver.find_element(self.button_equal).click()

    def get_text(self):
        return self.driver.find_element(self.result).text