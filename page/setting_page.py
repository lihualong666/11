from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base_page import BasePage


class SettingPage(BasePage):

    more= page.more
    display= page.display


    def click_more_btn(self):
        """点击更多"""

        self.click_func(self.more)

    def click_display(self):
        """点击显示"""

        self.click_func(self.display)
        sleep(3)