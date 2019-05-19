#!/use/bin/python
# -*- coding:utf-8 -*-
from jiekou.m_test.test_guojia import qwe
import unittest
from jiekou.report import HTMLTestRunner
def Guojia_baogao():
    suit = unittest.TestSuite()
    # 两个参数，1，路径  2，通配符
    # for i in name:
    #     dis = unittest.defaultTestLoader.discover(r'C:\Users\zhujh\PycharmProjects\untitled1\jiekou\m_test',pattern='test_{}.py'.format(i.strip()))
    #     for j in dis:
    #         suit.addTest(j)
    # 1、将测试用例添加到测试套件
    # suit.addTest(Denglu('test_1'))
    # suit.addTest(Denglu('test_2'))
    # 2、运行这个路径下的以text开头的.py文件
    # dis = unittest.defaultTestLoader.discover(r'C:\Users\zhujh\PycharmProjects\untitled1\接口__kuang\test_suite',
    #                                           pattern='test_{}.py'.format(name.strip()))
    # 3、将Denglu类中所有的以test开头的函数都添加到测试套件里
    suit.addTest(unittest.makeSuite(qwe))
    f = open(r'C:\Users\zhujh\PycharmProjects\untitled1\jiekou\logg\guojia.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='国家接口测试报告', tester='朱家豪', description='结果如下')
    runner.run(suit)
    f.close()
# Guojia_baogao()

if __name__ == '__main__':
    pass