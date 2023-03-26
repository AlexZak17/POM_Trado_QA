import allure
import Services.utilities.driver_chrome_Trado as td
import Services.pages.home_page as hp
import Services.constractors.login_locators as llc
import Services.pages.login_pages as lp


class TestHomePage(td.Drivers, hp.HomePage, hp.PopUpWindows, lp.LoginPage):

    @allure.description('this test checks if the user can search product at the first time he entered the site')
    def test_search_bar_valid_first_focus(self):
        hp.HomePage.search_bar_send_keys(self, 'אק')
        self.assertTrue(hp.HomePage.vi_of_search_result(self))

    @allure.description('this test checks if the search bar gives us valid drop down, in this example I searched for product that called אקדיה so I started with writing אק and expected to see the first product at my drop down to start with אק')
    def test_search_bar_valid(self):
        hp.PopUpWindows.choose_cocktail(self)
        hp.HomePage.search_bar_send_keys(self, 'אק')
        hp.HomePage.click_on_search_bar(self)
        td.sleep(2)
        assert "אק" in self.my_driver.find_element(td.By.XPATH, '/html/body/div/div/div[2]/header/div/div/div/div[1]/div/a[1]/div/div[2]/div[1]').get_attribute('textContent')

    @allure.description('test that check the functtion of the logo if it is clickable')
    def test_logo(self):
        hp.HomePage.logo_button_click(self)
        assert self.my_driver.current_url == 'https://qa.trado.co.il/'

    @allure.description('test that checks if I can get access to connect to the site')
    def test_hello_guest_button(self):
        hp.HomePage.hello_guest_button_click(self)
        hp.PopUpWindows.choose_cocktail(self)
        hp.HomePage.hello_guest_button_click(self)
        lp.LoginPage.wait_until_phone_field_is_displayed(self)
        assert self.my_driver.find_element(*llc.LoginLocators.phone_field,)

    