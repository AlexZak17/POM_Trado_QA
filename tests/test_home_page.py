import Services.utilities.driver_chrome_Trado as TD


class TestHomePage(TD.Drivers):
    def test_logo(self):
        
        assert self.my_driver.current_url == 'https://qa.trado.co.il/'
