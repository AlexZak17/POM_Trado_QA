import allure
import Services.utilities.driver_chrome_Trado as td
import Services.pages.home_page as hp
import Services.constractors.login_locators as llc
import Services.pages.login_pages as lp
import Services.constractors.home_page_locators as hpl


class TestHomePage(td.ChromeDriver, hp.HomePage, hp.PopUpWindows, lp.LoginPage):

    @allure.description('this test checks if the user can search product at the first time he entered the site')
    def test_1_search_bar_valid_first_focus(self):
        hp.HomePage.search_bar_send_keys(self, 'אק')
        td.sleep(2)
        assert self.my_driver.find_element(*hpl.HeaderLocators.first_search_res,).is_displayed()

    @allure.description('this test checks if the search bar gives us valid drop down, in this example I searched for product that called אקדיה so I started with writing אק and expected to see the first product at my drop down to start with אק')
    def test_2_search_bar_valid(self):
        hp.HomePage.search_bar_send_keys(self, 'אק')
        hp.HomePage.click_on_search_bar(self)
        td.sleep(2)
        assert "אק" in self.my_driver.find_element(*hpl.HeaderLocators.first_search_res,).get_attribute('textContent')

    @allure.description('this test checks if the search bar gives us valid drop down, in this example I searched for product that is not exsist so I started with writing AJLSGF78fo78eW and expected to see nothing in drop down = 0 results')
    def test_3_search_bar_invalid(self):
        hp.HomePage.search_bar_send_keys(self, 'AJLSGF78fo78eW')
        hp.HomePage.click_on_search_bar(self)
        td.sleep(2)
        assert "0" in self.my_driver.find_element(*hpl.HeaderLocators.zero_results,).get_attribute('innerText')

    @allure.description('test that check the functtion of the logo if it is clickable')
    def test_4_logo(self):
        hp.HomePage.logo_button_click(self)
        assert self.my_driver.current_url == 'https://qa.trado.co.il/'

    @allure.description('test that checks if I can get access to connect to the site')
    def test_5_hello_guest_button(self):
        hp.HomePage.hello_guest_button_click(self)
        assert self.my_driver.find_element(*llc.LoginLocators.phone_field,)

    def test_6_sales_btn(self):
        td.sleep(2)
        assert "מבצעים" in self.my_driver.find_element(td.By.CLASS_NAME, 'productsList_sectionName').get_attribute('textContent')






