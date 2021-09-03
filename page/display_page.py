from selenium.webdriver.common.by import By

import page
from base.base_page import BasePage



class DisplayPage(BasePage):
    # search_btn = By.ID, 'com.android.settings:id/search'# 搜索按钮
    search_btn = page.search_btn


    def click_search_btn(self):
        # 点击搜索按钮

        self.click_func(self.search_btn)
        # sleep(3)
