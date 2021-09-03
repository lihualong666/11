
from appium import webdriver

from common.initSetting import init_driver
from page.more_page import MorePage
from page.network_page import NetworkPage
from page.page_factor import Page
from page.setting_page import SettingPage


class TestSetting(object):

    # 初始设置
    def setup(self):
        self.driver = init_driver()# 获取驱动对象

        # self.setting_page= SettingPage(self.driver)# 设置页面
        # self.more_page = MorePage(self.driver)  # 更多页面
        # self.network_page = NetworkPage(self.driver)  # 网络设置页面对象
        self.page = Page(self.driver)


    # 结束测试类
    def teardown(self):
        self.driver.quit()


    def test_2g(self):
        self.page.setting_page.click_more_btn() # 点击更多
        self.page.more_page.click_mobile_btn() # 点击移动网络

        self.page.network_page.click_first_mobileStyle()

        self.page.network_page.click_2G_btn()


    def test_3g(self):
        self.page.setting_page.click_more_btn()  # 点击更多
        self.page.more_page.click_mobile_btn()  # 点击移动网络
        self.page.network_page.click_first_mobileStyle()

        self.page.network_page.click_3G_btn()





