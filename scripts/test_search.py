from time import sleep
from appium import webdriver

from common.initSetting import init_driver
from page.display_page import DisplayPage
from page.page_factor import Page
from page.search_page import SearchPage
from page.setting_page import SettingPage


class TestSetting(object):

    # 初始设置
    def setup(self):
        self.driver = init_driver()
        # self.setting_page = SettingPage(self.driver)  # 设置页面
        # self.display_page = DisplayPage(self.driver)  # 显示页面
        # self.searchpage = SearchPage(self.driver)# 搜索页面

        self.page= Page(self.driver)

    # 结束测试类
    # 123456
    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.page.setting_page.click_display()
        self.page.display_page.click_search_btn()
        self.page.search_page.input_search_bar('hello')
        self.page.search_page.click_back_btn()







