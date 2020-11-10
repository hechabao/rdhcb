# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from base.basePage import BasePage
from func.get_screenshot import Get_Screenshot
from func.log import Logger

'''
(//div[@class='register clearfix']//div)[3]
(//div[@class='content'])[2]
(//div[@class='content'])[3]
//div[text()='  联系电话']/following-sibling::p
//div[text()='  联系邮箱']/following-sibling::div
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[6]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[7]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[8]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[9]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[10]/div[1]"));
WebElement = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[11]/div[1]"));
WebElement  = driver.findElement(By.xpath("//div[@id='scroll']/div[1]/div[1]/div[2]/div[2]/div[2]/div[12]/div[1]"));
html>body>div:nth-of-type(2)
//button[@class='el-button el-button--primary']
(//button[@type='button'])[3]
(//div[@contenteditable='true'])[5]
(//button[@type='button'])[3]







['定期报告（年报等）','重组报告,基金募集报告','其他再融资报告','评级报告','审计报告','保荐书','法律意见书','固收报告','行研报告','债券发行报告（公司债、企业债、可转债、金融债、PPN等）','其他股/债申报底稿']
['跨版本对比核查','本地化部署','在线充值']
['数据一致性','财务指标','经营指标','发行指标','科目勾稽关系','指标变动异常','可比公司指标核查','固收报告','行研报告']
['发行人基本信息','子分公司基本信息','股东基本信息','股东基本信息','主要客户/供应商基本信息','专利信息','合同编号','商标信息','行业数据','采购及销售信息等']
['中介文件一致性引用','信披完备性','语句/段落描述完整性','其他低级错误类型（含错别字、符号、变动计算等）]
'''


class yijianss_tests(BasePage):
    zhenwennr = ['中介文件一致性引用', '信披完备性', '语句/段落描述完整性', '其他低级错误类型（含错别字、符号、变动计算等）']
    xingzgnxq = ['跨版本对比核查', '本地化部署', '在线充值']
    caiwsj = ['数据一致性', '财务指标', '经营指标', '发行指标', '科目勾稽关系', '指标变动异常', '可比公司指标核查', '固收报告', '行研报告']
    feicaiwfw = ['发行人基本信息', '子分公司基本信息', '股东基本信息', '股权变动连续性', '主要客户/供应商基本信息', '专利信息', '合同编号', '商标信息', '行业数据', '采购及销售信息等']
    wenjianleix_datas = ['定期报告（年报等）', '重组报告', '基金募集报告', '其他再融资报告', '评级报告', '审计报告', '保荐书', '法律意见书', '固收报告', '行研报告',
                         '债券发行报告（公司债、企业债、可转债、金融债、PPN等）', '其他股/债申报底稿']
    dianji_1_loc = (By.XPATH, ("(//p[@class='tag']//span)[2]"))
    jigoname_input = "(//div[@class='content'])[2]"
    lianxiren_input = "(//div[@class='content'])[3]"
    teshi_weizhi = (By.CSS_SELECTOR, ("(//div[@class='register clearfix']//div)[3]"))
    baocun_anniu = (By.XPATH, ("//button[@class='el-button el-button--primary']"))
    fanhui_anniu = (By.XPATH, ("(//button[@type='button'])[3]"))
    qita1_shurukuang = ("(//div[@contenteditable='true'])[5]")
    qita2_shurukuang = ("//div[@data='newNeedFour']")

    baocuo_xingxiss_loc = (By.XPATH, "//div[@class='el-message el-message--success']")
    baocuo_xingxi_loc = (By.XPATH, "//div[@class='el-message el-message--error']")
    div_zhanghao_loc = "(//div[@class='content'])[4]"
    p_zhanghao_loc = "//p[@class='content']"
    yanzhengshoye = (By.CSS_SELECTOR, ("header#head-top>header>span"))

    # 提示
    def tishi(self):
        while True:
            try:
                # time.sleep(2)
                nananan = self.driver.find_element(*self.baocuo_xingxi_loc).text.replace(" ", "")
                return nananan
            except:
                print('没有')

    def tishi2(self):
        while True:
            try:
                # time.sleep(2)
                nananan = self.driver.find_element(*self.baocuo_xingxiss_loc).text.replace(" ", "")
                return nananan
            except:
                print('没有')

    # 拼接位置
    def wanjianleix_pj(self, list, name):
        print(list, name)
        if name in list:
            print(list.index(name))
            neirn = list.index(name)
            return neirn
        else:
            print('没有这个文件类型')

    def wanjianleix_pj_weizhi(self, xuqiu, mokuai1, mokuai2, weizhi):
        n = "//div[@id='scroll']/div[1]/div[1]/div[%s]/div[%s]/div[%s]/div[%s]/div[1]" % (
        xuqiu, mokuai1, mokuai2, weizhi)
        return n

    # 进入
    def user_jinglai(self):
        sleep(1)
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.dianji_1_loc).click()
        sleep(0.5)

    # 邮箱，电话，地址，输入和获取操作
    def panduanweizhi(self, neirong, mame, caozuo, zhanghao):

        if mame == '联系邮箱':
            if caozuo == '输入':
                self.youxi_dianhua_dizhi(neirong, 4, 60)
            elif caozuo == "获取":
                if zhanghao == '邮箱':
                    return self.huoquqneirong(self.p_zhanghao_loc)
                elif zhanghao == '手机':
                    return self.huoquqneirong(self.div_zhanghao_loc)


        elif mame == '联系电话':
            if caozuo == '输入':
                self.youxi_dianhua_dizhi(neirong, 4, 12)
            elif caozuo == "获取":
                if zhanghao == '邮箱':
                    return self.huoquqneirong(self.div_zhanghao_loc)
                elif zhanghao == '手机':
                    return self.huoquqneirong(self.p_zhanghao_loc)


        elif mame == '地址':
            if caozuo == '输入':
                self.youxi_dianhua_dizhi(neirong, 5, 60)
            elif caozuo == "获取":
                return self.huoquqneirong(self.pin_xpas_dingwei_imput(5))


        elif mame == '机构名称':
            if caozuo == '输入':
                self.jigoname_input_loc(neirong)
            elif caozuo == "获取":
                return self.huoquqneirong(self.jigoname_input)


        elif mame == '联系人':
            if caozuo == '输入':
                self.lianxiren_input_loc(neirong)
            elif caozuo == "获取":
                return self.huoquqneirong(self.lianxiren_input)


        elif mame == '其他1':
            if caozuo == '输入':
                self.qita1_caozuo(neirong)
            elif caozuo == "获取":
                return self.huoquqneirong(self.qita1_shurukuang)


        elif mame == '其他2':
            if caozuo == '输入':
                self.qita2_caozuo(neirong)
            elif caozuo == "获取":
                return self.huoquqneirong(self.qita2_shurukuang)


        elif mame == '文件类型':
            queshi = self.wanjianleix_pj(self.wenjianleix_datas, neirong) + 1
            self.wenjianleix_goxuan('2', '2', '2', str(queshi))
        elif mame == '财务数据范围':
            self.wenjianleix_goxuan('2', '3', '2', str(self.wanjianleix_pj(self.caiwsj, neirong) + 1))
        elif mame == '非财务数据范围':
            self.wenjianleix_goxuan('2', '4', '2', str(self.wanjianleix_pj(self.feicaiwfw, neirong) + 1))
        elif mame == '正文内容范围':

            self.wenjianleix_goxuan('2', '5', '2', str(self.wanjianleix_pj(self.zhenwennr, neirong) + 1))
        elif mame == '新增功能需求':
            self.wenjianleix_goxuan('3', str(self.wanjianleix_pj(self.xingzgnxq, neirong) + 2), '1', '1')

    # 其他1
    def qita1_caozuo(self, name):
        self.qaingchu((By.XPATH, ("%s" % self.qita1_shurukuang)), 300)
        self.driver.find_element(By.XPATH, ("%s" % self.qita1_shurukuang)).send_keys(name)

    # 其他2
    def qita2_caozuo(self, name):
        self.qaingchu((By.XPATH, ("%s" % self.qita2_shurukuang)), 300)
        self.driver.find_element(By.XPATH, ("%s" % self.qita2_shurukuang)).send_keys(name)

    # 清除
    def qaingchu(self, weizhi, jisi):
        for i in range(jisi + 1):
            # print(weizhi)
            self.driver.find_element(weizhi[0], weizhi[1]).send_keys(Keys.BACK_SPACE)
            # print('111')

    # 获取操作
    def huoquqneirong(self, weizhi):
        n = self.driver.find_element(By.XPATH, ("%s" % weizhi)).text
        return n

    # 机构名称
    def jigoname_input_loc(self, neirong):
        self.qaingchu((By.XPATH, ("%s" % self.jigoname_input)), 50)
        self.driver.find_element(By.XPATH, ("%s" % self.jigoname_input)).send_keys(neirong)

    # 联系人
    def lianxiren_input_loc(self, neirong):
        self.qaingchu((By.XPATH, ("%s" % self.lianxiren_input)), 16)
        self.driver.find_element(By.XPATH, ("%s" % self.lianxiren_input)).send_keys(neirong)

    def pin_xpas_dingwei(self, s):
        n = "//div[text()='  %s']/following-sibling::div" % s
        print(n.replace("\\n", "").replace("\\", ""))
        return n.replace("\\n", "").replace("\\", "")

    def pin_xpas_dingwei2(self, s):
        n = "//div[text()='  %s']/following-sibling::p" % s
        print(n.replace("\\n", "").replace("\\", ""))
        return n.replace("\\n", "").replace("\\", "")

    def pin_xpas_dingwei_imput(self, s):
        dizhi_input = "(//div[@class='content'])[%s]" % s
        return dizhi_input

    # 勾选
    def wenjianleix_goxuan(self, xuqiu, mokuai1, mokuai2, weizhi):
        self.driver.find_element(By.XPATH, (self.wanjianleix_pj_weizhi(xuqiu, mokuai1, mokuai2, weizhi))).click()

    def dian_querding(self):
        self.driver.find_element(*self.baocun_anniu).click()

    def dian_fanhui(self):
        self.driver.find_element(*self.fanhui_anniu).click()

    def tuichuyanzheng(self):
        try:
            # time.sleep(2)
            nananan = self.driver.find_element(*self.yanzhengshoye).text.replace(" ", "")
            return nananan
        except:
            print('没有')

    # 邮箱，电话，地址，输入操作
    def youxi_dianhua_dizhi(self, neirong, weizhi, weishu):
        self.qaingchu((By.XPATH, ("%s" % self.pin_xpas_dingwei_imput(weizhi))), weishu)
        self.driver.find_element(By.XPATH, ("%s" % self.pin_xpas_dingwei_imput(weizhi))).send_keys(neirong)
