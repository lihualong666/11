from page.display_page import DisplayPage
from page.more_page import MorePage
from page.network_page import NetworkPage
from page.search_page import SearchPage
from page.setting_page import SettingPage


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def setting_page(self):
        """设置页面"""
        return SettingPage(self.driver)

    @property
    def more_page(self):
        """更多页面"""
        return MorePage(self.driver)

    @property
    def network_page(self):
        """网络设置页面"""
        return NetworkPage(self.driver)

    @property
    def display_page(self):
        """显示页面"""
        return DisplayPage(self.driver)

    @property
    def search_page(self):
        """搜索页面"""
        return SearchPage(self.driver)