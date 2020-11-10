# # text = ["公转书", "未知错误", "2【傲基科技】法律意见书20190827clean.doc", "财务报表", "解析成功", "深圳分所：大华审字(2019)009872号傲基科技股份有限公司5+1份-数字.xlsx"]
# # text = ["招股书", "解析成功", "1-1招股说明书（申报稿）.docx", "审计报告", "未知错误", "事业五部-大华审字[2017]002795号-爱美客技术发展股份有限公司-4+1份.doc", "财务报表", "未知错误", "事业五部-大华审字[2017]002795号-爱美客技术发展股份有限公司报表-4+1份.xls"]
# # jianyi = []
# # name = []
# # shibai = 0
# # chengong = 0
# # shibaiwenjian = []
# # if len(text)/3 == 0:
# #     for i in range(0,len(text),3):
# #         if text[i + 1] == "未知错误":
# #             shibai += 1
# #             shibaiwenjian.append(text[i + 2])
# #         elif text[i + 1] == "解析成功":
# #             chengong += 1
# #             name.append(text[i + 2])
# # elif len(text)/3 != 0:
# #     for i in range(0, len(text), 3):
# #         try:
# #             if text[i+1] == "未知错误":
# #                 shibai+=1
# #                 shibaiwenjian.append(text[i+2])
# #             elif text[i+1] == "解析成功":
# #                 chengong+=1
# #                 name.append(text[i+2])
# #         except:
# #             jianyi.append(text[i])
# # if len(jianyi) == 0:
# #     jianyi.append("没有建议")
# #
# # print(jianyi,name,shibai,chengong,shibaiwenjian)
# # print("成功%d个分别是%s文件，\n失败%d个分别是%s文件,\n建议%s\n"%(chengong,name,shibai,shibaiwenjian,jianyi))
#     # 成功n个分别是哪些文件，失败m个分别是那些文件
# # name_url = [["D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\傲基科技：招股说明书 0828-0341.docx"],
# #             ["D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\2【傲基科技】法律意见书 20190827 clean.docx","D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\2【傲基科技】法律意见书 20190827 clean.docx"],
# #             ["D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\深圳分所：大华审字(2019)009872号傲基科技股份有限公司5+1份-数字.xlsx"]]
#
#
#
#
#
# # import  unittest
# # #定义一个类，并继承类
# # class TestCase(unittest.TestCase):
# #     # 定义测试用例：前置条件、后置条件、用例1、用例2
# #     def setUp(self):
# #         print("start!")
# #     # def tearDown(self):
# #     #     print("end!")
# #     def test01(self):
# #         print("测试用例1")
# #     def test_03(self):
# #         print("测试用例3")
# #         # print(i)
# #         # print("end!")
# #     def test_02(self):
# #         print("测试用例2")JSESSIONID=4DC2CF0D04E1B5A85B1333DB011D94D3; SERVERID=3c38e0a2225151115edaa04db744a2bf|1599120080|1599117539
# #     def addtest(self):
# #         print("add方法")192.168.10.38/8010/statistics/loginDetailList
# # # 运行主方法
# # if __name__=="__main__":
# #     unittest.main()
import requests
import re
import ast
import json
#
#
# url = "https://crm.rongdasoft.com:10080/crm/orderList"
# headers={"Host": "crm.rongdasoft.com:10080",
#     "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#     "Accept-Encoding": "gzip, deflate",
#     "Referer": "https://crm.rongdasoft.com:10080/crm/orderList",
#     "Connection": "keep-alive",
#     "Cookie": "JSESSIONID=4DC2CF0D04E1B5A85B1333DB011D94D3; SERVERID=3c38e0a2225151115edaa04db744a2bf|1599120080|1599117539",
#     "Upgrade-Insecure-Requests": "1"
# }
# html = requests.get(url,headers=headers).content.decode("utf-8","ignore")
# print(html)
# n = re.findall(r"\{(.*?)\}",str(re.findall(r".*?data : \[(.*?)]",html)))
#
#
# print(n)
# # for i in n[0].split(","):
# #     print(i)vvv
# list = []
# for i in n:
#     print(i)
#     maaaa = json.loads(("{"+i+"}").replace("\\xa0"," "))
#     # print(i)
#     list.append(maaaa)
#
#     print(maaaa)
# # url = "https://crm.rongdasoft.com:10080/crm/orderList"
# # html = requests.get(url,headers=headers).content.decode("utf-8","ignore")
# # print(html)
#
# import requests
# url = "https://home.meishichina.com/show-top-type-recipe.html"
# html = requests.get(url).content.decode("utf-8","ignore")
# print(html)
# endpoint = "post"
# data = {
#         "Cookie": "JSESSIONID=1E0835B2B249E7F107A3322DE8A9842F; SESSION=MWYwOGMzNjItNzYxOS00YzIzLWI4MWYtZmQ4ZDUyNTQyNjJk",
# }
# url = 'https://check.rongdasoft.com:21000/user/updatePassword?password=123456&newPassword=1" and 1=2'
# print(url)
# headers = {"Host": "check-test.rongdasoft.com:21000",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
#     "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
#     "Origin": "https://check.rongdasoft.com:21000",
#     "Connection": "keep-alive",
#     "Cookie": "JSESSIONID=A176F65299C59FB18B2BD3160F392BDB; SESSION=NWFlNzU0OTEtN2MyOC00MzBkLTk0ZTQtY2NmYmEzNzQ2YzA5",
#     }
#
# # r = requests.post(url)
# print("开始")
# r = requests.post(url,headers=headers).content.decode("utf-8","ignore")
# print(r)
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import requests
# import time
# import re
#
# urllll = "https://www.baidu.com"
# driver = webdriver.Chrome()
# driver.get(urllll)
# time.sleep(1)
# ht = driver.page_source
# # print(ht)
# print('11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
# soup = BeautifulSoup(ht,"html.parser")
# # print(soup)
# # a = soup.find_all('a')
# # print(a)
# for tag in soup.find_all(True):
#     print(tag.name)
#
# list = []
# for i in range(0,6):
#     if i == 0 or i == 1:
#         list.append(i*2)
#     else:
#         a = 2
#         for j in range(i-1):
#             a = a*2
#         list.append(a)
# print(list)
# -*- coding: utf-8 -*-
# import dingtalk.api
#
# req=dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
#
# try:
# 	resp= req.getResponse(access_token)
# 	print(resp)
# except e:
# 	print(e)
# import json
# import requests
# data = {"token":"26e07460e9de407394b77e331e59e394","userId":1,"data":{"id":36},"projectId":36,"loginType":"web"}
# headers = {
# "Content-Type": "application/json;charset=utf-8"
# }
# a = requests.post(url="http://192.168.6.230:212/info/project/getProjectInfo",data=json.dumps(data),headers=headers).content.decode('utf-8', 'ignore')
# print(a)

from selenium.webdriver.common.by import By
import time
import re
import os
import selenium
from base.basePage import BasePage

class test_XXXXXXXXX(BasePage):
    #元素定位
    username_input_loc = (By.CLASS_NAME, 'el-input__inner')

    # 操作的方法
    def input_username(self,username):
        self.driver.find_element(*self.username_input_loc).send_keys(username)










