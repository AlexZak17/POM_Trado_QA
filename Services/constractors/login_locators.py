import Services.utilities.driver_chrome_Trado as td


class LoginLocators(object):
    phone_field = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    login_button = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/input')
    code_input = (td.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    confirm_code_button = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/input')
    logged_in_check = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/a[1]/span[1]')
    phone_numer_error = (td.By.CLASS_NAME, 'form_message')
    invalid_phone_number_msg = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/div')
    disconnect_btn = (td.By.CLASS_NAME, 'header_logOut')
    connect_btn = (td.By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/a[1]/span[1]')
    google_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[3]/div[1]/button')
    facebook_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[3]/div[1]/span/button')