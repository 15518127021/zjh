#!/use/bin/python
# -*- coding:utf-8 -*-
# d=[]
# b=[ {'美女' :300},
#     {'电脑':200},
#     {'美团晚餐':666},
#     {'游艇':550}
#   ]
# e=[300,200,666,550]
# while True:
#     a=int(input('>>>请输入你的余额：'))
#     if a>=0:     #判断你输入的金额是否为正数
#         break
#     else:
#         print('你的余额为负数！')
# while True:
#     print('商店商品如下：')
#     for i,j in enumerate(b):   #将列表中每个数据和下标位置对应显示
#         print(i+1,j)
#     c=int(input('>>>请输入你要购买物品的序号： 付款请安0：'))
#     wo=input('>>>商品已加入购物车,退出购买请按w,返回购买请按p!!')
#     if c==0:
#         print('购买成功，你的余额为：')
#         print(a)
#         break
#     if e[c-1]<=a or wo=='p':           #循环判断你的余额是否大于你要购买物品的价格
#         a=a-e[c-1]           #余额减去你购买物品的价格
#         d.append(b[c - 1])     #把你购买的物品添加到空列表d
#         print('你的购物车如下：')
#         print(d)                  #打印购物车
#     if wo=='w':
#         break
# if a<=0 or a>=0:
#     while True:
#         print('充值请按 1，移除购买商品请按 2,退出请按0：')                    #余额不足结束循
#         n=int(input('>>>'))
#         if n==1:                                          #判断是否充值或移除商品
#             m=int(input('>>>请输入你要充值的金额：'))
#             a=a+m
#             print('你的余额还剩{}'.format(a))
#         elif n==2:
#             print('你的购物车如下：')
#             print(d)
#             t=int(input('请输入你要移除的商品编号：'))
#             d.pop(t-1)
#             print('你的购物车如下：')
#             print(d)
#         elif n==0:
#             break
