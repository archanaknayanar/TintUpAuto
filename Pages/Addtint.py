class Addtint():

    def __init__(self,driver):
        self.driver = driver

        self.add_tint_button_class_name = "top-btn-container"
        self.add_tint_name_id = "newTintUsername"
        self.create_tint_class_name = "input-group-btn"
        self.skip_to_tint_editor_class_name = "modal-footer"
        self.networks_link_text = "content-panel-network-content"
        self.connect_youtube_class_name = "fab fa-youtube"
        self.youtube_username_class_name = "input-group"
        self.add_youtube_class_name = "icon-white fas fa-plus"


    def click_addtint(self):
        self.driver.find_element_by_xpath(self.add_tint_button_class_name).click()


    def add_tint_name(self,tintname):
        self.driver.find_element_by_id(self.add_tint_name_id).send_keys(tintname)


    def create_tint(self):
        self.driver.find_element_by_xpath(self.create_tint_class_name).click()


    def skip_to_tinteditor(self):
        self.driver.find_element_by_xpath(self.skip_to_tint_editor_class_name).click()


    def click_networks(self):
        self.driver.find_element_by_link_text(self.networks_link_text).click()


    def connect_youtube(self):
        self.driver.find_element_by_class_name(self.connect_youtube_class_name).click()


    def enter_youtube_username(self,youtubeusername):
        self.driver.find_element_by_xpath(self.youtube_username_class_name).send_keys(youtubeusername)


    def add_youtube(self):
        self.driver.find_element_by_xpath(self.add_youtube_class_name).click()


