import Services.utilities.driver_chrome_Trado as td
import Services.constractors.products_locators as pl


class ProductPage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def add_product_to_cart_click(self):
        td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((*pl.ProductLocators.add_product_btn,))).click()
