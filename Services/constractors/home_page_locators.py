import Services.utilities.driver_chrome_Trado as td


class HeaderLocators(object):
    logo_button = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/a[2]/div')
    search_bar = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div/span/input')
    first_search_res = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div/div[1]/div/a[1]/div/div[2]/div[1]')
    hello_guest_button = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/a[1]')
    zero_results = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div/div[1]/h3')


class PopUpWindows(object):
    cocktail_button = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    button_save = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    