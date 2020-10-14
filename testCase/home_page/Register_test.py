# from ddt import ddt,data,unpack,file_data
import unittest2
from time import sleep
from base.myTestCase import MyTestCase
from func.get_screenshot import Get_Screenshot
from func.read_CSV import read
from page_object.test_register_Page import test_Register_Page
from func.log import Logger

class TestLoginPage(MyTestCase):
    """登录页面测试

    :return:
    """
    def test_normal_login(self):
        """正常登录

        :return:
        """
        mylogger = Logger(logger='正常登录').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()#打开
        mylogger.info("打开浏览器")
        rp.input_username('sj17600446278@163.com')
        mylogger.info("输入账号")
        sleep(1)
        rp.input_password("a123456")
        mylogger.info("输入密码")
        sleep(2)
        rp.click_login_bth()
        mylogger.info("点击登录")
        try:
            self.assertEqual (rp.tishi(), '登录成功', msg='登录失败')
        except :
            Get_Screenshot(self.driver, '登录失败')
            raise

    def test_zhanhaocuowu_tishi(self):
        """错误账号登录

        :return:
        """
        mylogger = Logger(logger='错误账号登录').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()
        mylogger.info("打开浏览器")
        rp.input_username('sj17600@163.com')
        mylogger.info("输入账号")
        sleep(1)
        rp.input_password("a123456")
        mylogger.info("输入密码")
        sleep(2)
        jieguo = rp.click_login_bth()
        mylogger.info("点击登录")
        try:
            self.assertEqual(rp.click_shangcuan_bth(), '帐号不存在', msg='不提示账号不存在')
        except:
            Get_Screenshot(self.driver, '不提示账号不存在')
            raise
    def test_mimacuowu_tishi(self):
        """错误密码登录

        :return:
        """
        mylogger = Logger(logger='错误密码登录').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()
        mylogger.info("打开浏览器")
        rp.input_username('sj17600446278@163.com')
        mylogger.info("输入账号")
        sleep(1)
        rp.input_password("a123456123123")
        mylogger.info("输入密码")
        sleep(2)
        jieguo = rp.click_login_bth()
        mylogger.info("点击登录")
        try:
            self.assertEqual(rp.click_shangcuan_bth(), '密码输入错误，请重新输入', msg='不提示密码输入错误')
        except:
            Get_Screenshot(self.driver, '不提示密码输入错误')
            raise
    def test_zhanghaoweikong_tishi(self):
        """空账号登录

        :return:
        """
        mylogger = Logger(logger='空账号登录').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()
        mylogger.info("打开浏览器")
        rp.input_username('')
        mylogger.info("输入账号")
        sleep(1)
        rp.input_password("a123456123123")
        mylogger.info("输入密码")
        sleep(2)
        rp.click_login_bth()
        mylogger.info("点击登录")
        try:
            self.assertEqual(rp.click_shangcuan_bth(), '账号不能为空', msg='不提示账号不能为空')
        except:
            Get_Screenshot(self.driver, '不提示账号不能为空')
            raise
    def test_mimaweikong_tishi(self):
        """密码空登录

        :return:
        """
        mylogger = Logger(logger='密码空登录').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()
        mylogger.info("打开浏览器")
        rp.input_username('sj17600446278@163.com')
        mylogger.info("输入账号")
        sleep(1)
        rp.input_password('')
        mylogger.info("输入密码")
        sleep(2)
        rp.click_login_bth()
        mylogger.info("点击登录")
        try:
            self.assertEqual(rp.click_shangcuan_bth(), '密码不能为空', msg='不提示密码不能为空')
        except:
            Get_Screenshot(self.driver, '不提示密码不能为空')
            raise
    def test_yunxiezuo_tiaozhuan(self):
        """跳转云协作

        :return:
        """
        mylogger = Logger(logger='跳转云协作').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()
        mylogger.info("打开浏览器")
        n = rp.yunxiezuo()
        mylogger.info("点击云协作")
        try:
            self.assertEqual(n, 'http://cloud.rongdasoft.com/web/main', msg='跳转云协作失败')
        except:
            Get_Screenshot(self.driver, '跳转云协作失败')
            raise
    def test_erlangshen_tiaozhuan(self):
        """跳转二郎神

        :return:
        """
        mylogger = Logger(logger='跳转二郎神').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()
        mylogger.info("打开浏览器")
        n = rp.erlangshen()
        print(n)
        mylogger.info("点击二郎神")
        try:
            self.assertEqual(n, 'http://www.elangshen.com/', msg='跳转二郎神失败')
        except:
            Get_Screenshot(self.driver, '跳转二郎神失败')
            raise
    def test_wangjimimima_tiaozhuan(self):
        """跳转忘记密码

        :return:
        """
        mylogger = Logger(logger='跳转忘记密码').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()
        mylogger.info("打开浏览器")
        n = rp.wangjimima()
        print(n)
        mylogger.info("点击忘记密码")
        try:
            self.assertEqual(n, 'http://elangshen.com/toUpdateUserPwdOne', msg='跳转忘记密码失败')
        except:
            Get_Screenshot(self.driver, '跳转云协作失败')
            raise
    def test_zhuce_tiaozhuan(self):
        """跳转用户注册

        :return:
        """
        mylogger = Logger(logger='跳转用户注册').getlog()
        rp = test_Register_Page(self.driver)
        rp.open()
        mylogger.info("打开浏览器")
        n = rp.yonghuzhuce()
        print(n)
        mylogger.info("点击用户注册")
        try:
            self.assertEqual(n, 'http://elangshen.com/toUserRegisterOne?channel=hcb_web', msg='跳转用户注册失败')
        except:
            Get_Screenshot(self.driver, '跳转用户注册失败')
            raise
    # def tsst_kaishi_
if __name__ == '__main__':
    unittest2.main()