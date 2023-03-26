import Services.utilities.driver_chrome_Trado as td
import Services.pages.home_page as hp
import Services.constractors.login_locators as llc
import Services.pages.login_pages as lp


class TestHomePage(td.Drivers, hp.HomePage, hp.PopUpWindows, lp.LoginPage):

    def test_search_bar_valid_first_focus(self):
        hp.HomePage.search_bar_send_keys(self, 'אק')

        self.assertTrue(hp.HomePage.vi_of_search_result(self))

    def test_search_bar_valid(self):
        hp.HomePage.search_bar_send_keys(self, 'אק')
        hp.HomePage.clear_search_bar(self)
        hp.HomePage.search_bar_send_keys(self, 'אק')
        hp.HomePage.vi_of_search_result(self)

    def test_logo(self):
        hp.HomePage.logo_button_click(self)
        assert self.my_driver.current_url == 'https://qa.trado.co.il/'

    def test_hello_guest_button(self):
        hp.HomePage.hello_guest_button_click(self)
        hp.PopUpWindows.choose_cocktail(self)
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.wait_until_phone_field_is_displayed(self)
        assert self.my_driver.find_element(*llc.LoginLocators.phone_field,)