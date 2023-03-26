import Services.utilities.driver_chrome_Trado as td
import Services.constractors.login_locators as llc


class LoginPage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def wait_until_phone_field_is_displayed(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*llc.LoginLocators.phone_field,)))