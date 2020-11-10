#
# # coding=utf-8
#
# import re
# n = '''
#  data : [{"id":45,"institution_name":"1","person":"2","email":"hcb@test.com","phone":"","address":"","filetype":"","finance_scope":"","not_finance_scope":"","text_scope":"","other_scope":"","newNeedOne":"","newNeedTwo":"","newNeedThree":"","newNeedFour":"","create_time":"2020-08-19 19:04:30","update_time":"2020-08-19 19:04:30"},{"id":44,"institution_name":"11111111111111111111111111111111111111111111111111","person":"111111111111111","email":"sj17600446278@163.com","phone":"11111111111","address":"11111111111111111111111111111111111111111111111111","filetype":"重组报告-基金募集报告-保荐书-行研报告-审计报告-评级报告-定期报告（年报等）-固收报告-其他股/债申报底稿-债券发行报告（公司债、企业债、可转债、金融债、PPN等）-法律意见书-其他再融资报告","finance_scope":"数据一致性-科目勾稽关系-行研报告-指标变动异常-财务指标-经营指标-可比公司指标核查-固收报告-发行指标","not_finance_scope":"股权变动连续性-商标信息-股东基本信息-合同编号-专利信息-子分公司基本信息-采购及销售信息等-行业数据-主要客户/供应商基本信息-发行人基本信息","text_scope":"中介文件一致性引用-其他低级错误类型（含错别字、符号、变动计算等）-信披完备性-语句/段落描述完整性","other_scope":"","newNeedOne":"跨版本对比核查","newNeedTwo":"","newNeedThree":"","newNeedFour":"","create_time":"2020-07-13 11:17:34","update_time":"2020-07-13 11:17:34"},{"id":43,"institution_name":"asda","person":"dasdasd","email":"asdasd","phone":"17600446279","address":"asdasdasdasdasdasdasd","filetype":"","finance_scope":"","not_finance_scope":"","text_scope":"","other_scope":"","newNeedOne":"","newNeedTwo":"","newNeedThree":"","newNeedFour":"","create_time":"2020-07-10 15:28:03","update_time":"2020-07-10 15:28:03"},{"id":42,"institution_name":"d","person":"d","email":"hcb@test.com","phone":"","address":"","filetype":"","finance_scope":"","not_finance_scope":"","text_scope":"","other_scope":"","newNeedOne":"","newNeedTwo":"","newNeedThree":"","newNeedFour":"","create_time":"2020-01-14 09:34:16","update_time":"2020-01-14 09:34:16"},{"id":41,"institution_name":"1","person":"2","email":"502900588@qq.com","phone":"3","address":"4","filetype":"定期报告（年报等）-评级报告","finance_scope":"科目勾稽关系","not_finance_scope":"主要客户/供应商基本信息","text_scope":"其他低级错误类型（含错别字、符号、变动计算等）","other_scope":"5","newNeedOne":"跨版本对比核查","newNeedTwo":"","newNeedThree":"","newNeedFour":"6","create_time":"2020-01-14 09:21:09","update_time":"2020-01-14 09:21:09"},{"id":38,"institution_name":"12345678901234567890123456789012345678901234567890","person":"123456789012345","email":"502900588@qq.com","phone":"12345678901","address":"12345678901234567890123456789012345678901234567890","filetype":"其他再融资报告-基金募集报告-保荐书-债券发行报告（公司债、企业债、可转债、金融债、PPN等）-重组报告-审计报告-行研报告-固收报告-评级报告-定期报告（年报等）-其他股/债申报底稿-法律意见书","finance_scope":"数据一致性-科目勾稽关系-行研报告-指标变动异常-财务指标-可比公司指标核查-经营指标-发行指标-固收报告","not_finance_scope":"发行人基本信息-主要客户/供应商基本信息-行业数据-采购及销售信息等-专利信息-子分公司基本信息-合同编号-股东基本信息-股权变动连续性-商标信息","text_scope":"中介文件一致性引用-其他低级错误类型（含错别字、符号、变动计算等）-信披完备性-语句/段落描述完整性","other_scope":"123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890","newNeedOne":"跨版本对比核查","newNeedTwo":"本地化部署","newNeedThree":"在线充值","newNeedFour":"123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890","create_time":"2019-09-20 10:52:49","update_time":"2019-09-20 10:52:49"},{"id":37,"institution_name":"11111111111111111111111111111111111111111111111111","person":"111111111111111","email":"11111111111111111111111111111111111111111111111111","phone":"15295771258","address":"11111111111111111111111111111111111111111111111111","filetype":"固收报告","finance_scope":"科目勾稽关系","not_finance_scope":"主要客户/供应商基本信息","text_scope":"其他低级错误类型（含错别字、符号、变动计算等）","other_scope":"","newNeedOne":"跨版本对比核查","newNeedTwo":"本地化部署","newNeedThree":"在线充值","newNeedFour":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","create_time":"2019-09-20 10:51:56","update_time":"2019-09-20 10:51:56"},{"id":36,"institution_name":"12345678901234567890123456789012345678901234567890","person":"123456789012345","email":"502900588@qq.com","phone":"12345678901","address":"12345678901234567890123456789012345678901234567890","filetype":"债券发行报告（公司债、企业债、可转债、金融债、PPN等）-行研报告-其他股/债申报底稿-固收报告-评级报告-定期报告（年报等）-重组报告-审计报告-基金募集报告-保荐书-其他再融资报告-法律意见书","finance_scope":"可比公司指标核查-经营指标-指标变动异常-财务指标-数据一致性-科目勾稽关系-行研报告-发行指标-固收报告","not_finance_scope":"采购及销售信息等-行业数据-主要客户/供应商基本信息-发行人基本信息-子分公司基本信息-专利信息-股东基本信息-股权变动连续性-商标信息-合同编号","text_scope":"其他低级错误类型（含错别字、符号、变动计算等）-中介文件一致性引用-信披完备性-语句/段落描述完整性","other_scope":"12345678901234567890123456789012345678901234567890","newNeedOne":"跨版本对比核查","newNeedTwo":"本地化部署","newNeedThree":"在线充值","newNeedFour":"12345678901234567890123456789012345678901234567890","create_time":"2019-09-20 09:09:51","update_time":"2019-09-20 09:09:51"},{"id":35,"institution_name":"12345678901234567890123456789012345678901234567890","person":"123456789012345","email":"502900588@qq.com","phone":"12345678901","address":"12345678901234567890123456789012345678901234567890","filetype":"评级报告-定期报告（年报等）-固收报告-其他股/债申报底稿-重组报告-审计报告-行研报告-基金募集报告-保荐书-债券发行报告（公司债、企业债、可转债、金融债、PPN等）-其他再融资报告-法律意见书","finance_scope":"数据一致性-科目勾稽关系-行研报告-财务指标-指标变动异常-经营指标-可比公司指标核查-发行指标-固收报告","not_finance_scope":"发行人基本信息-主要客户/供应商基本信息-行业数据-子分公司基本信息-专利信息-采购及销售信息等-合同编号-股东基本信息-股权变动连续性-商标信息","text_scope":"中介文件一致性引用-其他低级错误类型（含错别字、符号、变动计算等）-信披完备性-语句/段落描述完整性","other_scope":"12345678901234567890123456789012345678901234567890","newNeedOne":"跨版本对比核查","newNeedTwo":"本地化部署","newNeedThree":"在线充值","newNeedFour":"12345678901234567890123456789012345678901234567890","create_time":"2019-09-20 09:08:50","update_time":"2019-09-20 09:08:50"},{"id":34,"institution_name":"12345678901234567890123456789012345678901234567890","person":"123456789012345","email":"502900588@qq.com","phone":"12345678901","address":"","filetype":"定期报告（年报等）-评级报告-固收报告-其他股/债申报底稿-重组报告-审计报告-基金募集报告-保荐书-其他再融资报告-法律意见书","finance_scope":"发行指标-数据一致性-科目勾稽关系","not_finance_scope":"股权变动连续性-商标信息-股东基本信息-合同编号","text_scope":"语句/段落描述完整性-信披完备性-中介文件一致性引用","other_scope":"12345678901234567890123456789012345678901234567890","newNeedOne":"","newNeedTwo":"","newNeedThree":"","newNeedFour":"12345678901234567890123456789012345678901234567890","create_time":"2019-09-20 08:56:51","update_time":"2019-09-20 08:56:51"}],'''
# print(re.findall(r".*?data : \[(.*?)]",n))
#
# from selenium import webdriver
#news-list-body
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# import requests
# import re
# import ast
# import json
# url = "http://182.92.2.252:8010/crm/feedbacks/list"
# headers={"Host": "182.92.2.252:8010",
#     "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#     "Accept-Encoding": "gzip, deflate",
#     "Referer": "http://182.92.2.252:8010/crm/user/userManager",
#     "Connection": "keep-alive",
#     "Cookie": "JSESSIONID=D2CE5E0EE6423B47205A069584296590",
#     "Upgrade-Insecure-Requests": "1"
# }
#
# html = requests.get(url,headers=headers).content.decode('utf-8','ignore')
# print(html)
# n = re.findall(r"\{(.*?)\}",str(re.findall(r".*?data : \[(.*?)]",html)))
#
#
# # for i in n[0].split(','):
# #     print(i)vvv
# list = []
# for i in n:
#     # print(i)
#     maaaa = json.loads(("{"+i+"}").replace('\\xa0',' '))
#     # print(i)
#     list.append(maaaa)
#
#     print(maaaa)
#coding:utf-8   #字符集编码设置成UTF-8
  #发送post请求

import time
import hmac
import hashlib
import base64
import urllib.parse
# 17600446278
timestamp = str(round(time.time() * 1000))
secret = 'SEC25644221f3356cbc3ba949f64f46a89a86ac7d31a500701fa407993a737aad2f'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)
import requests,json   #导入依赖库
headers={'Content-Type': 'application/json'}   #定义数据类型
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=748ba163ab0d433093471b8cffbf9052c8fa519bcc6543f891b99c08044b72bb&timestamp=%s&sign=%s'%(timestamp,sign)  #定义webhook，从钉钉群机器人设置页面复制获得
#定义要发送的数据+86-13051296614+86-15600599039+86-17600446278
# 高尚13051296614
# 海15600599039
# 成龙17600446278


mobile = "13051296614"
data = {
    "msgtype": "text",
    "text": {"content": '晚上来成龙家咱们玩不要做挑战' },
    "at": {"atMobiles": "['']","isAtAll": True}
}
a = requests.post(url=webhook, data=json.dumps(data), headers=headers)
print(a)
data1 = {

}
# https://oapi.dingtalk.com/topapi/robot/org/intelligent/message/send