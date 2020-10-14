# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from base.basePage import BasePage
from func.get_screenshot import Get_Screenshot
from func.log import Logger
'''
(//div[@class='register clearfix']//div)[2]
//span[text()='修改个人资料']
(//input[@class='el-input__inner'])[1]
(//input[@class='el-input__inner'])[2]
(//input[@class='el-input__inner'])[3]
html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[1]
html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[2]
(//input[@class='el-input__inner'])[4]
(//input[@class='el-input__inner'])[5]
(//input[@value-key='project_name'])[5]
(//input[@placeholder='请选择'])[2]
header#head-top>header>span
tab-password
(//input[@type='password'])[1]
'''
class user_tests(BasePage):
    dianji_1_loc = (By.XPATH,("(//div[@class='register clearfix']//div)[2]"))
    dianji_2_loc = (By.XPATH,("//span[text()='修改个人资料']"))
    shur_nichen_loc = (By.XPATH, ("(//input[@class='el-input__inner'])[1]"))
    shuru_name_loc = (By.XPATH, ("(//input[@class='el-input__inner'])[2]"))
    dianji_xb_loc = (By.XPATH, ("(//input[@class='el-input__inner'])[3]"))
    xuanze_nan_loc = (By.XPATH, ("html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[1]"))
    xuanze_nv_loc = (By.XPATH, ("html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[2]"))
    shuru_gongsi_name_loc = (By.XPATH, ("(//input[@class='el-input__inner'])[4]"))
    shuru_bunen_name_loc = (By.XPATH, ("(//input[@class='el-input__inner'])[5]"))
    shuru_zhiye_name_loc = (By.XPATH, ("(//input[@value-key='project_name'])[5]"))
    xuanze_zhiye_loc = (By.XPATH, ("(//input[@placeholder='请选择'])[2]"))
    dianji_baocun_loc = (By.XPATH, ("(//button[@class='el-button el-button--primary'])[1]"))
    dianji_tuichu_loc = (By.XPATH, ("(//button[@class='el-button el-button--primary'])[2]"))
    baocuo_xingxi_loc = (By.CLASS_NAME, "el-message__content")
    tishi_kuang_loc = (By.XPATH,("//div[@role='alert']"))
    nichengtishi = (By.XPATH,("(//div[@class='inline-input el-input']/following-sibling::span)[1]"))
    gongsitishi = (By.XPATH,("//div[@class='inline-input el-input']/following-sibling::span[1]"))
    password_input1_loc = (By.XPATH, ("(//input[@type='password'])[1]"))
    yanzhengshoye = (By.CSS_SELECTOR,("header#head-top>header>span"))
    password_change_ye = (By.ID,("tab-password"))
    password_input2_loc = (By.XPATH, ("(//input[@type='password'])[2]"))
    password_input3_loc = (By.XPATH, ("(//input[@type='password'])[3]"))
    password_input1_loc_tishi1 = (By.XPATH, ("(//div[contains(@class,'el-alert el-alert--error')])[1]"))
    password_input1_loc_tishi2 = (By.XPATH, ("(//div[contains(@class,'el-alert el-alert--error')])[2]"))
    password_input1_loc_tishi3 = (By.XPATH, ("(//div[contains(@class,'el-alert el-alert--error')])[3]"))
    password_click_determine = (By.XPATH, ("(//div[contains(@class,'el-alert el-alert--error')])[3]"))



    # 跳转密码修改页面
    def Change_Password(self):
        sleep(1)
        self.driver.find_element(*self.dianji_1_loc).click()
        sleep(1)
        self.driver.find_element(*self.password_change_ye).click()
    # 原始密码输入
    def password_input_original(self, password):
        sleep(1)
        self.driver.find_element(*self.password_input1_loc).send_keys(password)
    # 新密码输入
    def password_input_new1(self, password):
        sleep(1)
        self.driver.find_element(*self.password_input2_loc).send_keys(password)
    # 验证密码
    def password_input_new2(self, password):
        sleep(1)
        self.driver.find_element(*self.password_input3_loc).send_keys(password)
    # 进入
    def  user_jinglai(self):
        sleep(1)
        self.driver.find_element(*self.dianji_1_loc).click()
        sleep(1)
        self.driver.find_element(*self.dianji_2_loc).click()
        # self.driver.find_element(*self.dianji_2_loc).

    #返回昵称提示
    def huoqu_nicheng_tishi(self):
        sleep(1)
        a = self.driver.find_element(*self.nichengtishi).text.replace(" ", "")
        print(a)
        return a
        # sleep(101)
    def shurujong(self):
        for i in range(0,10):
            self.driver.find_element(*self.shur_nichen_loc).send_keys(Keys.BACK_SPACE)
    #     输入昵称
    def xiugai_name(self,name):
        self.driver.find_element(*self.shur_nichen_loc).clear()
        self.driver.find_element(*self.shur_nichen_loc).send_keys(name)

    # 获取其输入框内容
    def nicheng_shuru_neirong(self,weizhi):
        sleep(1)
        self.driver.find_element(*self.dianji_2_loc).click()
        sleep(0.5)
        a = self.driver.execute_script(
            "return document.getElementsByClassName('el-input__inner')[%s].value"%weizhi)
        return a
    #     输入姓名
    def xiugai_user_name(self,user_name):
        self.driver.find_element(*self.shuru_name_loc).clear()
        self.driver.find_element(*self.shuru_name_loc).send_keys(user_name)
    def mingziqingkong(self):
        for i in range(0,10):
            self.driver.find_element(*self.shuru_name_loc).send_keys(Keys.BACK_SPACE)
    #     选择性别
    def xuanze_xb(self,xb):

        self.driver.find_element(*self.dianji_xb_loc).click()
        if xb == '男':
            self.driver.find_element(*self.xuanze_nan_loc).click()

        elif xb == '女':
            self.driver.find_element(*self.xuanze_nv_loc).click()

    #     公司名字
    def gongsiname(self,gongsiname):
        self.driver.find_element(*self.shuru_gongsi_name_loc).clear()
        self.driver.find_element(*self.shuru_gongsi_name_loc).send_keys(gongsiname)
    def huoqu_gongsi_tishi(self):
        sleep(1)
        a = self.driver.find_element(*self.gongsitishi).text.replace(" ", "")
        print(a)
        return a
    def shurujong_gongsi(self):
        for i in range(0,20):
            self.driver.find_element(*self.shuru_gongsi_name_loc).send_keys(Keys.BACK_SPACE)
    #     所属部门
    def suoshubumenname(self,suoshubumenname):
        self.driver.find_element(*self.shuru_bunen_name_loc).clear()
        self.driver.find_element(*self.shuru_bunen_name_loc).send_keys(suoshubumenname)
    #     职位姓名
    def zhiweiname(self,zhiweiname):
        self.driver.find_element(*self.shuru_zhiye_name_loc).clear()
        self.driver.find_element(*self.shuru_zhiye_name_loc).send_keys(zhiweiname)
    #     职位
    def zhiweis(self,zhiye):
        sleep(1)
        self.driver.find_element(*self.xuanze_zhiye_loc).click()
        sleep(1)
        dianji_zhiye_loc = (By.XPATH, ("//span[text() = '%s']/.."%zhiye))
        self.driver.find_element(*dianji_zhiye_loc).click()
    #     保存按钮
    def baocun(self):

        self.driver.find_element(*self.dianji_baocun_loc).click()
    #     推出按钮
    def tuichu(self):

        self.driver.find_element(*self.dianji_tuichu_loc).click()
    #     提示获取
    def tishi(self):
        sleep(1)
        while True:
            try:
                # time.sleep(2)
                nananan = self.driver.find_element(*self.baocuo_xingxi_loc).text.replace(" ", "")
                return nananan
            except:
                print('没有')

    def tuichuyanzheng(self):
        try:
            # time.sleep(2)
            nananan = self.driver.find_element(*self.yanzhengshoye).text.replace(" ", "")
            return nananan
        except:
            print('没有')
    def weishu(self,weizhi,neriong):

        if weizhi == 0:
            self.xiugai_name(neriong)
        elif weizhi == 1:
            self.xiugai_user_name(neriong)
        elif weizhi == 3:
            self.gongsiname(neriong)
        elif weizhi == 4:
            self.suoshubumenname(neriong)
        elif weizhi == 5:
            self.zhiweiname(neriong)




































