# import json
#
# date = {
#     'id': 1,
#     'name': 'wupeng',
#     'school': None
# }
# json_str = json.dumps(date)
# print(json_str)
# JSON字符串转换为python字典
#
# import json
#
# json_str = '{"id": 1,"name": "wupeng","school":null}'
# python_str = json.loads(json_str)
# print(python_str)
import requests
import re

import json


def huoqu():
    url = "http://47.93.138.236:8010/crm/feedbacks/list"
    headers = {"Host": "47.93.180.226:10080",
               "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Accept-Encoding": "gzip, deflate",
               "Referer": "http://47.93.138.236:8010/crm/user/userManager",
               "Connection": "keep-alive",
               "Cookie": "JSESSIONID=1C8539F81D2CE69F82FF20DADA3464C7",
               "Upgrade-Insecure-Requests": "1"
               }

    html = requests.get(url, headers=headers).content.decode('utf-8', 'ignore')

    n = re.findall(r"\{(.*?)\}", str(re.findall(r".*?data : \[(.*?)]", html)))

    # for i in n[0].split(','):
    #     print(i)
    list = []
    for i in n:
        # print(i)
        maaaa = json.loads(("{" + i + "}").replace('\\xa0', ' '))
        # print(i)
        list.append(maaaa)

        print(maaaa)
    # print(html)
    return list
