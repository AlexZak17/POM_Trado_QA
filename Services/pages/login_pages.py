import Services.utilities.driver_chrome_Trado as td
import Services.constractors.login_locators as llc
from Services.utilities.Trado_DB import alex_SMS_code
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def wait_until_phone_field_is_displayed(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.phone_field,)))

    def input_valid_code(self):
        my_code = alex_SMS_code()
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.code_input,))).send_keys(my_code)
        td.sleep(2)

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


