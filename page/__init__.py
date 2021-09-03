from selenium.webdriver.common.by import By

# 设置页面
display = By.XPATH, '//*[contains(@text, "显示")]'
more_btn = By.XPATH, '//*[contains(@text, "更多")]'

# 更多页面

mobile_btn = By.XPATH, '//*[contains(@text, "移动网络")]'


# 网络设置
first_mobileStyle = By.XPATH, '//*[contains(@text, "首选网络类型")]'
twoG_btn = By.XPATH, '//*[contains(@text, "2G")]'
threeG_btn = By.XPATH, '//*[contains(@text, "3G")]'

# 搜索展示页面
search_btn = By.ID, 'com.android.settings:id/search'# 搜索按钮

# 搜索页面
search_bar = By.ID, 'android:id/search_src_text'  # 搜索框
back_btn = By.CLASS_NAME, 'android.widget.ImageButton'  # 返回按钮