from selenium.webdriver.common.by import By
import time
import re
import os
import selenium
from base.basePage import BasePage


# 登录
class test_Register_Page(BasePage):
    # 元素定位div#app>div>div:nth-of-type(3)>div>span
    baocuo_xingxi_loc = (By.CLASS_NAME, "el-message__content")  # 提示框获取
    username_input_loc = (By.CLASS_NAME, 'el-input__inner')  # 账号输入框
    password_input_loc = (By.XPATH, "//input[@placeholder='请输入密码']")  # 密码输入框
    baiwen_input_loc = (By.CLASS_NAME, 'el-progress__text')
    url = '/projectManager/index#/'  # 地址
    baocuo = (By.XPATH, "//div[contains(@class,'el-inp el-input')]/following-sibling::p[1]")  # 输入框提示
    yxz = (By.LINK_TEXT, "云协作")  # 云协作跳转按钮
    erlang = (By.LINK_TEXT, "二郎神")  # 二郎神跳转按钮
    yonghuzuce = (By.XPATH, "//div[text()='忘记密码?']")  # 忘记密码按钮
    wangjimimas = (By.XPATH, "//div[text()='用户注册']")  # 用户注册按钮
    shenji_baduan_zhidao_anniu = (By.XPATH, "//span[text()[normalize-space()='我知道了']]")  # 活动提示框等待5秒后的我知道了按钮
    login_btu_loc = (By.CSS_SELECTOR, "div#app>div>div:nth-of-type(3)>div>span")

    # 打开页面
    def open(self):
        self.url = self.base_url + self.url
        self.driver.get(self.url)

    # 账号输入框
    def input_username(self, username):
        time.sleep(1)
        self.driver.find_element(*self.username_input_loc).send_keys(username)
        # self.driver.find_element()

    # 密码输入框
    def input_password(self, password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    # 点击登录
    def click_login_bth(self):
        time.sleep(1)
        self.driver.find_element(*self.login_btu_loc).click()
        time.sleep(1)

    # 提示框获取
    def tishi(self):
        while True:
            try:
                # time.sleep(2)
                nananan = self.driver.find_element(*self.baocuo_xingxi_loc).text.replace(" ", "")
                return nananan
            except:
                print('没有')

    # 输入框提示
    def click_shangcuan_bth(self):
        time.sleep(1)
        n = self.driver.find_element(*self.baocuo).text
        return n

    # 升级通告时点击知道按钮
    def shengji_panduan(self):
        try:
            time.sleep(5)
            self.driver.find_element(*self.shenji_baduan_zhidao_anniu).click()
            time.sleep(1)
        except:
            print('失败')

    # 登录操作集
    def login(self, username, password):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_login_bth()
        # self.shengji_panduan()#升级通告时点击知道按钮
        # return self.driver

    # 点击云协作按钮获取跳转链接
    def yunxiezuo(self):
        self.driver.find_element(*self.yxz).click()
        return self.driver.current_url

    # 点击二郎神按钮获取跳转链接
    def erlangshen(self):
        self.driver.find_element(*self.erlang).click()
        return self.driver.current_url

    # 点击用户注册按钮获取跳转链接
    def wangjimima(self):
        self.driver.find_element(*self.yonghuzuce).click()
        return self.driver.current_url

    # 点击忘记密码按钮获取跳转链接
    def yonghuzhuce(self):
        time.sleep(1)
        self.driver.find_element(*self.wangjimimas).click()
        return self.driver.current_url
