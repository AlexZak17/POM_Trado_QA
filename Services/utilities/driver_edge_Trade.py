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


class EdgeDriver(unittest.TestCase):

    def setUp(self):
        self.my_driver = webdriver.Edge()
        self.my_driver.get('https://qa.trado.co.il/')
        self.my_driver.maximize_window()
        self.my_driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/span').click()

    def tearDown(self):
        sleep(1)
        self.my_driver.quit()