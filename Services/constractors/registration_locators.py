import Services.utilities.driver_chrome_Trado as td


class RegistrationLocators(object):
    registration_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[1]/span[2]')
    phone_field = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    privet_company_filed = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input')
    terms_of_use_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span')
    mailing_lst_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[4]/span')
    registration_done_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/input')
    twitter_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[3]/div[1]/div')
    google_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[3]/div[1]/button')
    facebook_btn = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[3]/div[1]/span/button')
    terms_of_use_msg = (td.By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[3]')
