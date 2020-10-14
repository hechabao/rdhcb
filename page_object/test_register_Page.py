from selenium.webdriver.common.by import By
import time
import re
import os
import selenium
from base.basePage import BasePage
'''
//i[@class='close el-icon-circle-close']


'''
#登录
class test_Register_Page(BasePage):
    baocuo_xingxi_loc = (By.CLASS_NAME, "el-message__content")
    username_input_loc = (By.CLASS_NAME, 'el-input__inner')
    password_input_loc = (By.XPATH, "//input[@placeholder='请输入密码']")
    baiwen_input_loc = (By.CLASS_NAME, 'el-progress__text')
    login_btu_loc = (By.XPATH,
                     "/html/body/div[@id='app']/div[@class='login']/div[@class='clearfix login-box']/div[@class='login-cont']/span")
    shangchuan_loc = (By.XPATH, (
        "/html/body/div[@id='app']/div[@id='home']/div[@class='content']/div[@class='main source']/div[@class='main-create flex-row']/div[@class='main-create-upload']/div[@class='content']/div[@class='center']/div[@class='upload flex-row3']/div[@class='elUpload flex1']/div[@class='upload-demo flex-col']/div[@class='el-upload el-upload--text']/div[@class='el-upload-dragger']"))
    url = '/projectManager/index#/'
    guanggao_guanbi = (By.XPATH,("//i[@class='close el-icon-circle-close']"))
    baocuo = (By.XPATH, "//div[contains(@class,'el-inp el-input')]/following-sibling::p[1]")
    yxz= (By.LINK_TEXT,"云协作")
    erlang = (By.LINK_TEXT, "二郎神")
    yonghuzuce=(By.XPATH,"//div[text()='忘记密码?']")
    wangjimimas=(By.XPATH,"//div[text()='用户注册']")
    shenji_baduan_zhidao_anniu = (By.XPATH,"//span[text()[normalize-space()='我知道了']]")
    def open(self):
        self.url = self.base_url + self.url
        self.driver.get(self.url)


    def input_username(self,username):
        time.sleep(1)
        self.driver.find_element(*self.username_input_loc).send_keys(username)
        # self.driver.find_element()

    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_bth(self):
        time.sleep(1)
        self.driver.find_element(*self.login_btu_loc).click()
        time.sleep(1)
        # time.sleep(3)
        # self.driver.find_element(*self.guanggao_guanbi).click()
        # time.sleep(1)
        return 1
    def tishi(self):
        while True:
            try:
                # time.sleep(2)
                nananan = self.driver.find_element(*self.baocuo_xingxi_loc).text.replace(" ", "")
                return nananan
            except:
                print('没有')

    def click_shangcuan_bth(self):
        time.sleep(1)
        n = self.driver.find_element(*self.baocuo).text
        return n
        # print(n)
        # print('......................')
    def shengji_panduan(self):
        try:
            time.sleep(5)
            self.driver.find_element(*self.shenji_baduan_zhidao_anniu).click()
            time.sleep(1)
        except:
            print('失败')
    def login(self,username,password):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_login_bth()
        # self.shengji_panduan()#升级通告时点击知道按钮
        # return self.driver
    def yunxiezuo(self):
        self.driver.find_element(*self.yxz).click()
        return self.driver.current_url
    def erlangshen(self):
        self.driver.find_element(*self.erlang).click()
        return self.driver.current_url
    def wangjimima(self):
        self.driver.find_element(*self.yonghuzuce).click()
        return self.driver.current_url
    def yonghuzhuce(self):
        time.sleep(1)
        self.driver.find_element(*self.wangjimimas).click()
        return self.driver.current_url