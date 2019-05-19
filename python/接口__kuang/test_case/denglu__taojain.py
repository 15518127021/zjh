#!/use/bin/python
# -*- coding:utf-8 -*-
import unittest
from 学习 import HTMLTestRunner
from 接口__kuang.test_suite.test_denglu import CalTest
def Yx(name):
        # unittest.main()
        # 创建一个测试套件
    # for j in name:
    suit=unittest.TestSuite()
            # 1、将测试用例添加到测试套件
            # suit.addTest(Denglu('test_1'))
            # suit.addTest(Denglu('test_2'))
            # 2、运行这个路径下的以text开头的.py文件
    dis=unittest.defaultTestLoader.discover(r'C:\Users\zhujh\PycharmProjects\untitled1\接口__kuang\test_suite',pattern='test_{}.py'.format(name.strip()))
            # 3、将Denglu类中所有的以test开头的函数都添加到测试套件里
        # suit.addTest(unittest.makeSuite(CalTest))
    ff = open(r'C:\Users\zhujh\PycharmProjects\untitled1\接口__kuang\dig\abc.html','wb')        # 打开一个空文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=ff,title='接口测试报告',tester='朱家豪',description='结果如下')     #定义测试报告的信息
            #执行测试套件0m
        # suit(dis)
    # print('111')
    runner.run(suit(dis))
    ff.close()
# for i in
# Yx()
if __name__ == '__main__':
    pass