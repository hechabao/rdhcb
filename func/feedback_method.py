import requests
import re
import ast
import json




def get_the_key():
    # 获取crm的cookie
    data = {"username": "hcb@test.com", "password": "hcb1234567"}
    url = "	https://hcbcrm.rongdasoft.com:8010/dologin"
    response = requests.post(url=url, data=data)
    # print(response)
    # 获取requests请求返回的cookie
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    # print(cookie)
    return "JSESSIONID="+str(cookie["JSESSIONID"])



def huoqu(data_fields,data_m):
    list = []
    data_identifier = ['机构名称','联系人','联系邮箱','联系电话','联系地址','文件类型','财务数据范围','非财务数据范围','正文内容范围','其他1','跨版本对比核查','本地化部署','在线充值','其他2','时间1','时间2']
    data_key = ['institution_name','person','email','phone','address','filetype','finance_scope','not_finance_scope','text_scope','other_scope','newNeedOne','newNeedTwo','newNeedThree','newNeedFour','create_time','update_time']

    url = "	https://hcbcrm.rongdasoft.com:8010/feedbacks/list"
    headers={"Host": "47.93.180.226:10080",
        "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
        "Referer": "https://hcbcrm.rongdasoft.com:8010/user/userManager",
        "Cookie": get_the_key()
    }
    html = requests.get(url,headers=headers).content.decode('utf-8','ignore')
    # print(html)
    data_n = re.findall(r"\{(.*?)\}",str(re.findall(r".*?data : \[(.*?)]",html)))
    print(data_n)
    for i in data_n:
        maaaa = json.loads(("{"+i+"}").replace('\\xa0',' '))
        list.append(maaaa)
    if data_fields == '新增功能需求':
        data_fields = data_m
    data_shuju_fields = data_identifier.index(data_fields)
    return list[0].get(data_key[data_shuju_fields])

def weishu_shengchenqi(weishuss):
    a = ''
    for i in range(weishuss):
        # print(a)
        a +='哇'
    print(len(a))
    return a


print(huoqu('联系邮箱',"文件类型"))
# print(weishu_shengchenqi(11))
# print(get_the_key())其他再融资报告,文件类型
