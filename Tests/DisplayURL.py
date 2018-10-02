from selenium import webdriver
import time
import unittest
from Pages.LoginPage import Loginpage
from Pages.Addtint import Addtint


class Addtinttest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def add_tint(self):
        driver = self.driver
        driver.get('https://www.tintup.com')
        driver.find_element_by_id('login').click()
        driver.find_element_by_tag_name('h2')

        login = Loginpage(driver)
        login.enter_username("qatesting+employeeplan@tintup.com")
        login.enter_password("welcome")
        login.click_login()

        time.sleep(5)

        addtint = Addtint(driver)
        addtint.click_addtint()
        addtint.add_tint_name("autotest4")
        addtint.create_tint()
        addtint.skip_to_tinteditor()
        time.sleep(5)
        addtint.click_networks()
        addtint.connect_youtube()
        addtint.enter_youtube_username("ucla")
        addtint.add_youtube()
        time.sleep(5)

    @classmethod
    def tearDown(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test completed")