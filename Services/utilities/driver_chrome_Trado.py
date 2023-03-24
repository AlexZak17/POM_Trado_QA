from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
import allure


class Drivers:

    def get_chrome_driver(self):
        self.my_driver = webdriver.Chrome()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def tearDown(self):
        sleep(1)
        self.my_driver.quit()
