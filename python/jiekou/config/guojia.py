#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import unittest
class Guo():
    def guo_qingqiu(self):
        url = "http://120.132.8.33:9000/api/Others/GetCountryList"

        payload = "{\r\n    \"phone\":\"15993835273\",\r\n    \"password\":\"111111\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"
        headers = {
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'Content-Type': "application/json",
            'x-access-token': "2b3e9f0348774c9ca551455a53f634d3",
            'cache-control': "no-cache",
            'Postman-Token': "2750edc8-1826-40d2-ba28-2abb3ae0a64b"
            }

        response = requests.request("GET", url, data=payload, headers=headers)

        gj = response.json()
        return gj
# if __name__ == '__main__':
    # unittest.defaultTestLoader