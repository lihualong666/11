from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base_page import BasePage


class SearchPage(BasePage):
    search_bar = page.search_bar
    back_btn = page.back_btn

    def input_search_bar(self, txt):
        # 点击搜索框
        # self.driver.find_element_by_id('android:id/search_src_text').send_keys('hello')
        # self.driver.find_element(self.search_bar[0], self.search_bar[1]).send_keys('hello')
        # self.find_element_function(self.search_bar).send_keys('hello')
        self.input_func(self.search_bar, txt)

    def click_back_btn(self):
        # 点击返回按钮
        # self.driver.find_element_by_class_name('android.widget.ImageButton').click()
        # self.driver.find_element(self.back_btn[0], self.back_btn[1]).click()
        # self.find_element_function(self.back_btn).click()
        self.click_func(self.back_btn)