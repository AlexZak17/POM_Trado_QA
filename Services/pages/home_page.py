import Services.utilities.driver_chrome_Trado as td
import Services.constractors.home_page_locators as hl


class HomePage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def logo_button_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.logo_button,)))

    def search_bar_send_keys(self, keys):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.search_bar,))).click()
        td.sleep(2)
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.search_bar,))).send_keys(keys)
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.search_bar,))).send_keys(td.Keys.RETURN)

    def vi_of_search_result(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.first_search_res,)))

    def clear_search_bar(self):
         td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.search_bar,))).clear()
         td.sleep(2)

