# PO base基类配置文件
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element_function(self, location, timeout=10, poll=1):
        # 元素定位方法
        # return self.driver.find_element(location[0], location[1])

        # 利用显示等待优化元素定位方法，找不到元素等问题
        element= WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(location[0], location[1]))

        return element


    # def find_elements_function(self, location, timeout=10, poll=1):
    #     # 元素定位方法
    #     # return self.driver.find_element(location[0], location[1])
    #
    #     # 利用显示等待优化元素定位方法，找不到元素等问题
    #
    #     return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(location[0], location[1]))

    def click_func(self,location):
        """定位元素点击方法的封装"""
        self.find_element_function(location).click()


    def input_func(self, location, txt):
        """定位元素的输入操作"""
        element= self.find_element_function(location)
        element.clear()
        element.send_keys(txt)


