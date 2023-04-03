import Services.utilities.driver_chrome_Trado as td
import Services.pages.home_page as hp
import Services.pages.login_pages as lp
import Services.pages.checkout_process_pages as cp


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
        cp.Checkout.write_valid_num_for_card(self)


