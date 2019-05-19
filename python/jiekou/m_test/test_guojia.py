#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from jiekou.config.guojia import Guo

class qwe(unittest.TestCase):
    guoj = Guo().guo_qingqiu

    def test_qw(self):
        qq = self.guoj()
        self.assertEqual(qq['code'],0)
        self.assertEqual(qq['msg'],'OK')
    # def test_ww(self):
    #     ww = self.guoj()
    #     self.assertNotEqual(ww['code'],1)

if __name__ == '__main__':
    unittest.main()