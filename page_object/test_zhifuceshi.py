# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from base.basePage import BasePage

'''
//div[@class='ft-center qrcode-header-money']
(//div[@class='register clearfix']//div)[1]
(//section[@class='head-tab-item'])[3]
document.getElementsByClassName('span45')[0].value
document.getElementsByClassName('span20')[0].value
(//span[@class='desr'])[1]
document.getElementsByClassName('span20')[1].value
(//span[@class='desr'])[2]
(//div[@class='content']//img)[4]
no1
no2
//button[@class='combtn submit']
//button[@class='combtn reset']
您还未输入充值积分
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[1]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[2]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[3]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[4]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span25'])[1]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span25'])[2]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[1]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[2]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span25'])[1]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span25'])[2]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[3]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[4]"));
WebElement  = driver.findElement(By.xpath("(//input[@class='span45'])[5]"));
WebElement  = driver.findElement(By.className("span15"));
WebElement  = driver.findElement(By.className("span20"));
WebElement  = driver.findElement(By.xpath("//input[@placeholder='请输入手机号']"));
placeholder
document.getElementsByClassName('span45')[0].value
'''


class zhifu_tests(BasePage):
    jinru_1_loc = (By.XPATH, "(//div[@class='register clearfix']//div)[1]")
    jinru_2_loc = (By.XPATH, "(//section[@class='head-tab-item'])[3]")
    zhanhao_kuang = "return document.getElementsByClassName('span45')[0].value"
    jifen_kuang_huoqu = "return document.getElementsByClassName('span20')[0].value"
    jifen_kuang = (By.XPATH, "(//input[@class='span20'])[1]")
    jifen_tishi = (By.XPATH, "(//span[@class='desr'])[1]")
    jiner_kuang_huoqu = "return document.getElementsByClassName('span20')[1].value"
    jiner_kuang = (By.XPATH, "(//input[@class='span20'])[2]")
    jiner_tishi = (By.XPATH, "(//span[@class='desr'])[2]")
    zhifu_fangshi_kuang = (By.XPATH, "(//div[@class='content']//img)[4]")
    ptfp_goxuan_kuang = (By.ID, 'no1')
    zzfp_goxuan_kuang = (By.ID, 'no2')
    queding_kuang = (By.XPATH, "//button[@class='combtn submit']")
    fanhui_annniu = (By.XPATH, "//button[@class='combtn reset']")
    baocuo_xingxi_loc = (By.CLASS_NAME, "el-message__content")
    zhanhao_kuang0 = "return document.getElementsByClassName('span45')[0].value"
    zhanhao_kuang1 = "return document.getElementsByClassName('span45')[1].value"
    zhanhao_kuang2 = "return document.getElementsByClassName('span45')[2].value"
    zhanhao_kuang3 = "return document.getElementsByClassName('span45')[3].value"
    zhanhao_kuang4 = "return document.getElementsByClassName('span45')[4].value"
    zhanhao_kuang5 = "return document.getElementsByClassName('span45')[5].value"
    zhanhao_kuangs0 = "return document.getElementsByClassName('span25')[0].value"
    zhanhao_kuangs1 = "return document.getElementsByClassName('span25')[1].value"
    zhanhao_kuangs2 = "return document.getElementsByClassName('span25')[2].value"

    zhanhao_kuangs3 = "return document.getElementsByClassName('span25')[3].value"
    zhanhao_kuangsss0 = "return document.getElementsByClassName('span20')[0].value"
    zhanhao_kuangsss1 = "return document.getElementsByClassName('span15')[0].value"

    # 进入积分充值
    def jinruf(self):
        sleep(0.5)
        self.driver.find_element(*self.jinru_1_loc).click()
        sleep(0.5)
        self.driver.find_element(*self.jinru_2_loc).click()

    # 清除
    def qaingchu(self, weizhi, jisi):
        for i in range(jisi + 1):
            # print(weizhi)
            self.driver.find_element(weizhi[0], weizhi[1]).send_keys(Keys.BACK_SPACE)
            # print('111')

    # 返回账号框内容
    def zhanghao_huoquf(self):
        a = self.driver.execute_script(self.zhanhao_kuang)
        print(a)
        if a:
            return '有'
        else:
            return '没'

    # 积分框输入
    def jifen_chongzhif(self, neirong):
        self.qaingchu(self.jifen_kuang, 16)
        self.driver.find_element(*self.jifen_kuang).send_keys(neirong)

    # 积分输入框内容获取返回
    def jifen_huoquf(self):
        a = self.driver.execute_script(*self.jifen_kuang_huoqu)
        return a

    # 积分提示
    def jifen_tishif(self):
        sleep(1)
        self.driver.find_element(*self.jifen_tishi).text

    # 金额框输入
    def jiner_chongzhif(self, neirong):
        self.qaingchu(self.jiner_kuang, 16)
        self.driver.find_element(*self.jiner_kuang).send_keys(neirong)

    # 金额输入框内容获取返回
    def jiner_huoquf(self):
        a = self.driver.execute_script(*self.jiner_kuang_huoqu)
        return a

    # 金额提示
    def jiner_tishif(self):
        sleep(1)
        self.driver.find_element(*self.jiner_tishi).text

    # 点击支付方式
    def dianji_zhifu_fangshi(self):
        sleep(0.5)
        self.driver.find_element(*self.zhifu_fangshi_kuang).click()

    # 勾选普通发票
    def go_xuan_ptfapiao(self):
        self.driver.find_element(*self.ptfp_goxuan_kuang).click()
        # print('ssss')

    # 勾选增值税发票
    def go_xuan_zzfapiao(self):
        self.driver.find_element(*self.zzfp_goxuan_kuang).click()

    # 点确定
    def dian_queding(self):
        self.driver.find_element(*self.queding_kuang).click()

    # 获取确定键内容
    def huoquq_queding(self):
        n = self.driver.find_element(*self.queding_kuang).text
        return n

    # 点返回
    def dian_fanhui(self):
        self.driver.find_element(*self.fanhui_annniu).click()

    # 二级位置
    def caozuo_weizhisss(self, weihzi):
        if weihzi == '公司名':
            a = self.driver.execute_script(self.zhanhao_kuang0)
            return a
        elif weihzi == '纳税人识':
            a = self.driver.execute_script(self.zhanhao_kuang1)
            return a
        elif weihzi == '邮寄地址':
            a = self.driver.execute_script(self.zhanhao_kuang4)
            return a
        elif weihzi == '邮政编码':
            a = self.driver.execute_script(self.zhanhao_kuangsss1)
            return a
        elif weihzi == '联系人':
            a = self.driver.execute_script(self.zhanhao_kuangsss0)
            return a
        elif weihzi == '手机号':
            a = self.driver.execute_script(self.zhanhao_kuang5)
            return a
        elif weihzi == '手机':
            a = self.driver.execute_script(self.zhanhao_kuangs0)
            return a
        elif weihzi == '公司地址':
            a = self.driver.execute_script(self.zhanhao_kuangs1)
            return a
        elif weihzi == '开户银行':
            a = self.driver.execute_script(self.zhanhao_kuang2)
            return a
        elif weihzi == '账户':
            a = self.driver.execute_script(self.zhanhao_kuang3)
            return a

    # 二级位置
    def caozuo_weizhi(self, weihzi):
        if weihzi == '公司名':
            a = self.driver.execute_script(self.zhanhao_kuang0)
            return a
        elif weihzi == '纳税人识':
            a = self.driver.execute_script(self.zhanhao_kuang1)
            return a
        elif weihzi == '邮寄地址':
            a = self.driver.execute_script(self.zhanhao_kuang2)
            return a
        elif weihzi == '邮政编码':
            a = self.driver.execute_script(self.zhanhao_kuang3)
            return a
        elif weihzi == '联系人':
            a = self.driver.execute_script(self.zhanhao_kuangs0)
            return a
        elif weihzi == '手机号':
            a = self.driver.execute_script(self.zhanhao_kuangs1)
            return a

    def fanhui_pn(self, neirong):
        namesss = "//input[@placeholder='%s']" % neirong
        self.driver.find_URL_elements()
        # print(namesss)
        return namesss

    # 框输入
    def wanneng_chongzhif(self, neirong, name):
        sleep(1)
        # print('zjap')
        self.driver.find_element(*(By.XPATH, (self.fanhui_pn(neirong)))).send_keys(name)

    def kuang_huoqu(self, neirong):
        a = self.driver.find_element(*(By.XPATH, (self.fanhui_pn(neirong)))).text
        return a

    # 一级位置
    def dian_weizhi(self, weihzi, names, nsss):
        if weihzi == '积分充值':
            self.wanneng_chongzhif(neirong=names, name=nsss)
        elif weihzi == '普通发票':
            self.go_xuan_ptfapiao()
            sleep(1)
            self.dian_queding()
            sleep(1)
            self.wanneng_chongzhif(neirong=names, name=nsss)
        elif weihzi == '增值税发票':
            self.go_xuan_zzfapiao()
            self.dian_queding()
            self.wanneng_chongzhif(neirong=names, name=nsss)

    # 获取
    def huoqu_dian_weizhi(self, weihzi, name):
        print(weihzi, name)
        if weihzi == '积分充值':
            return self.kuang_huoqu(neirong=name)
        elif weihzi == '普通发票':
            return self.caozuo_weizhi(name)

        elif weihzi == '增值税发票':
            return self.caozuo_weizhisss(name)

    # 提示
    def tishi(self):
        sleep(1)
        while True:
            try:
                # time.sleep(2)
                nananan = self.driver.find_element(*self.baocuo_xingxi_loc).text.replace(" ", "")
                return nananan
            except:
                print('没有')
