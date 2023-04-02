import allure
import Services.utilities.driver_chrome_Trado as td
import Services.pages.home_page as hp
import Services.pages.registration_pages as rp


class TestRegistration(td.ChromeDriver, hp.HomePage, rp.RegistrationPage):
    def test_11_connect_process_valid(self):
        hp.HomePage.hello_guest_button_click(self)
        rp.RegistrationPage.regi_btn_click(self)
        rp.RegistrationPage.send_phone_num_valid(self)
        rp.RegistrationPage.send_privet_company_numbers_valid(self)
        rp.RegistrationPage.terms_of_use_btn_click(self)
        rp.RegistrationPage.join_mailing_lst_btn_click(self)
        rp.RegistrationPage.done_regi_btn_click(self)
