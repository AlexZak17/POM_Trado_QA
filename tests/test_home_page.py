import Services.utilities.driver_chrome_Trado as td
import Services.pages.home_page as hp


class TestHomePage(td.Drivers, hp.HomePage):

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
