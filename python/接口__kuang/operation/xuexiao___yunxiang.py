#!/use/bin/python
# -*- coding:utf-8 -*-
from 接口__kuang.test_case.denglu__taojain import Yx
with open(r'C:\Users\zhujh\PycharmProjects\untitled1\a.txt','r')as f:
    bbb=f.readlines()
    print(bbb)
for i in bbb:
    if 'all' in bbb:
        Yx('*')
    else:
        Yx(i)

