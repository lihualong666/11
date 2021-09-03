
from selenium.webdriver.common.by import By

import page
from base.base_page import BasePage



class MorePage(BasePage):

    mobile_btn= page.mobile_btn

    def click_mobile_btn(self):

        self.click_func(self.mobile_btn)
