import time

import requests
import json
from urllib import parse

header = {
    "language": "cn",
    "clientType": "app",
    "device": "android",
    "deviceId": "1a0018970afe5191f23",
    "vendorSign": "5c85bc7c363787844e0b7951",
    "User-Agent": "okhttp/3.11.0",
    "Connection": "keep-alive"
}
user_info = {"mobile": "18012989876",
             "password": "top123456",
             "device": "123456"}
url = 'http://aguav.test.topxgunuav.cn'
login_api = '/tagri/app/api/v1/user/signin?'
userdetail_api = '/tagri/app/api/v1/user/userDetail'


def jionurl(url,api):
    url = parse.urljoin(url, api)
    return url

r = requests.post(jionurl(url, login_api), headers=header, data=user_info)
data = r.json()["data"]
token = data["token"]
# print(token)
header["token"] = token
res = requests.get(jionurl(url, userdetail_api), headers=header, timeout=5)
print(header)
print(res.text)
