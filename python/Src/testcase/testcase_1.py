#!/use/bin/python
# -*- coding:utf-8 -*-
from Src.func.func_1 import foo,qq,wb,mlma
from appium import webdriver
import time
import unittest
from 学习 import HTMLTestRunner
from Src.testcase.rizhi import get_logger
g=get_logger(name='testcast_1.py')

class Text(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
                d = {
                        "platformName": "Android",
                        "platformVersion": "5.1.1",
                        "deviceName": "emulator-5554",
                        "appPackage": "com.qk.butterfly",
                        "appActivity": ".main.LauncherActivity",
                        "noReset": "True"
                }
                # @classmethod
                # def setUpClass(cls):
                cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
                time.sleep(4)
                g.info("app建立连接完成！")
        @classmethod
        def tearDownClass(cls):
                cls.dr.quit()
                g.info("app关闭")
        def test_qq(self):
                g.info("执行测试用例")
                self.assertEqual(qq(self.dr),'QQ')
        def test_wx(self):
                g.info("执行测试用例")
                self.assertEqual(foo(self.dr),'微信')
        def test_wb(self):
                g.info("执行测试用例")
                self.assertEqual(wb(self.dr),'微博')
        def test_pw(self):
                g.info("执行测试用例")
                self.assertEqual(mlma(self.dr),'密码')
if __name__ == '__main__':
        # unittest.main()
#
        suit=unittest.TestSuite()
        # dis = unittest.defaultTestLoader.discover(r'C:\Users\zhujh\PycharmProjects\untitled1\Src\testcase',pattern='test_{}.py'.format(name.strip()))
        suit.addTest(unittest.makeSuite(Text))
        # lujing =
        ff = open(r'C:\Users\zhujh\PycharmProjects\untitled1\Src\report\diesheng.html', 'wb')  # 打开一个空文件
        runner = HTMLTestRunner.HTMLTestRunner(stream=ff, title='接口测试报告', tester='朱家豪', description='结果如下')  # 定义测试报告的信息
        # 执行测试套件0m
        # suit(dis)
        # print('111')
        runner.run(suit)



