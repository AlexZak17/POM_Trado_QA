import Services.utilities.driver_chrome_Trado as td
import Services.pages.products_pages as pp


class TestProduct(td.ChromeDriver, pp.ProductPage):
    def test_26_add_product_to_cart(self):
        self.my_driver.get('https://qa.trado.co.il/product/56586')
        pp.ProductPage.add_product_to_cart_click(self)
        assert "אקדיה" in td.WDW(self.my_driver, 5).until(td.EC.visibility_of_element_located((td.By.CLASS_NAME, 'inlineProduct_name'))).text

    def test_27_check_price(self):
        self.my_driver.get('https://qa.trado.co.il/product/56586')
        pp.ProductPage.add_product_to_cart_click(self)

