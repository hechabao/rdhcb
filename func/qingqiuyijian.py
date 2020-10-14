import requests
import re
import ast
import json
def huoqu(ns,m):
    a = ['机构名称','联系人','联系邮箱','联系电话','联系地址','文件类型','财务数据范围','非财务数据范围','正文内容范围','其他1','跨版本对比核查','本地化部署','在线充值','其他2','时间1','时间2']
    c = ['institution_name','person','email','phone','address','filetype','finance_scope','not_finance_scope','text_scope','other_scope','newNeedOne','newNeedTwo','newNeedThree','newNeedFour','create_time','update_time']
    b = ['跨版本对比核查', '本地化部署', '在线充值']
    url = "http://47.93.138.236:8010/crm/feedbacks/list"
    headers={"Host": "47.93.180.226:10080",
        "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://47.93.138.236:8010/crm/user/userManager",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=1C8539F81D2CE69F82FF20DADA3464C7",
        "Upgrade-Insecure-Requests": "1"
    }

    html = requests.get(url,headers=headers).content.decode('utf-8','ignore')

    n = re.findall(r"\{(.*?)\}",str(re.findall(r".*?data : \[(.*?)]",html)))


    # for i in n[0].split(','):
    #     print(i)
    list = []
    for i in n:
        # print(i)
        maaaa = json.loads(("{"+i+"}").replace('\\xa0',' '))
        # print(i)
        list.append(maaaa)

        # print(maaaa)

    if ns == '新增功能需求':
        ns = m
    print(list[0])
    print(ns)
    shuju1 = a.index(ns)
    print(shuju1)
    print(c[shuju1])
    # print(html)
    return list[0].get(c[shuju1])

def weishu_shengchenqi(weishuss):
    a = ''
    for i in range(weishuss):
        # print(a)
        a +='哇'
    print(len(a))
    return a
print(huoqu('机构名称',))
# print(weishu_shengchenqi(11))