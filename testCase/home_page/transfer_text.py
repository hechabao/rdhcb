from ddt import ddt, data, unpack
import unittest2
# from time import sleep
from base.myTestCase import MyTestCase
# from func.get_screenshot import Get_Screenshot
# from func.read_CSV import read
from func.Transfer_files import wenjianlujin
from page_object.test_register_Page import test_Register_Page
from page_object.test_transfer_files_Page import wenjian

# from func.log import Logger
# # mylogger = Logger(logger='上传文件').getlog()
# import page_object.transfer_files_Page不能有空格
# import page_object.test_register_Page
hhh = wenjianlujin()


@ddt
class test_cwj(MyTestCase):
    @data(*hhh)
    @unpack
    def test_chuanwenjians(self, i, n):
        print(i, n)
        rp = test_Register_Page(self.driver)
        rp.login('hcb@test.com', 'hcb123')
        rp.click_shenbaohecha()
        zhinenga = wenjian(self.driver)
        zhinenga.zhineng(i, n)
        # zhinenga.putong(name_url)


if __name__ == '__main__':
    unittest2.main()
