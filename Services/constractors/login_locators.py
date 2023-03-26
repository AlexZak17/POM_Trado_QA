import Services.utilities.driver_chrome_Trado as td


class LoginLocators(object):
    phone_field = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    login_button = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/input')
    code_input = (td.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    p_v_button = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/input')