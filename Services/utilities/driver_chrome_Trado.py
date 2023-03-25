from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
import allure
import unittest


class Drivers(unittest.TestCase):
    def setUp(self):
        self.my_driver = webdriver.Chrome()
        self.my_driver.get('https://qa.trado.co.il/')
        self.my_driver.maximize_window()
        yield
        self.my_driver.quit()



