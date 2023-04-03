import Services.utilities.driver_chrome_Trado as td


class CheckoutLocators(object):
    add_card_btn = (td.By.CLASS_NAME, 'userCardsList_addCardBtn')
    card_numbers_field = (td.By.NAME, 'CC')