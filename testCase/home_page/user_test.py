from ddt import ddt, data, unpack, file_data
import unittest2
from time import sleep
from func.feedback_method import weishu_shengchenqi
from func.get_screenshot import Get_Screenshot
from base.myTestCase import MyTestCase
from page_object.test_register_Page import test_Register_Page
from page_object.text_user_Page import user_tests
# from selenium import webdriver
from func.read_CSV import read
from func.log import Logger

nichen = read('geren-nicen.csv')
mingzi = read('geren-mingzi.csv')
xingbie = read('geren-xingbie.csv')
gongsiname = read('geren-gongsiname.csv')
zhiyess = read('geren-gzhiyess.csv')
weishuxianzhi = read('geren-weishuxianzhi.csv')


@ddt
class testyonghu(MyTestCase):
    def txst_baocun(self):
        """测试不修改内容点保存

        :return:
        """
        mylogger = Logger(logger='测试不修改内容点保存').getlog()
        mylogger.info("登录'sj17600446278@163.com','a123456'")
        test_Register_Page(self.driver).login('sj17600446278@163.com', 'a123456')
        mylogger.info("点修改用户信息")
        user_tests(self.driver).user_jinglai()
        mylogger.info("点保存")
        # print(user_tests(self.driver).nicheng_shuru_neirong(2))
        user_tests(self.driver).baocun()
        sleep(2)
        try:
            self.assertEqual(user_tests(self.driver).tishi(), '个人资料修改成功', msg='不提示修改成功')
        except:
            Get_Screenshot(self.driver, '不提示修改成功')
            mylogger.info("用例执行失败已截图")
            raise

    @data(*nichen)
    @unpack
    def txst_nicheng(self, name, zhanghao, mimai, neirong, names1, names2, names3, names4, names5, yuji, wenti):
        """%s

        :return:
        """ % name
        mylogger = Logger(logger=name).getlog()
        # '0-6'
        mylogger.info(names1)
        test_Register_Page(self.driver).login(zhanghao, mimai)
        mylogger.info(names2)
        user_tests(self.driver).user_jinglai()
        mylogger.info(names3)
        if neirong == '':
            user_tests(self.driver).shurujong()
        else:
            user_tests(self.driver).xiugai_name(neirong)
        if names4 == '点保存':
            mylogger.info(names4)
            user_tests(self.driver).baocun()
            try:
                # print(user_tests(self.driver).nicheng_shuru_neirong())
                mylogger.info(names5)
                self.assertEqual(user_tests(self.driver).tishi(), yuji, msg=wenti)
                mylogger.info('保存交互正常')
                try:
                    self.assertEqual(user_tests(self.driver).nicheng_shuru_neirong(0), neirong, msg='不提示修改成功')
                    mylogger.info('保存数据正常')
                except:
                    wenti = '数据保存失败'
                    raise
            except:
                mylogger.info(wenti)
                Get_Screenshot(self.driver, wenti)
                mylogger.info("用例执行失败已截图")
                raise
        else:
            try:
                # print(user_tests(self.driver).nicheng_shuru_neirong())
                mylogger.info(names5)
                self.assertEqual(user_tests(self.driver).huoqu_nicheng_tishi(), yuji, msg=wenti)
                mylogger.info('正常')
            except:
                mylogger.info(wenti)
                Get_Screenshot(self.driver, wenti)
                mylogger.info("用例执行失败已截图")
                raise

    @data(*mingzi)
    @unpack
    def txst_mingzi(self, name, zhanghao, mimai, neirong, names1, names2, names3, names4, names5, yuji, wenti):
        """%s

        :return:
        """ % name
        mylogger = Logger(logger=name).getlog()
        mylogger.info(names1)
        test_Register_Page(self.driver).login(zhanghao, mimai)
        mylogger.info(names2)
        user_tests(self.driver).user_jinglai()
        mylogger.info(names3)

        if neirong == '':
            user_tests(self.driver).mingziqingkong()
        else:
            user_tests(self.driver).xiugai_user_name(neirong)
        mylogger.info('输入内容' + neirong)

        if names4 == '点保存':
            mylogger.info(names4)
            user_tests(self.driver).baocun()

            try:

                mylogger.info(names5)
                self.assertEqual(user_tests(self.driver).tishi(), yuji, msg=wenti)
                mylogger.info('保存交互正常')
                try:
                    self.assertEqual(user_tests(self.driver).nicheng_shuru_neirong(1), neirong, msg='数据保存失败')
                    mylogger.info('保存数据正常')
                except:
                    wenti = '数据保存失败'
                    raise
            except:
                mylogger.info(wenti)
                Get_Screenshot(self.driver, wenti)
                mylogger.info("用例执行失败已截图")
                raise
        else:
            try:
                mylogger.info(names5)
                self.assertEqual(user_tests(self.driver).huoqu_nicheng_tishi(), yuji, msg=wenti)
                mylogger.info('正常')
            except:
                mylogger.info(wenti)
                Get_Screenshot(self.driver, wenti)
                mylogger.info("用例执行失败已截图")
                raise

    @data(*xingbie)
    @unpack
    def test_xingbie(self, name, zhanghao, mimai, xingbie, names1, names2, names3, names4, names5, wenti):
        """%s

        :return:
        """ % name
        mylogger = Logger(logger=name).getlog()
        mylogger.info(names1)
        test_Register_Page(self.driver).login(zhanghao, mimai)
        mylogger.info(names2)
        user_tests(self.driver).user_jinglai()
        mylogger.info(names3)
        user_tests(self.driver).xuanze_xb(xingbie)
        # print(user_tests(self.driver).nicheng_shuru_neirong(int(caoz)), xingbie)
        mylogger.info(names4)
        user_tests(self.driver).baocun()
        try:
            mylogger.info(names5)
            self.assertEqual(user_tests(self.driver).tishi(), '个人资料修改成功', msg=wenti)
            mylogger.info('保存交互正常')
            print(user_tests(self.driver).nicheng_shuru_neirong(2), xingbie)
            try:
                self.assertEqual(user_tests(self.driver).nicheng_shuru_neirong(2), xingbie, msg='数据没有回显成功')
                mylogger.info('保存数据正常')
            except:
                wenti = '数据保存失败'
                raise
        except:
            mylogger.info(wenti)
            Get_Screenshot(self.driver, wenti)
            mylogger.info("用例执行失败已截图")
            raise

    @data(*gongsiname)
    @unpack
    def txst_nichengs(self, name, zhanghao, mimai, neirong, names1, names2, names3, names4, names5, yuji, wenti):
        """%s

        :return:
        """ % name
        mylogger = Logger(logger=name).getlog()
        # '0-6'
        mylogger.info(names1)
        test_Register_Page(self.driver).login(zhanghao, mimai)
        mylogger.info(names2)
        user_tests(self.driver).user_jinglai()
        mylogger.info(names3)
        if neirong == '':
            user_tests(self.driver).shurujong_gongsi()
        else:
            user_tests(self.driver).gongsiname(neirong)
        if names4 == '点保存':
            mylogger.info(names4)
            user_tests(self.driver).baocun()
            try:
                print(user_tests(self.driver).nicheng_shuru_neirong(3), neirong)
                mylogger.info(names5)
                self.assertEqual(user_tests(self.driver).tishi(), yuji, msg=wenti)
                mylogger.info('保存交互正常')
                try:
                    self.assertEqual(user_tests(self.driver).nicheng_shuru_neirong(3), neirong, msg='不提示修改成功')
                    mylogger.info('保存数据正常')
                except:
                    wenti = '数据保存失败'
                    raise
            except:
                mylogger.info(wenti)
                Get_Screenshot(self.driver, wenti)
                mylogger.info("用例执行失败已截图")
                raise
        else:
            mylogger.info(names4)
            try:
                mylogger.info(names5)
                self.assertEqual(user_tests(self.driver).huoqu_gongsi_tishi(), yuji, msg=wenti)
                mylogger.info('正常')
            except:
                mylogger.info(wenti)
                Get_Screenshot(self.driver, wenti)
                mylogger.info("用例执行失败已截图")
                raise

    @data(*zhiyess)
    @unpack
    def txst_zhiwei(self, name, zhanghao, mimai, neirong, names1, names2, names3, names4, names5, yuji, wenti):
        """%s

        :return:
        """ % name
        print(name, neirong)
        mylogger = Logger(logger=name).getlog()
        # '0-6'
        mylogger.info(names1)
        test_Register_Page(self.driver).login(zhanghao, mimai)
        mylogger.info(names2)
        user_tests(self.driver).user_jinglai()
        mylogger.info(names3)
        user_tests(self.driver).zhiweis(neirong)
        # user_tests(self.driver).gongsiname(neirong)
        if names4 == '保存':
            mylogger.info(names4)
            user_tests(self.driver).baocun()
            try:
                print(user_tests(self.driver).nicheng_shuru_neirong(6), neirong)
                mylogger.info(names5)
                self.assertEqual(user_tests(self.driver).tishi(), yuji, msg=wenti)
                mylogger.info('保存交互正常')
                try:
                    self.assertEqual(user_tests(self.driver).nicheng_shuru_neirong(6), neirong, msg='不提示修改成功')
                    mylogger.info('保存数据正常')
                    # sleep(3)
                except:
                    wenti = '数据保存失败'
                    raise
            except:
                mylogger.info(wenti)
                Get_Screenshot(self.driver, wenti)
                mylogger.info("用例执行失败已截图")
                raise
        else:
            mylogger.info(names4)
            try:
                mylogger.info(names5)
                self.assertEqual(user_tests(self.driver).nicheng_shuru_neirong(6), neirong, msg=wenti)
                mylogger.info('正常')
                # sleep(3)
            except:
                mylogger.info(wenti)
                Get_Screenshot(self.driver, wenti)
                mylogger.info("用例执行失败已截图")
                raise

    @data(*weishuxianzhi)
    @unpack
    def txst_weishuxianzhia(self, name, zhanghao, mimai, weizhisssa, names1, names2, names3, names4, names5, yuji,
                            wenti):
        """%s

        :return:
        """ % name
        # print(name, neirong)
        mylogger = Logger(logger=name).getlog()
        mylogger.info(names1)
        test_Register_Page(self.driver).login(zhanghao, mimai)
        mylogger.info(names2)
        user_tests(self.driver).user_jinglai()
        mylogger.info(names3)
        user_tests(self.driver).weishu(int(weizhisssa), weishu_shengchenqi(int(yuji)))
        mylogger.info(names4)
        try:
            self.assertEqual(len(user_tests(self.driver).nicheng_shuru_neirong(int(weizhisssa))), int(yuji) - 1,
                             msg=wenti)
            mylogger.info(names5)
        except:
            mylogger.info(wenti)
            Get_Screenshot(self.driver, wenti)
            mylogger.info("用例执行失败已截图")
            raise

    def txst_tuichu(self):
        """测试用户信息修改页点退出

        :return:
        """
        mylogger = Logger(logger='测试用户信息修改页点退出').getlog()
        mylogger.info("登录'sj17600446278@163.com','a123456'")
        test_Register_Page(self.driver).login('sj17600446278@163.com', 'a123456')
        mylogger.info("点修改用户信息")
        user_tests(self.driver).user_jinglai()
        mylogger.info("点退出按钮")
        # print(user_tests(self.driver).nicheng_shuru_neirong(2))
        user_tests(self.driver).tuichu()
        sleep(2)
        try:
            self.assertEqual(user_tests(self.driver).tuichuyanzheng(), '智能核查', msg='用户信息修改页不能退出首页')
            mylogger.info("退出成功")
        except:
            Get_Screenshot(self.driver, '用户信息修改页不能退出首页')
            mylogger.info("用例执行失败已截图")
            raise


if __name__ == '__main__':
    unittest2.main()
