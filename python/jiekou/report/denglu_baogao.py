#!/usr/bin/python
#-*- coding:utf-8 -*-
from jiekou.report import HTMLTestRunner
import unittest

def Baogao(name):
    suit = unittest.TestSuite()
    # 两个参数，1，路径  2，通配符
    for i in name:
        dis = unittest.defaultTestLoader.discover(r'C:\Users\zhujh\PycharmProjects\untitled1\jiekou\m_test',pattern='test_{}.py'.format(i.strip()))
        for j in dis:
            suit.addTest(j)
    f = open(r'C:\Users\zhujh\PycharmProjects\untitled1\jiekou\logg\abc.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='朱家豪', description='结果如下')
    runner.run(suit)
    f.close()

if __name__ == '__main__':
    pass