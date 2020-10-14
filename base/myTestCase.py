from time import sleep
from selenium import webdriver
import unittest2
class MyTestCase(unittest2.TestCase):
    # 所有用例前置条件
    def setUp(self):
        # --页面隐藏运行
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)

        # --页面显示运行
        self.driver = webdriver.Chrome()# 谷歌驱动
        # self.driver = webdriver.Firefox()# firefox(驱动)
        # self.driver = webdriver.Ie()# ie(驱动)

        self.driver.implicitly_wait(10)#初始化
        self.driver.maximize_window()#

    # 所有用例执行后调用的方法
    def tearDown(self):
        # time.sleep(10)
        # pass
        self.driver.quit()






