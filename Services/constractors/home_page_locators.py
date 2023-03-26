import Services.utilities.driver_chrome_Trado as td


class HeaderLocators(object):
    logo_button = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/a[2]/div')
    search_bar = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div/span/input')
    first_search_res = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div/div[1]/div/a[1]/div')