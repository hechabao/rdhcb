from ddt import ddt, data, unpack, file_data
import unittest2
from time import sleep
from func.feedback_method import weishu_shengchenqi
from func.get_screenshot import Get_Screenshot
from base.myTestCase import MyTestCase
from page_object.test_register_Page import test_Register_Page
from page_object.test_zhifuceshi import zhifu_tests
# from selenium import webdriver
from func.read_CSV import read
from func.log import Logger

chongzhi_wsxz = read('chongzhi.csv')


@ddt
class testzhifu(MyTestCase):

    def text_panduanzh(self):
        """测试账号输入框是否存在内容

        :return:
        """
        mylogger = Logger(logger='测试账号输入框是否存在内容').getlog()
        mylogger.info("登录'sj17600446278@163.com','a123456'")
        test_Register_Page(self.driver).login('sj17600446278@163.com', 'a123456')
        mylogger.info("进入积分充值")
        zhifu_tests(self.driver).jinruf()
        mylogger.info("查看账号内是否有值")
        try:
            self.assertEqual(zhifu_tests(self.driver).zhanghao_huoquf(), '有', msg='账号框里无内容')
        except:
            Get_Screenshot(self.driver, '账号框里无内容')
            mylogger.info("用例执行失败已截图")
            raise

    def test_weishu_dian_queding(self):
        """测试提示未输入充值积分

        :return:
        """
        mylogger = Logger(logger='测试账号输入框是否存在内容').getlog()
        mylogger.info("登录'sj17600446278@163.com','a123456'")
        test_Register_Page(self.driver).login('sj17600446278@163.com', 'a123456')
        mylogger.info("进入积分充值")
        zhifu_tests(self.driver).jinruf()
        mylogger.info("点确定")
        sleep(1)
        zhifu_tests(self.driver).dian_queding()
        mylogger.info("判断提示")
        try:

            self.assertEqual(zhifu_tests(self.driver).tishi(), '您还未输入充值积分1', msg='未提示未输入充值积分')
            mylogger.info("成功")
        except:
            # mylogger.info("用例执行失败已截图")
            Get_Screenshot(self.driver, '未提示未输入充值积分')
            mylogger.info("用例执行失败已截图")
            raise

    @data(*chongzhi_wsxz)
    @unpack
    def test_jifen_jine(self, name, zhanghao, mimai, names1, names2, name21, names3, names4, names5, neirong, yuji,
                        wenti, erji, weizhi, kuang):
        """%s

        :return:
        """ % name
        mylogger = Logger(logger='name').getlog()
        mylogger.info(names1)
        test_Register_Page(self.driver).login(zhanghao, mimai)
        mylogger.info(names2)
        zhifu_tests(self.driver).jinruf()
        mylogger.info(name21)
        sleep(1)
        zhifu_tests(self.driver).dian_weizhi('积分充值', '请输入充值积分', '1')
        mylogger.info(names3)
        sleep(1)
        zhifu_tests(self.driver).dian_weizhi(erji, weizhi, weishu_shengchenqi(int(neirong)))
        mylogger.info(names4)
        try:
            print(zhifu_tests(self.driver).huoqu_dian_weizhi(erji, kuang), (int(yuji)))
            self.assertEqual(len(zhifu_tests(self.driver).huoqu_dian_weizhi(erji, kuang)), (int(yuji)), msg=wenti)
            mylogger.info(names5)
        except:
            mylogger.info(wenti)
            Get_Screenshot(self.driver, wenti)
            mylogger.info("用例执行失败已截图")
            raise


if __name__ == '__main__':
    unittest2.main()
