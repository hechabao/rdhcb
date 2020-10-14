from time import sleep
from selenium import webdriver
import unittest2
# from
class MyTestCase(unittest2.TestCase):

    def setUp(self):

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Ie()

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        # time.sleep(10)
        # pass
        self.driver.quit()






