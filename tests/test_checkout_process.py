import Services.utilities.driver_chrome_Trado as td
import Services.pages.home_page as hp
import Services.pages.login_pages as lp
import Services.pages.checkout_process_pages as cp
import Services.constractors.home_page_locators as hl


class TestCheckout(td.ChromeDriver, hp.HomePage, lp.LoginPage, cp.Checkout):
    def test_add_payment_method(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.send_valid_phone_number(self)
        lp.LoginPage.login_btn_click(self)
        lp.LoginPage.input_valid_code(self)
        lp.LoginPage.confirm_code_button_click(self)
        td.sleep(2)
        hp.HomePage.hello_guest_button_click(self)
        cp.Checkout.add_card_click(self)
        self.my_driver.switch_to.frame('yaadFrame')
        cp.Checkout.write_valid_num_for_card(self)
        cp.Checkout.write_valid_num_for_id(self)
        cp.Checkout.write_valid_date(self)
        cp.Checkout.write_valid_cvv(self)
        cp.Checkout.submit_btn_click(self)
        self.my_driver.switch_to.parent_frame()
        td.sleep(5)
        assert td.WDW(self.my_driver, 5).until_not(td.EC.element_to_be_clickable((*hl.HeaderLocators.search_bar,)))



