import Services.utilities.driver_chrome_Trado as td
import Services.constractors.checkout_process_locators as cl


class Checkout:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def add_card_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*cl.CheckoutLocators.add_card_btn,))).click()

    def write_valid_num_for_card(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*cl.CheckoutLocators.card_numbers_field,))).send_keys('4580000000000000')