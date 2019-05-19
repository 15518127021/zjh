#!/use/bin/python
# -*- coding:utf-8 -*-
import  xlrd
def Duqu():
    f = xlrd.open_workbook(r'C:\Users\zhujh\PycharmProjects\untitled1\a.xls')
    sheet = f.sheets()[0]
    # print(sheet)
    row_1 = sheet.nrows
    # print(row_1)
    # return sheet
Duqu()