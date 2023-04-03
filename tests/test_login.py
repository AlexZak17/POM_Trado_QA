import allure
import Services.utilities.driver_chrome_Trado as td
import Services.pages.home_page as hp
import Services.constractors.login_locators as llc
import Services.pages.login_pages as lp


class TestLogin(td.ChromeDriver, hp.HomePage, lp.LoginPage):
    @allure.description('test that checks if the user can login to site with valid user phone number')
    @allure.severity('Critical')
    def test_16_login_valid(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.send_valid_phone_number(self)
        lp.LoginPage.login_btn_click(self)
        lp.LoginPage.input_valid_code(self)
        lp.LoginPage.confirm_code_button_click(self)
        td.sleep(5)
        assert self.my_driver.find_element(*llc.LoginLocators.logged_in_check,).text == "אזור אישי"

    @allure.description('test that checks that the user can not login to site with invalid user phone number')
    @allure.severity('Critical')
    def test_17_login_invalid(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.send_invalid_phone_number(self, '0542563451')
        lp.LoginPage.login_btn_click(self)
        td.sleep(2)
        assert self.my_driver.find_element(*llc.LoginLocators.phone_numer_error,).text == 'No Such User Please Register'

    @allure.description('test that checks if the user can not login to site with invalid phone number')
    @allure.severity('Critical, sanity')
    def test_19_phone_field_invalid(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.send_valid_phone_number(self)
        lp.LoginPage.send_invalid_phone_number(self, 'aslfb54')
        lp.LoginPage.login_btn_click(self)
        assert "מס׳ טלפון לא תקין" in self.my_driver.find_element(*llc.LoginLocators.invalid_phone_number_msg,).get_attribute('textContent')

    @allure.description('test that checks if the user can logout from the site with valid user phone number')
    @allure.severity('medium')
    def test_20_sign_out(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.send_valid_phone_number(self)
        lp.LoginPage.login_btn_click(self)
        lp.LoginPage.input_valid_code(self)
        lp.LoginPage.confirm_code_button_click(self)
        td.sleep(5)
        lp.LoginPage.disconnect_btn_click(self)
        assert "התחברות" in self.my_driver.find_element(*llc.LoginLocators.connect_btn,).get_attribute('innerText')

    @allure.description('test that checks if the user can login to site by twitter')
    @allure.severity('High')
    def test_21_connection_by_twitter(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.twitter_btn_click(self)
        self.my_driver.get('about:blank')
        td.sleep(3)
        assert "accounts.twitter.com" in self.my_driver.find_element(td.By.XPATH, '/html/body').get_attribute('baseURI')

    @allure.description('test that checks if the user can login to site by google')
    @allure.severity('High')
    def test_22_connection_by_google(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.google_btn_click(self)
        self.my_driver.get('https://accounts.google.com/signin/oauth/error/v2?authError=ChVyZWRpcmVjdF91cmlfbWlzbWF0Y2gSkgIK15DXmdefINec15og15DXpNep16jXldeqINec15TXmdeb16DXoSDXnNeQ16TXnNeZ16fXpteZ15Qg15TXlteVINeb15kg15TXmdeQINec15Ag16LXldee15PXqiDXkdeT16jXmdep15XXqiDXnteT15nXoNeZ15XXqiBPQXV0aCAyLjAg16nXnCBHb29nbGUuCgrXkNedINeQ16ov15Qg15TXntek16rXly_XqiDXqdecINeU15DXpNec15nXp9em15nXlCwg16LXnNeZ15og15zXqNep15XXnSDXkS1Hb29nbGUgQ2xvdWQgQ29uc29sZSDXkNeqINee16fXldeoINeULUphdmFTY3JpcHQuCiAgGnVodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL2phdmFzY3JpcHQtaW1wbGljaXQtZmxvdyNhdXRob3JpemF0aW9uLWVycm9ycy1vcmlnaW4tbWlzbWF0Y2ggkAMqIAoGb3JpZ2luEhZodHRwczovL3FhLnRyYWRvLmNvLmlsMo4DCAESkgIK15DXmdefINec15og15DXpNep16jXldeqINec15TXmdeb16DXoSDXnNeQ16TXnNeZ16fXpteZ15Qg15TXlteVINeb15kg15TXmdeQINec15Ag16LXldee15PXqiDXkdeT16jXmdep15XXqiDXnteT15nXoNeZ15XXqiBPQXV0aCAyLjAg16nXnCBHb29nbGUuCgrXkNedINeQ16ov15Qg15TXntek16rXly_XqiDXqdecINeU15DXpNec15nXp9em15nXlCwg16LXnNeZ15og15zXqNep15XXnSDXkS1Hb29nbGUgQ2xvdWQgQ29uc29sZSDXkNeqINee16fXldeoINeULUphdmFTY3JpcHQuCiAgGnVodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL2phdmFzY3JpcHQtaW1wbGljaXQtZmxvdyNhdXRob3JpemF0aW9uLWVycm9ycy1vcmlnaW4tbWlzbWF0Y2g%3D&client_id=918041190286-ts0hq2o9fhq3adumgcj45a3vsp2fh8v9.apps.googleusercontent.com')
        td.sleep(3)
        assert self.my_driver.find_element(td.By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]').text != "שגיאה 400: redirect_uri_mismatch"

    @allure.description('test that checks if the user can login to site by facebook')
    @allure.severity('High')
    def test_23_connection_by_facebook(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.facebook_btn_click(self)
        self.my_driver.get("https://www.facebook.com/v2.3/dialog/oauth?app_id=356713278727771&auth_type=&cbt=1680078421795&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df5dcb328ae1a88%26domain%3Dqa.trado.co.il%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fqa.trado.co.il%252Fff5da19a3284fc%26relation%3Dopener&client_id=356713278727771&display=popup&domain=qa.trado.co.il&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fqa.trado.co.il%2F&locale=en_US&logger_id=f3f4826ddc37424&origin=1&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df36c7ccfd41bb14%26domain%3Dqa.trado.co.il%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fqa.trado.co.il%252Fff5da19a3284fc%26relation%3Dopener%26frame%3Df2686a781e7a2f8&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=false&scope=public_profile%2Cemail&sdk=joey&version=v2.3")
        td.sleep(3)
        assert 'facebook.com' in self.my_driver.current_url

    @allure.description('test that checks if the site remember me button works')
    @allure.severity('High')
    def test_24_remember_me_button(self):
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.send_valid_phone_number(self)
        lp.LoginPage.remember_me_btn_click(self)
        lp.LoginPage.login_btn_click(self)
        lp.LoginPage.input_valid_code(self)
        lp.LoginPage.confirm_code_button_click(self)
        td.sleep(5)
        lp.LoginPage.disconnect_btn_click(self)
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.send_valid_phone_number(self)
        lp.LoginPage.login_btn_click(self)
        self.assertIsNone(self.my_driver.find_element(*llc.LoginLocators.code_input,).is_displayed())

    @allure.description('test that checks visability of hebrew valid title')
    @allure.severity('Low, UI')
    def test_25_login_title_container(self):
        hp.HomePage.hello_guest_button_click(self)
        assert "ברוכים השבים! מתרגשים לראות אתכם כאן" in self.my_driver.find_element(*llc.LoginLocators.login__title,).text
