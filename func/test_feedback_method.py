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
    headers = {"User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
               "Referer": "http://47.93.138.236:8010/crm/user/userManager",
               "Cookie": "JSESSIONID=1C8539F81D2CE69F82FF20DADA3464C7",
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
