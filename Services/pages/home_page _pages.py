import Services.utilities.driver_chrome_Trado as td
import Services.constractors.home_page_locators as hl


class HomePage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def logo_button_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.logo_button,)))