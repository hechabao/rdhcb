# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By
import time
from func.verification_result_method import baogao
from func.log import Logger
# import re
import os
# import selenium
from base.basePage import BasePage
from func.get_screenshot import Get_Screenshot
'''
D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\傲基科技：招股说明书 0828-0341.docx
D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\2【傲基科技】法律意见书 20190827 clean.docx
D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\深圳分所：大华审字(2019)009872号傲基科技股份有限公司5+1份-数字.xlsx
<span class="xh-highlight">开始核查</span>
el-button table-middle-button el-button--danger el-button--mini is-plain
tagName("select")
//div[@class='fileList']/
//div[@class='fileList']
el-scrollbar__view el-select-dropdown__list
class[main-create-project]/div/img切换按钮
报错内容el-col el-col-24
详情el-dialog__body
积分tag jifen
placeholder="请选择"
上海证券交易所
class="main-create-project flex1"
//a[text()="文本"]/following-sibling::a[1]

'''
# mylogger = Logger(logger='TestMyLog').getlog()
# mylogger = Logger(logger='上传').getlog()
# mylogger.info("打开浏览器")
class wenjian(BasePage):
    # self.driver.find_element(*self.qiehuan_anniu_loc).click()    智能上传和普通上传切换代码
    shangchuan_loc = (By.XPATH, (
        "/html/body/div[@id='app']/div[@id='home']/div[@class='content']/div[@class='main source']/div[@class='main-create flex-row']/div[@class='main-create-upload']/div[@class='content']/div[@class='center']/div[@class='upload flex-row3']/div[@class='elUpload flex1']/div[@class='upload-demo flex-col']/div[@class='el-upload el-upload--text']/div[@class='el-upload-dragger']"))
    shangchuan_jindu_loc = (By.CLASS_NAME, 'el-progress__text')
    hecha_click_loc = (By.XPATH, "//span[text()='开始核查']")
    hecha_zhuangtai_loc = (By.XPATH, ("//div[@class='cell']/button"))
    hecha_shuliang_loc = (By.XPATH,("//div[@class='fileList']"))
    baocuo_xingxi_loc = (By.CLASS_NAME, "el-message__content")
    jiexixiangqing_xingxi_loc = (By.CLASS_NAME, ("el-dialog__body"))
    # jifen_huoqu_loc = (By.XPATH, ('//header[@class="el-header clearfix"]/div[@class="register clearfix"]/div/p/span'))placeholder="请输入核查人员"
    jifen_huoqu_loc = (By.XPATH, ('//p[@class="tag jifen"]/span'))
    shuru_xiangmuname_loc = (By.XPATH, ('//input[@placeholder="请输入项目名称"]'))
    xuanzhe_gslx_name_loc = (By.XPATH, ("(//input[@class='el-input__inner'])[2]"))
    qiehuan_anniu_loc = (By.XPATH, ("//div[contains(@class,'meun-switch animated')]//img[1]"))
    gslys_all_loc = (By.XPATH, ('//span[text()="深圳证券交易所"]'))
    hechayuan_shuru_loc = (By.XPATH,('//input[@placeholder="请输入核查人员"]'))
    jioayisuo_all_loc = (By.XPATH, ("//label[text()='交易所：']/following-sibling::div[1]/div/div/input"))
    rongzileixing_all_loc = (By.XPATH, ("//label[text()='融资类型：']/following-sibling::div[1]/div/div/input"))
    xiayibu_loc = (By.XPATH, ("//span[text()='下一步']"))
    wenjianhsnagchuan_loc = (By.XPATH, ("//div[@class='upload']/div[@class='upload-name']"))
    gongzhuanshu_loc = (By.XPATH, ("(//p[text()='点击上传文件'])[1]"))
    pt_1_shuliang_loc = (By.XPATH, ("(//div[@class='box_file_list']//div)[1]"))
    shangchuan_2_loc = (By.XPATH, ("(//span[text()='点击上传'])[1]"))
    # shuoqujingdu = (By.CLASS_NAME, ("el-progress__text"))
    putonghecha_kaishi = (By.XPATH, ("//button[contains(@class,'el-button zIndex199')]"))
    shuoqujingdu = (By.XPATH, ("(//div[@class='progress-box'])[1]"))
    guanbi_loc = (By.XPATH, ("//span[text()='关 闭']"))
    def zhineng(self,name_url,name_shizi):
        # time.sleep(2)el-progress__text(//div[@class='progress-box'])[1]//span[text()='关 闭']
        # self.jiexishibai()doc_file_list(//span[text()='点击上传'])[1]
        # name_url = ["D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\傲基科技：招股说明书 0828-0341.docx",
        #             "D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\2【傲基科技】法律意见书 20190827 clean.docx",
        #             "D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\深圳分所：大华审字(2019)009872号傲基科技股份有限公司5+1份-数字.xlsx"]
        # el-message__content表单必选项不得漏填!
        # time.sleep(2)
        # self.driver.find_element(*self.shangchuan_loc).click()
        # while True:
        #     try:
        #         # time.sleep(2)
        #         nananan = self.driver.find_element(*self.baocuo_xingxi_loc).text.replace(" ", "")
        #         print(nananan)
        #         if nananan == "表单必选项不得漏填!":
        #             Get_Screenshot(self.driver, '登录异常用例')
        #             break
        #     except:
        #         print('没有')
        mylogger = Logger(logger='智能上传').getlog()
        time.sleep(1)
        # self.zhinengchuanshuju('臧一凡','银行','admin')************************
        # self.shurruxingxi('臧一凡','银行','深圳证券交易所','新三板挂牌','admin')*******************************
        # self.driver.find_element(*self.qiehuan_anniu_loc).click()
        # time.sleep(2)
        # self.driver.find_element(*self.qiehuan_anniu_loc).click()
        mylogger.info("判断如果已存在文件则跳过信息填写")
        n = 1
        try:
            resultsss = len(self.driver.find_element(*self.hecha_shuliang_loc).text.split(' 上传成功\n'))
        except:
            self.zhinengchuanshuju(name_shizi[0], name_shizi[1], name_shizi[2])
        time.sleep(1)

        for i in name_url:
            print(i)

            try:
                resultsss = len(self.driver.find_element(*self.hecha_shuliang_loc).text.split(' 上传成功\n'))
            except:
                resultsss = 0
            time.sleep(0.5)
            mylogger.info("点击上传")
            self.driver.find_element(*self.shangchuan_loc).click()
            print(resultsss)
            time.sleep(0.5)
            mylogger.info("上传文件%s" % i)
            os.system(r'D:\2.1\shangchuan.exe %s' % i)
            mylogger.info("判断上传进度")

            while True:
                try:
                    result = self.driver.find_element(*self.shangchuan_jindu_loc).text
                    # print(result)
                    if result == '100%':
                        mylogger.info("100%成功")
                        # print('完成')
                        break
                except:
                    print('-----------------')
                    resultss = len(self.driver.find_element(*self.hecha_shuliang_loc).text.split(' 上传成功\n'))
                    if resultsss + 1 == resultss:
                        # print('成功')
                        mylogger.info("100%成功")
                        break
                    else:
                        mylogger.info("上传失败")
                        # print('失败')
        self.driver.find_element(*self.hecha_click_loc).click()
        # jieguo,jifen,jifens,results = self.hecha(2,mylogger)
        # print(jieguo,jifen,jifens,results)



    def shurruxingxi(self,password,gslx,jiaoyi,rongzi,hechayuan=''):
            time.sleep(1)
            self.driver.find_element(*self.shuru_xiangmuname_loc).clear()
            self.driver.find_element(*self.shuru_xiangmuname_loc).send_keys(password)
            time.sleep(1)
            self.driver.find_element(*self.xuanzhe_gslx_name_loc).click()
            time.sleep(1)
            gslx_all_loc = (By.XPATH, ("//span[text()='%s']" % gslx))
            self.driver.find_element(*gslx_all_loc).click()
            time.sleep(1)
            self.driver.execute_script("document.getElementsByClassName('el-select-dropdown el-popper')[0].style.display='block';")
            time.sleep(1)
            gslx_all_loc = (By.XPATH, ("//span[text()='%s']" % jiaoyi))
            self.driver.find_element(*gslx_all_loc).click()
            self.driver.execute_script(
                "document.getElementsByClassName('el-select-dropdown el-popper')[0].style.display='none';")
            time.sleep(1)
            self.driver.execute_script(
                "document.getElementsByClassName('el-select-dropdown el-popper')[1].style.display='block';")
            time.sleep(1)
            gslx_all_loc = (By.XPATH, ("//span[text()='%s']" % rongzi))
            self.driver.find_element(*gslx_all_loc).click()
            self.driver.execute_script(
                "document.getElementsByClassName('el-select-dropdown el-popper')[1].style.display='none';")

            self.driver.find_element(*self.hechayuan_shuru_loc).clear()
            self.driver.find_element(*self.hechayuan_shuru_loc).send_keys(hechayuan)
            # print('完美')
            time.sleep(1)


    def zhinengchuanshuju(self,xiangmuname,gslx,hechayuan):
        print(xiangmuname)
        time.sleep(2)
        self.driver.find_element(*self.shuru_xiangmuname_loc).clear()
        self.driver.find_element(*self.shuru_xiangmuname_loc).send_keys(xiangmuname)
        print(self.driver.find_element(*self.shuru_xiangmuname_loc).get_attribute('name'))
        time.sleep(2)

        self.driver.find_element(*self.xuanzhe_gslx_name_loc).click()
        time.sleep(2)
        self.driver.execute_script(
            "document.getElementsByClassName('el-select-dropdown el-popper')[1].style.display='block';")
        gslx_all_loc = (By.XPATH, ("//span[text()='%s']" % gslx))
        self.driver.find_element(*gslx_all_loc).click()
        self.driver.execute_script(
            "document.getElementsByClassName('el-select-dropdown el-popper')[1].style.display='none';")
        time.sleep(2)
        self.driver.find_element(*self.hechayuan_shuru_loc).clear()
        self.driver.find_element(*self.hechayuan_shuru_loc).send_keys(hechayuan)


        # return self.driver
    def hecha(self,a,mylogger):
        mylogger.info("获取现有积分")
        jifen = self.driver.find_element(*self.jifen_huoqu_loc).text[5:]
        time.sleep(1)
        mylogger.info("点击开始核查")
        self.driver.find_element(*self.hecha_click_loc).click()
        mylogger.info("判断进度")
        while True:
            time.sleep(1)
            self.driver.refresh()
            # self.driver.find_elem
            time.sleep(1)
            result = self.driver.find_element(*self.hecha_zhuangtai_loc).text
            # print(result)
            if result.replace(" ", "") == '解析完成':
                mylogger.info("解析完成")
                jieguo, jifens = self.jiexishibai()
                results = '成功'
                break
            elif result.replace(" ","") == "解析失败":
                jieguo, jifens = self.jiexishibai()
                results = '失败'

                break
        mylogger.info("结果%s"%jieguo)
        return jieguo,jifen,jifens,results
    def jifenhuoqu(self):
        self.driver.refresh()
        time.sleep(0.7)
        jifen = self.driver.find_element(*self.jifen_huoqu_loc).text[5:]
        return jifen
    def jiexishibai(self):
        jifens = self.jifenhuoqu()
        self.driver.find_element(*self.hecha_zhuangtai_loc).click()
        time.sleep(0.5)
        jieguo = self.driver.find_element(*self.jiexixiangqing_xingxi_loc).text.split('\n')
        # for i in range(0,len(jieguo),3):
        #     print(jieguo[i])wed
        # print(jieguo)
        jieguo = baogao(jieguo)
        time.sleep(0.5)
        self.driver.find_element(*self.guanbi_loc).click()
        return jieguo,jifens

    def jiexichenggong(self):
        jifens = self.jifenhuoqu()
        self.driver.find_element(*self.hecha_zhuangtai_loc).click()
        time.sleep(0.5)
        jieguo = self.driver.find_element(*self.jiexixiangqing_xingxi_loc).text.split('\n')
        # for i in range(0,len(jieguo),3):
        #     print(jieguo[i])
        # print(jieguo)
        jieguo = baogao(jieguo)
        time.sleep(5)
        self.driver.find_element(*self.guanbi_loc).click()
        time.sleep(5)
        return jieguo, jifens
    def tishi(self):
        while True:
            try:
                # time.sleep(2)
                nananan = self.driver.find_element(*self.baocuo_xingxi_loc).text.replace(" ", "")
                return nananan
            except:
                print('没有')
        # a = self.tishi()
        # print(a)
    def putong(self,name_url):
        mylogger = Logger(logger='普通上传').getlog()
        time.sleep(4)
        self.driver.find_element(*self.qiehuan_anniu_loc).click()
        self.shurruxingxi(name_url[1][0],name_url[1][1],name_url[1][2],name_url[1][3],name_url[1][4])
        self.driver.find_element(*self.xiayibu_loc).click()
        # gongzhuanshu_locself.driver.find_element(*self.wenjianhsnagchuan_loc).send_keys("D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\傲基科技：招股说明书 0828-0341.docx")
        # self.driver.find_element(*self.gongzhuanshu_loc).click()
        for i in range(len(name_url[0])):
            for j in range(len(name_url[0][i])):
                print(name_url[0][i][j])
                if j != 0:
                    shangchuan_2_loc = (By.XPATH, ("(//span[text()='点击上传'])[%s]"%str(i+1)))
                    self.driver.find_element(*shangchuan_2_loc).click()
                else:
                    time.sleep(1)
                    self.driver.find_element(*self.gongzhuanshu_loc).click()

                time.sleep(1)
                os.system(r'D:\jb\shangchuan.exe %s' % name_url[0][i][j])
                hhh = self.tishi()
                print(hhh)

        time.sleep(1)

        # self.driver.find_element(*self.putonghecha_kaishi).click()
        # print(self.driver.find_element(*self.pt_1_shuliang_loc).text)
        jieguo, jifen, jifens, results = self.hecha(1,mylogger)
        print(jieguo, jifen, jifens, results)


    def shanchu_wenjian(self):
        pass

