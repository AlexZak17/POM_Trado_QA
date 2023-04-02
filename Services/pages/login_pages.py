import Services.utilities.driver_chrome_Trado as td
import Services.constractors.login_locators as llc
from Services.utilities.Trado_DB import alex_SMS_code
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def send_valid_phone_number(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.phone_field,))).send_keys('0527088611')

    def send_invalid_phone_number(self, invalid_phone_number):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.phone_field,))).send_keys(invalid_phone_number)

    def login_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.login_button,))).click()

    def input_valid_code(self):
        my_code = alex_SMS_code()
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.code_input,))).send_keys(my_code)
        td.sleep(2)

    def confirm_code_button_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.confirm_code_button,))).click()

    def disconnect_btn_click(self):
        menu = self.my_driver.find_element(td.By.CLASS_NAME, "header_logOut")
        hidden_submenu = self.my_driver.find_element(td.By.CLASS_NAME, "header_logOut")
        actions = ActionChains(self.my_driver)
        actions.move_to_element(menu)
        actions.click(hidden_submenu)
        actions.perform()

    def google_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.google_btn,))).click()

    def facebook_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.facebook_btn,))).click()

    def remember_me_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.remember_me_btn,))).click()


