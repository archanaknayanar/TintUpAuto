from selenium import webdriver
import time
import unittest
from Pages.LoginPage import Loginpage
from Pages.HomePage import Homepage



class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://www.tintup.com')
        driver.find_element_by_id('login').click()
        driver.find_element_by_tag_name('h2')

        login = Loginpage(driver)
        login.enter_username("archana+qa@tintup.com")
        login.enter_password("welcome")
        login.click_login()

        homePage = Homepage(driver)
        homePage.click_settings_dropdown()
        homePage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")