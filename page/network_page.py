from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base_page import BasePage



class NetworkPage(BasePage):
    first_mobileStyle = page.first_mobileStyle
    twoG_btn = page.twoG_btn
    threeG_btn = page.threeG_btn

    def click_first_mobileStyle(self):
        # 点击搜索框
        # self.driver.find_element_by_xpath('//*[contains(@text, "首选网络类型")]').click()
        # self.find_element_function(self.first_mobileStyle).click()
        self.click_func(self.first_mobileStyle)
        sleep(3)

    def click_2G_btn(self):
            # 点击返回按钮
        # self.driver.find_element_by_xpath('//*[contains(@text, "2G")]').click()  # 2G
        #     self.find_element_function(self.twoG_btn).click()
        self.click_func(self.twoG_btn)

    def click_3G_btn(self):
        # 点击返回按钮
        # self.driver.find_element_by_xpath('//*[contains(@text, "3G")]').click()  # 2G
        # self.find_element_function(self.threeG_btn).click()
        self.click_func(self.threeG_btn)