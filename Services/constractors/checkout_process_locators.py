import Services.utilities.driver_chrome_Trado as td


class CheckoutLocators(object):
    add_card_btn = (td.By.CLASS_NAME, 'userCardsList_addCardBtn')
    card_numbers_field = (td.By.ID, 'credit-card-input')
    id_for_card = (td.By.ID, 'userId-input')
    date_month_5 = (td.By.XPATH, '//*[@id="expmonth"]/option[6]')
    date_year_2024 = (td.By.XPATH, '//*[@id="expyear"]/option[3]')
    cv_field = (td.By.ID, 'cvv')
    Submit_payment_method_btn = (td.By.ID, 'btnSubmit')
