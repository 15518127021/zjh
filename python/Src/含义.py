#!/use/bin/python
# -*- coding:utf-8 -*-
# datas    读取数据
# element   存放定位元素
# func          函数脚本
# testcase  测试用例
# logs  日志
# report   报告
# until  公共部分，整个项目都会用到的公共部分

# 导入appium模块的webriver
from appium import webdriver
import time
# 测试
d = {
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "emulator-5554",
      "appPackage": "com.qk.butterfly",
      "appActivity": ".main.LauncherActivity",
      "noReset": "True"
    }
# 测试脚本是appium服务器与手机建立连接的过程
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
time.sleep(5)
# 登录元素id定位
# dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()
# 元素的多级定位
# text=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# print(text)
# # dr.find_element_by_link_text('').click()
# tex=dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# print(tex)
# te=dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# print(te)
# t=dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
# print(t)
# time.sleep(3)
# send_keys  1.在输入数据，2.clickable为true的，3.enables为true，4.foucsable为true时候，输入的是字符串
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()

dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15518127021')
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('qwe123')
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
time.sleep(5)
# 退出app包括后台进程
dr.quit()