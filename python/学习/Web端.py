#!/use/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
# dr = webdriver.Firefox()  #定义打开的浏览器
# dr.get('https://www.zhipin.com')    #请求的网页
# time.sleep(1)
# dr.get('https://www.baidu.com')
# dr.back()   #返回上一次打开的网页
# dr.forward()    # 前进
# print(dr.title)  #获取网页的标题
# print(dr.current_url) #获取网页的网址
# dr.quit() #关闭浏览器
# dr.set_window_size(800,400)#  改变网页窗体大小
# dr.set_window_position(300,200)  #设置浏览器窗口的位置
# time.sleep(2)
# dr.maximize_window()  #最大化浏览器
# time.sleep(2)
# dr.minimize_window()  #最下话浏览器
# dr.find_element_by_name('query').send_keys('自动化测试')
# dr.find_element_by_xpath('/html/body/div/div[3]/div/div/div[1]/form/button').click()
# 单个定位的时候要保证 class 的值要唯一
# time.sleep(1)
# dr.find
# dr.quit()
# #  tag_name定位  标签页定位
#  xpath定位   路径定位
# css 选择器 路径定位
# dr.find_element_by_css_selector()
# clear 清除、text  文本、click  点击、send_keys 输入
# 层级定位：先定位一个顶层元素，再定位这个元素的子元素
# 弹出框 叫 alert
# iframe  网页框架
# 进入到框架
# dr.switch_to_frame()
# 退出框架，推出到最初的框架
# dr.switch_to_default_content()
# 切换到上一个框架
# dr.switch_to.parent_frame()
# 切换窗口
# dr.switch_to_window('标识')
# 获取当前窗口的标识
# dr.current_window_handle
# 获取所有的窗口标识
# dr.window_handles

# dr.switch_to_window(dr.window_handles[1])

# class QQ():
#     dr = webdriver.Firefox()
#     dr.get('https://i.qq.com')
#     time.sleep(2)
#     dr.switch_to.frame('login_frame')
#     def Zh(self):
#         self.dr.find_element_by_id('switcher_plogin').click()
#         self.dr.find_element_by_id('u').send_keys('2469360064')
#         time.sleep(2)
#         self.dr.find_element_by_id('p').send_keys('1998050266')
#     def Dl(self):
#         self.dr.find_element_by_xpath('//*[@id="login_button"]').click()
#         time.sleep(6)
#         # self.dr.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div[1]/a[2]/i').click()
# #       切换到alert上去，自动点击确定
# #         ww=self.dr.switch_to.alert()
# #         print(ww.text)
# #         ww.accept()   #来 点击确定
# a=QQ()
# a.Zh()
# a.Dl()


# dr = webdriver.Firefox()
# dr.get('file:///C:/Users/zhujh/Desktop/abc.html')
# dr.find_element_by_xpath('/html/body/input').click()
# time.sleep(2)
# ww = dr.switch_to_alert()
# print(ww.text)
# # ww.accept()  #确定
# # ww.dismiss()   #取消
# ww.send_keys('beujing')
# time.sleep(2)
# ww.accept()

dr = webdriver.Firefox()
dr.get('https://www.taobao.com')
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[1]/li[2]/div[1]/div[1]/a[1]').click()
# time.sleep(10)
dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/a[2]').click()
dr.switch_to.window(dr.window_handles[1])
# print(dr.title)
dr.find_element_by_class_name('theme-bd-level2') 
dr.find_elements_by_css_selector('/html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/dl[2]')[2].click()
# dr.find_element_by_xpath('//*[@id="J_Itemlist_TLink_551444482105"]').click()
# dr.switch_to_window(dr.window_handles[-1])
# dr.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[7]/div/dl[1]/dd/ul/li[2]').click()
# dr.find_element_by_xpath('dr.find_element_by_xpath').click()
# dr.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[7]/div/div[3]/div[2]/a').click()


# dr.switch_to_frame('//*[@id="J_Form"]')
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[2]').click()
# dr.find_element_by_xpath('//*[@id="J-input-user"]').send_keys('15518127021')
# dr.find_element_by_xpath('//*[@id="password_rsainput"]').send_keys('zjh520000')
# dr.find_element_by_xpath('//*[@id="J-login-btn"]').click()
# aa=dr.current_window_handle
# print(aa)
# time.sleep(2)
# dr.switch_to.window(dr.window_handles[1])
# # bb=dr.switch_to_window(aa)
# time.sleep(2)
# print(dr.title)