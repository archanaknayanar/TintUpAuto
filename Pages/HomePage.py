class Homepage():

    def __init__(self,driver):
        self.driver = driver

        self.settings_dropdown_id = "settings_dropdown_toggle"
        self.logout_button_class_name = "refresh"



    def click_settings_dropdown(self):
        self.driver.find_element_by_id(self.settings_dropdown_id).click()

    def click_logout(self):
        self.driver.find_element_by_class_name(self.logout_button_class_name).click()


