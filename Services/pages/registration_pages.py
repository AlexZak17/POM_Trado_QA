import Services.utilities.driver_chrome_Trado as td
import Services.constractors.registration_locators as rl
import random


class RegistrationPage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def regi_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.registration_btn,))).click()

    def send_phone_num_valid(self):
        digits = ''.join([str(random.randint(0, 9)) for i in range(7)])
        phone_number = '057' + digits
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.phone_field,))).send_keys(phone_number)

    def send_phone_num_invalid(self):
        digits = ''.join([str(random.randint(0, 9)) for i in range(5)])
        phone_number = '0' + digits
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.phone_field,))).send_keys(phone_number)

    def send_privet_company_numbers_valid(self):
        num = ''.join([str(random.randint(0, 9)) for i in range(7)])
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.privet_company_filed,))).send_keys(num)

    def terms_of_use_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.terms_of_use_btn,))).click()

    def join_mailing_lst_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.mailing_lst_btn,))).click()

    def done_regi_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.registration_done_btn,))).click()

    def twitter_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.twitter_btn,))).click()

    def google_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.google_btn,))).click()

    def facebook_btn_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*rl.RegistrationLocators.facebook_btn,))).click()