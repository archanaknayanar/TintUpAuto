from selenium import webdriver
import time
import unittest
from Pages.LoginPage import Loginpage


class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_invalid(self):
        driver = self.driver
        driver.get('https://www.tintup.com')
        driver.find_element_by_id('login').click()
        driver.find_element_by_tag_name('h2')

        login = Loginpage(driver)
        login.enter_username("archana+collab1@tintup.com")
        login.enter_password("Welcome123")
        login.click_login()
        time.sleep(5)


        element = driver.find_element_by_id('flash_alert')
        print(element.text)


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

