import Services.utilities.driver_chrome_Trado as td
import Services.constractors.home_page_locators as hl
import Services.constractors.home_page_locators as hpl


class HomePage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def logo_button_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.logo_button,))).click()

    def search_bar_send_keys(self, keys):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.search_bar,))).send_keys(keys)

    def click_on_search_bar(self):
        HomePage.logo_button_click(self)
        td.sleep(2)
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.search_bar,))).click()

    def vi_of_search_result(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.first_search_res,)))

    def clear_search_bar(self):
         self.my_driver.find_element((*hl.HeaderLocators.search_bar,)).clear()

    def hello_guest_button_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.HeaderLocators.hello_guest_button,))).click()

    def search_drop_down(self):
        x = td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hpl.HeaderLocators.first_search_res,)))
        return x


class PopUpWindows:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def choose_cocktail(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.PopUpWindows.cocktail_button,))).click()
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*hl.PopUpWindows.button_save,))).click()
