#!/use/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
import time
import unittest
from 学习 import HTMLTestRunner
class Diesheng(unittest.TestCase):
    d = {
      "device": "android",
      "platformName": "Android",
      "platformVersion": "9",
      "deviceName": "1437f81",
      "appPackage": "com.vy.visvacn",
      "appActivity": ".SplashActivity",
      "noReset": "True"
    }
    dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
    time.sleep(2)
    def setUp(self):
        print('测试开始')
    def test_2 (self):
        time.sleep(4)
        self.dr.find_element_by_id('com.vy.visvacn:id/et_phone').send_keys('15518127021')
        self.dr.find_element_by_id('com.vy.visvacn:id/et_passwrd').send_keys('qwe12')
        self.dr.find_element_by_id('com.vy.visvacn:id/tv_done').click()
        tt = self.dr.find_element_by_id('com.vy.visvacn:id/v_visit').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(tt,'先逛一逛')
        print('__This is an incorrect input__')
    def test_3(self):
        time.sleep(4)
        self.dr.find_element_by_id('com.vy.visvacn:id/et_phone').send_keys('1551812702')
        self.dr.find_element_by_id('com.vy.visvacn:id/et_passwrd').send_keys('qwe123')
        self.dr.find_element_by_id('com.vy.visvacn:id/tv_done').click()
        time.sleep(2)
        tex = self.dr.find_element_by_id('com.vy.visvacn:id/v_visit').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(tex,'先逛一逛')
        print('__This is an incorrect input__')


        # 获取当前屏幕的分辨率
        # size = self.dr.get_window_size()
        #
        # x1 = size['width'] * 0.5  # x坐标 50
        # y1 = size['height'] * 0.25  # 起始y坐标 50
        # y2 = size['height'] * 0.75  # 150
        # for i in range(10):
        #     self.dr.swipe(x1, y2, x1, y1)
        #     time.sleep(2)#模拟手指上滑，实际屏幕下滑

    def tearDown(self):
        time.sleep(2)
        print('测试结束')
if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    # dis = unittest.defaultTestLoader.discover(r'C:\Users\zhujh\PycharmProjects\untitled1\Src\testcase',pattern='test_{}.py'.format(name.strip()))
    suit.addTest(unittest.makeSuite(Diesheng))
    ff = open(r'C:\Users\zhujh\PycharmProjects\untitled1\Src\report\diesheng.html', 'wb')  # 打开一个空文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=ff, title='接口测试报告', tester='朱家豪', description='结果如下')  # 定义测试报告的信息
    # 执行测试套件
    # suit(dis)
    # print('111')
    runner.run(suit)



