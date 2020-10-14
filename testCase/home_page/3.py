import requests
import json
#

endpoint = "post"
data = {"data":{"id":"4407","password":"a","newPassword":"a123456"},"token":"1e041050990843028e37a05a602d084e","userId":"5322","projectId":"4417","loginType":"web"}
url = 'http://39.106.254.225/sys/updatePassword'
headers = {"Connection": "keep-alive",
    "Content-Encoding": "gzip",
    "Content-Type": "application/json;charset=UTF-8",
    "Date":"Fri, 04 Sep 2020 01:44:35 GMT",
    "Server": "nginx/1.16.0",
    "Transfer-Encoding": "chunked",
    "Vary": "Accept-Encoding",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "158",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "39.106.254.225",
    "Origin": "http://39.106.254.225",
    "Referer": "http://39.106.254.225/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

# r = requests.post(url)
r = requests.post(url,json=data).content.decode('utf-8','ignore')
print(r)
#response = r.json()
# endpoint = "post"
# data = {"data":{"id":"5322","password":"a123456","newPassword":"a"},"token":"72422461673e45ea95da0edc4be41339","userId":"282","projectId":"4368","loginType":"web"}
# url = 'https://check.rongdasoft.com:20000/user/updatePassword'
# headers = {"Connection": "keep-alive",
#     "Content-Encoding": "gzip",
#     "Content-Type": "application/json;charset=UTF-8",
#     "Date":"Fri, 04 Sep 2020 01:44:35 GMT",
#     "Server": "nginx/1.16.0",
#     "Transfer-Encoding": "chunked",
#     "Vary": "Accept-Encoding",
#     "Accept": "application/json, text/plain, */*",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Connection": "keep-alive",
#     "Content-Length": "158",
#     "Content-Type": "application/json;charset=UTF-8",
#     "Host": "39.106.254.225",
#     "Origin": "http://39.106.254.225",
#     "Referer": "http://39.106.254.225/",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
#
# # r = requests.post(url)
# r = requests.post(url,json=data).content.decode('utf-8','ignore')
# print(r)
# response = r.json()