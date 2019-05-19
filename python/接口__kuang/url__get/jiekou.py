#!/use/bin/python
# -*- coding:utf-8 -*-
import unittest
import requests
class Denglu(unittest.TestCase):
    def dizi(self,username,password):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
        payload = '{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}' %(username,password)
        headers = {
                'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
                'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
                'Language': "zh_CN",
                'APIVersion': "3.0",
                'Content-Type': "application/json",
                'cache-control': "no-cache",
                'Postman-Token': "c3e8a8e4-d355-49b2-93b8-b4f814eb148a"
                }

        response = requests.request("POST", url, data=payload, headers=headers)

        zhuye=response.json()
        # print(zhuye)
        return zhuye
    # dizi()
