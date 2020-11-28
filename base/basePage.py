# 驱动类
class BasePage():
    # 初始化驱动和项目地址
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://check.rongdasoft.com/'

    # 自定义全局element单元素定位方法
    def find_URL_element(self, loc):
        return self.driver.find_element(*loc)

    # 自定义多元素方法
    def find_URL_elements(self, loc):
        return self.driver.find_elements(*loc)
