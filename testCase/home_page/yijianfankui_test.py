from ddt import ddt,data,unpack,file_data
import unittest2
from time import sleep
from func.feedback_method import weishu_shengchenqi,huoqu
from func.get_screenshot import Get_Screenshot
from base.myTestCase import MyTestCase
from page_object.test_register_Page import test_Register_Page
from page_object.test_yijianfankui import yijianss_tests
# from selenium import webdriver
from func.read_CSV import read
from func.log import Logger

wei_shu_xian_zhi = read('yijian-weishuxianzhi.csv')
hui_xian_zhanghao = read('yijian-huixianzhanghao.csv')
bi_tian_xiang = read('yijian-bitianxiang.csv')
xuan_ze_kuang_ceshi = read('yijian-xuan_ze_kuang_ceshi.csv')
@ddt
class testyonghu(MyTestCase):
    @data(*wei_shu_xian_zhi)
    @unpack
    def test_weishuxianzhi(self,name,zhanghao,mima,name1,name2,name3,name4,name5,yuqi,shibai,shuju,shurkuang,zhanghaoleix):
        """%s

        :return:
        """%name
        mylogger = Logger(logger=name).getlog()
        mylogger.info(name1)
        test_Register_Page(self.driver).login(zhanghao,mima)
        mylogger.info(name2)
        yijianss_tests(self.driver).user_jinglai()
        mylogger.info(name3)
        yijianss_tests(self.driver).panduanweizhi(weishu_shengchenqi(int(shuju)),shurkuang,'输入',zhanghaoleix)
        mylogger.info(name4)
        print(len(yijianss_tests(self.driver).panduanweizhi(int(shuju),shurkuang,'获取',zhanghaoleix)), yijianss_tests(self.driver).tishi())
        try:
            self.assertEqual(yijianss_tests(self.driver).tishi(), yuqi, msg='不提示位数限制')
            mylogger.info('提示验证成功')
            mylogger.info(name5)
            try:

                self.assertEqual(len(yijianss_tests(self.driver).panduanweizhi(int(shuju),shurkuang,'获取',zhanghaoleix)), (int(shuju)-1), msg='数据验证失败')
                mylogger.info('数据验证成功')
            except:
                shibai = '数据保存失败'
                raise
        except:
            mylogger.info(shibai)
            Get_Screenshot(self.driver, yuqi)
            raise

    @data(*hui_xian_zhanghao)
    @unpack
    def test_zhanghaohuixian(self,name,zhanghao,mima,name1,name2,name3,yuqi,cuowu,shuju,shurkuang,zhanghaoleix):
        """%s

        :return:
        """ % name
        mylogger = Logger(logger=name).getlog()
        mylogger.info(name1)
        test_Register_Page(self.driver).login(zhanghao, mima)
        mylogger.info(name2)
        yijianss_tests(self.driver).user_jinglai()
        mylogger.info(name3)
        try:
            self.assertEqual(yijianss_tests(self.driver).panduanweizhi(shuju, shurkuang, '获取', zhanghaoleix), zhanghao, msg=cuowu)
            mylogger.info('回显成功')
        except:
            mylogger.info(cuowu)
            Get_Screenshot(self.driver, cuowu)
            raise

    @data(*bi_tian_xiang)
    @unpack
    def test_bitianxiangtishi(self,name,zhanghao,mima,name1,name2,name3,name4,yanzheng,shuru,yuqi,cuowu,shurkuang,zhanghaoleix):
        """%s

        :return:
        """ % name
        mylogger = Logger(logger=name).getlog()
        mylogger.info(name1)
        test_Register_Page(self.driver).login(zhanghao, mima)
        mylogger.info(name2)
        yijianss_tests(self.driver).user_jinglai()
        mylogger.info(name3)
        yijianss_tests(self.driver).panduanweizhi(shuru, shurkuang, '输入', zhanghaoleix)
        mylogger.info(name4)
        yijianss_tests(self.driver).dian_querding()
        mylogger.info(yanzheng)
        try:
            self.assertEqual(yijianss_tests(self.driver).tishi(), yuqi,
                             msg=cuowu)
            mylogger.info('提示验证成功')
        except:
            mylogger.info(cuowu)
            Get_Screenshot(self.driver, cuowu)
            raise

    @data(*xuan_ze_kuang_ceshi)
    @unpack
    def test_bitianxiangtishi(self,name,zhanghao,mima,name1,name2,name3,name4,name5,name6,name7,yuqi,cuowu,shuju,leix,zhanghaolx):
        """%s

        :return:
        """ % name
        print(zhanghaolx)
        mylogger = Logger(logger=name).getlog()
        mylogger.info(name1)
        test_Register_Page(self.driver).login(zhanghao, mima)
        mylogger.info(name2)
        yijianss_tests(self.driver).user_jinglai()
        mylogger.info(name3)
        yijianss_tests(self.driver).panduanweizhi('哇哇哇', '机构名称', '输入', zhanghaolx)
        yijianss_tests(self.driver).panduanweizhi('哇哇哇', '联系人', '输入', zhanghaolx)
        mylogger.info(name4)
        yijianss_tests(self.driver).panduanweizhi(shuju,leix,'无','无')
        sleep(5)
        mylogger.info(name5)

        yijianss_tests(self.driver).dian_querding()

        try:
            mylogger.info(name6)
            self.assertEqual(yijianss_tests(self.driver).tishi2(), yuqi, msg='不提示提交成功')
            mylogger.info('提示验证成功')

            try:
                mylogger.info(name7)
                print(huoqu(leix,shuju),shuju)
                self.assertEqual(huoqu(leix,shuju), shuju ,msg='数据核实失败')
                mylogger.info('数据验证成功')
            except:
                cuowu = '数据保存失败'
                raise
        except:
            mylogger.info(cuowu)
            Get_Screenshot(self.driver, cuowu)
            raise

    def test_tuichu(self):
        """测试用户信息修改页点退出

        :return:
        """
        mylogger = Logger(logger='测试不修改内容点保存').getlog()
        mylogger.info("登录'sj17600446278@163.com','a123456'")
        test_Register_Page(self.driver).login('sj17600446278@163.com', 'a123456')
        mylogger.info("点修改用户信息")
        yijianss_tests(self.driver).user_jinglai()
        mylogger.info("点退出按钮")
        # print(user_tests(self.driver).nicheng_shuru_neirong(2))
        yijianss_tests(self.driver).dian_fanhui()
        sleep(2)
        try:
            self.assertEqual(yijianss_tests(self.driver).tuichuyanzheng(), '智能核查', msg='用户信息修改页不能退出首页')
            mylogger.info("退出成功")
        except:
            Get_Screenshot(self.driver, '用户信息修改页不能退出首页')
            raise
if __name__ == '__main__':
    unittest2.main()
