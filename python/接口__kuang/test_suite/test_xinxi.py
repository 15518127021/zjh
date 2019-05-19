#!/use/bin/python
# -*- coding:utf-8 -*-
import unittest
import xlrd
f = xlrd.open_workbook(r'C:\Users\zhujh\PycharmProjects\untitled1\a.xls')
sheet = f.sheets()[0]
row_1 = sheet.nrows
from 接口__kuang.url__get.jiekou import Denglu
# from 学习 import HTMLTestRunner
from 接口__kuang.read.read_xls import Duqu
class CalTest(unittest.TestCase):
    bb=Denglu().dizi
    # aa=Duqu()
    def setUp(self):  # 初始化测试环境
        print('测试开始')
    def tearDown(self):  # 清理测试环境
        print('测试结束')
    def test_1(self):  # 有效
        bbb = self.bb(int(sheet.cell(1, 0).value), int(sheet.cell(1, 1).value))
        # print('查询成功,学校如下')
        # print(bbb)
        self.assertEqual(bbb['code'], 0)
        print('__login successfully__')

    def test_2(self):  # 无效
        for i in range(2, row_1):
            ccc = self.bb(int(sheet.cell(i, 0).value), int(sheet.cell(i, 1).value))
            # print(ccc)
            self.assertNotEqual(ccc['code'], 0)
            print('__This is an incorrect input__')
if  __name__=='__main__':
    unittest.main()