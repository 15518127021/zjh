#!/use/bin/python
# -*- coding:utf-8 -*-
import os
a=os.path.dirname(os.path.abspath(__file__))  #显示当前.py文件的绝对路径
print(a)
# 项目根目录
# a(src目录)
# 日志目录
b= a + '/logs/'
# 报告目录
c= a + '/report/'
# 源文件目录
d = a+'/src/'
# 测试用例目录
e = a + '/testcase/'
# 页面方法目录
f = a + '/func/'
#公共目录
g = a + '/until/'