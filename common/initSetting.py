from appium import webdriver


def init_driver():
    capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "模拟器",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings"
    }

    # 设置启动名和包名
    # com.android.settings/.Settings

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

    driver.implicitly_wait(10)

    return driver


