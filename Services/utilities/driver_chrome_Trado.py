from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
import unittest
import Services.pages.home_page as hp


class ChromeDriver(unittest.TestCase, hp.PopUpWindows):

    def setUp(self):
        self.my_driver = webdriver.Chrome()
        self.my_driver.get('https://qa.trado.co.il/')
        self.my_driver.maximize_window()
        hp.PopUpWindows.choose_cocktail(self)

    def tearDown(self):
        sleep(1)
        self.my_driver.quit()







