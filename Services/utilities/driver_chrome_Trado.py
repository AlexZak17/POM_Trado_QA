from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
import allure


def test_get_chrome_driver():
    my_driver = webdriver.Chrome()
    my_driver.get('https://qa.trado.co.il/')
    my_driver.maximize_window()
    assert my_driver.current_url == 'https://qa.trado.co.il/'


test_get_chrome_driver()
