#!/use/bin/python
#-*- coding:utf-8 -*-

#同时整除2和3；整除2；整除3
# a=int(input('请输入数字:'))
# if a%2==0:
#     if a%3==0:
#         print('hello world')
#     elif a%2==0:
#      print('hello')
# elif a%3==0:
#     print('world')
# else:
#     print(666)
#以a或A开头以c结尾；以a开头；以c结尾
# a=input('请输入数据:')
# b=a[0]
# c=a[-1]
# if b=='a' and c=='c' or b=='A' and c=='c':
#      print(110)
# elif b=='a':
#     print(120)
# elif c=='c':
#     print(130)
# else:
#     print(250)

#猜数字
# import  random
# a = random.randrange(1,10)
# print(a)
# for i in range(100):
#     b=int(input('请输入数字:'))
#     if b > a :
#         print('大''还有{}次机会'.format(3-i))
#     elif b< a :
#         print('小''还有{}次机会'.format(3-i))
#     elif b == a :
#         print('正确')
#         break
# 99乘法表
# for a in range(1,10):
#     for b in range(1,a+1):
#         print('{}*{}={}'.format(b,a,a*b),end='\t')
#     print()

#将大于55的加入到一个列表，小与等于的的加入到另一个列表
# a=[99,44,66,77,33,22,11,88,55]
# b = list()
# c = list()
# for i in a:
#     if i > 55:
#         b.append(i)
#     else:
#         c.append(i)
# # print(b,c)

# 质数之和
# def zhishu(a):
#     b=0
#     for i in range(2,a+1):
#         for j in range(2,i+1):
#             if i%j==0:
#                 break
#         if i==j:
#             print(i)
#             b=b+i
#     print(b)
# zhishu(100)

# 水仙花数
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             d=a*100+b*10+c
#             e=a**3+b**3+c**3
#             if d==e:
#                 print(d)

#因数
# def yinshu(a):
#     c=0
#     for i in range(1,a+1):
#         b = 0
#         for j in range(1,i):
#             if i%j==0:
#                 b=b+j
#         if b==i:
#             print(i)
#             c=c+i
#     print(c)


#阶乘之和
# def jiecheng(a):
#     b=1
#     c=0
#     for i in range(1,a+1):
#         b=b*i
#         c=c+b
#     print(c)
# jiecheng(5)

#判断三角形钝角锐角直角
# a=int(input('>>'))
# b=int(input('>>'))
# c=int(input('>>'))
# if c>a and c>b and a+b>c and a+c>b and b+c>a:
#         if a**2+b**2==c**2:
#             print('直角')
#         if a**2+b**2>c**2:
#             print('锐角')
#         if a**2+b**2<c**2:
#             print('钝角')
# elif a+b>c and a+c>b and b+c>a:
#     print('C不是最大值')
# else:
#     print('不是三角形')


#输入一组数，大于平均数打印出来
# c=[]
# while True:
#       a=input('请输入数字:')
#       b=a.split(',')
#       for i in b:
#           c.append(int(i))
#           avg=sum(c)/len(c)
#       print(avg)
#           # print(c)
#       for j in c:
#          if j>avg:
#            print(j)

#从键盘上输入若干个学生的成绩，统计出平均成绩并输出低于平均分的学生成绩，用输入负数结束输入
# while True:
#     a=[]
#     b=input('请输入数字:')
#     if '-' in b:
#         break
#     c=b.split(',')
#     for i in c:
#      a.append(int(i))
#     d=sum(a)/len(a)
#     print(d)
#     for j in a:
#      if j < d:
#       print(j)

#去重,并排序
# a=input('请输入数据:')
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# c=[]
# for i in b:
#     c.append(int(i))
# for x in range(1,len(c)):
#     for y in range(0,len(c)-1):
#         if c[y]>c[y+1]:
#             c[y],c[y+1]=c[y+1],c[y]
# print(c)

# 冒泡排序
# a=[]
# b=input('请输入数字:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(0,len(a)):
#    for y in range(0,len(a)-1):
#        if a[y] > a[y+1]:
#            a[y],a[y+1]=a[y+1],a[y]
# print(a)

#选择排序法
# a=[]
# b=input('请输入数据:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(0,len(a)):
#     for y in range(x+1,len(a)):
#         if a[x] > a[y] :
#             a[x],a[y]=a[y],a[x]
# print(a)

#冒泡函数
# def maopo(a):
#     global maopo
#     a=[]
#     b=input('请输入数字:')
#     c=b.split(',')
#     for i in c:
#         a.append(int(i))
#     for x in range(1,len(a)):
#        for y in range(0,len(a)-1):
#            if a[y] > a[y+1]:
#                a[y],a[y+1]=a[y+1],a[y]
#     print(a)


#打印列表中第一大和第二大的值
# a=[]
# b=input('请输入数字:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(1,len(a)):
#    for y in range(0,len(a)-1):
#        if a[y] > a[y+1]:
#            a[y],a[y+1]=a[y+1],a[y]
# print('最大值为{},第二大值为{}'.format(a[-1],a[-2]))

#a=[]
# b=input('请输入数字:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))

#买鸡
# for x in range(1,100):
#     for y in range(1,100):
#         for z in range(1,100):
#             if 2*x+1*y+0.5*z==100 and x+y+z==100:
#                 print(x,y,z)


#一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数
# def xx(a,b):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j]==b:
#                 print(a[i],a[j],b)
# xx((1,2,3,4),5)

#一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a=[1,3,4,5,6,7,8,9]
# b=int(input('请输入数字:'))
# a.append(b)
# a.sort()
# print(a)

#任意4个数字，组成不相同的三位数
# a=input('请输入数字:')
# b=a.split(',')
# c=[]
# d=[]
# for i in b:
#     c.append(int(i))
# for x in c:
#     for y in c:
#         for z in c:
#             if x != y and x != z and y != z:
#                 e=x*100+y*10+z*1
#                 d.append(int(e))
# print(len(d))

#不用int将字符串变成整数
# a=input('请输入数据:')
# a=a[::-1]
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b=b+j*10**i
# print(type(a))
# print(type(b))


#将列表中的元素向左挪一位
# a=[1,2,3,4,5,6]
# for i in range(1,len(a)):
#     a[i-1],a[i]=a[i],a[i-1]
# print(a)
#将列表中最大的放在最后一位，最小的放在第一位
# a=(input('请输入数据:'))
# b=a.split(',')
# c=[]
# for i in b:
#     c.append(int(i))
# c.sort()
# c[0],c[-1]=c[-1],c[0]
# print(c)

# #判断一串文字是否为回文
# a=input('请输入一个数字：')
# for i in range(len(a)//2):
#     if a[i]!=a[-i-1]:
#         print('不是回文！')
#         break
# else:
#     print('是回文')

#十进制转十六进制
# a=int(input('请输入一个数字：'))
# print('十进制数为：',a)
# print('转换为十六进制：',hex(a))
# print('转换为八进制：',oct(a))
# print('转换为二进制：',bin(a))

#统计文件中行数：
# j=[]
# a=open('a.txt','r',encoding='utf-8')
# b=a.readlines()
# print(len(b))
# for i in b:
#     d=i.startswith('#')
#     j.append(d)
# e=b.count('\n')
# c=j.count(True)
# print(c) #带星号的数量
# print(e)
# w=len(b)-e-c
# print('除去空格和注释还剩：')
# print(w)

#统计文件中行数：
# with open('a.txt','r',encoding='utf-8') as f:
#     b=f.readlines()
#     c=len(b)
#     print(c)
#     for i in b:
#         if i.startswith('#') or i == '\n':
#             c=c-1
# print(c)

#阶乘之和
# a,b=0,1
# c=int(input('请输入一个数字：'))
# for i in range(1,c):
#     b=b*i
#     a=a+b
# print(a)

#10转16:
# m=[]
# b = int(input('请输入一个十进制数'))
# a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# while True:
#     if b<16:
#         m.append(a[b])
#         break
#     elif b>=16:
#         c=b%16
#         b=b//16
#         m.append(a[c])
# m=m[::-1]
# print(''.join(m))

# class 小爱同学():
#     def __init__(self,a):
#         self.name=a
#     def  a (self):
#         print('发消息给{}'.format(self.name))
#     def  __b  (self):
#         print('打电话给{}'.format(self.name))
#     def  c  (self):
#         self.__b()
# 小爱同学('小张').c()

# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('一周计划')
# for i in range(0,9):
#     for j in range(0,i+1):
#         sheet.write(i,j,'{}X{}={}'.format(i+1,j+1,(i+1)*(j+1)))
# f.save('b.xls')

#文档写表格：
# f=open('a.txt','r',encoding='utf-8')
# f=f.read()
# d=f.split('\n')
# z=len(d)
# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('一周计划')
# for b in range(z):
#     m=d[b]
#     m=m.split(',')
#     x=len(m)
#     for n in range(x):
#         sheet.write(b,n,'{}'.format(m[n]))
# f.save('a.xls')
#
#表格写文档：
# import  xlrd
# f=xlrd.open_workbook('b.xls')
# sheet=f.sheet_by_name('一周计划')
# hang=sheet.nrows
# xie = open('b.txt', 'w', encoding='utf-8')
# for i in range(hang):
#     z=sheet.row_values(i)
#     lie=len(z)
#     for j in range(lie):
#         b=sheet.cell(i,j).value
#         xie.write(b+' ')
#     xie.write('\n')
#
#统计文档中带有abc的行：
# a=open('a.txt','r',encoding='utf-8')
# while True:
#     b=a.readline()
#     if 'abc' not in b:
#         continue
#     else:
#         print(b)
#     if b=='':
#         break

#表格的追加
# from xlutils.copy import copy
# import  xlrd
# f = xlrd.open_workbook('a.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(3,1,'23')
# new_f.save('a.xls')


# import time
# a=time.localtime(1234543)
# print(a)
# b=time.strftime('%Y-%m-%d  %H:%M:%S',a)
# print(b)
#
# a=input('请输入一个时间,并以-为分割符：')
# b=time.strptime(a,'%Y-%m-%d')
# print(b)
# nian=b[0]
# if nian%400==0:
#     print('这一年是世纪年')
# elif nian%4==0:
#     print('这一年是闰年')
# else:
#     print('这一年不是闰年')
# print('今天是周{}'.format(b[6]+1))
# print('今天是今年的第{}天'.format(b[7]))


# m=[]
# a=input('请输入一个时间,并以-为分割符：')
# b=time.strptime(a,'%Y-%m-%d')
# for i in b:
#     m.append(i)
# m=tuple(m)
# # print(m)
# chuo=time.mktime(m)
# # print(chu)
# chuo=chuo-86400
# # print(chu)
# z=time.localtime(chuo)
# print(z)
# n=time.strftime('%Y-%m-%d',z)
# print(n)









#https://www.qiushibaike.com/text/page/3/

# import requests
# import re
# import xlwt
# mm=[]
# mz=[]
# # class Qiushi():
# for s in range(1,6):
#     wz='https://www.qiushibaike.com/text/page/{}/'.format(s)
#     #发送请求
#     zhidian={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#         #简单的反扒代码，更改你的发送的请求头数据
#
#    }
#     fq=requests.get(wz,headers=zhidian)
#     # 接收响应  1.text   网页源代码以文档的形式显示(字符串)  2.content 以字节的方式接收
#     wy=fq.content.decode('utf-8')
#     # print(wy)
#     #2,过滤想要的内容：
#     pp=re.compile('<h2(.*?)</h2>',re.S)
#     cc=pp.findall(wy)   #条件.findall(文件)
#     for k in cc:
#         mz.append(k)
#     p=re.compile('<div class="content">(.*?)/span',re.S)
#     c=p.findall(wy)
#     # print(c)
#     for i in c:
#         i=i.replace('<span>','')
#         i=i.replace('<br/>','')
#         i=i.replace('<','')
#         mm.append(i)
#     with open ('c.txt','w',encoding='utf-8') as shuj:
#         for j in mm:
#             xb=mm.index(j)
#             zhuzhe=mz[xb]
#             shuj.write(mz[xb])
#             shuj.write(j+'\n')
# print(len(mm))
# f=xlwt.Workbook()
# sheet=f.add_sheet('爬虫')
# for l in range(len(mm)):
#
#     sheet.write(2*l,0,mz[l])
#     sheet.write(2*l+1, 0, mm[l])
#     f.save('a.xls')


# 糗事百科图片：
# import requests
# import re
# class Tupian(object):
#     def fq(self,ys):
#         wz='https://www.qiushibaike.com/imgrank/page/{}/'.format(ys)
#         zhidian = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#                 }
#
#         fs=requests.get(wz,headers=zhidian)
#         wy=fs.content.decode('utf-8')
#         return wy
#     def guolv(self,abc):
#         lianjie=[]
#         patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         items=patt.findall(abc)
#         # print(items)
#         for i in items:
#             # print(i)
#             patt_a=re.compile(r'<img datas="(.*?)" alt',re.S)
#             items_a=patt_a.findall(i)
#             lianjie.append(items_a[0])
#         # print(len(lianjie))
#         return lianjie
#     def baocun(self,bc):
#         #图片保存
#         for a,j in enumerate(bc):
#             res =requests.get('https:'+j)
#             #接受的相应结果只能用content
#             qq=res.content
#             f=open('wenjian\{}.jpg'.format(a),'wb')
#             f.write(qq)
#
# tu=Tupian()
# ab=tu.fq(1)
# cun=tu.guolv(ab)
# tu.baocun(cun)


# import paramiko
#
# ssh123 = paramiko.Transport(('192.168.2.201',22))
# ssh123.connect(username='root',
#                    password='123456')
# sftp =paramiko.SFTPClient.from_transport(ssh123)
# # 要下摘得文件  存储的本地位置(重linux下载到本地)
# sftp.get('anaconda-ks.cfg','aaa.cfg')
# ssh123.close()
# 从w上传到linux
# sftp.put('','')
# ssh123.close()



# def abc(a,b,c):
#     aa=list(a)
#     bb=int(b)
#     cc=int(c)
#     # print(aa[bb:cc+bb])
#     # print(len(aa))
#     if cc>len(aa)-(bb+1):
#         aaa=aa[bb+1::]
#         for i in aaa:
#             aa.remove(i)
#         print(aa)
#     else:
#         for j in aa[bb+1:cc+bb+1]:
#             aa.remove(j)
#         print(aa)
#
# abc('abcdefg',4,1)

# import os
# os.mkdir('aaa')
# f=open(r'aaa\a.txt','w',encoding='utf-8')
# while True:
#     i=input('请输入数据：')
#     if i != 'exit':
#         f.write(i+'\n')
#     else:
#         f.close()
#         break
# du=open(r'aaa\a.txt','r',encoding='utf-8')
# print(du.read())
# du.close()
# os.remove('aaa/a.txt')
# os.rmdir('aaa')








#unittest:python自带单元测试的框架
# 使用unittest中unittest.TestCase这个类
# 自动化测试用例进行管理
# 所有的测试用例函数必须以test开头

# import unittest
# import requests
# from 学习 import HTMLTestRunner
#
#
# class xuex(unittest.TestCase):
#     def dizi(self,a):
#         url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
#         querystring = {"filterInput":"{}".format(a)}
#         headers = {
#                 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#                 'Accept-Encoding': "gzip, deflate",
#                 'Accept-Language': "zh-CN,zh;q=0.9",
#                 'Cache-Control': "max-age=0",
#                 'Connection': "keep-alive",
#                 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#                 'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
#                 'Content-Type': "application/x-www-form-urlencoded",
#                 'cache-control': "no-cache",
#                 'Postman-Token': "285aebd5-1382-4f9c-b6e8-5fa8ea84704d"
#                 }
#         response = requests.request("GET", url, headers=headers, params=querystring)
#         aaa=response.json()
#         return aaa
#     def setUp(self): #  初始化测试环境
#         print('查询开始')
#     def tearDown(self): #清理测试环境
#         print('查询结束')
#     def test_1(self):
#         bbb=self.dizi('北京')
#         # print(bbb)
#         self.assertEqual(bbb['code'],0)
#         print('__login__')
#     def test_2(self):
#         ccc=self.dizi('???')
#         # print(ccc)
#         self.assertNotEqual(ccc['code'],0)
#         print('__faill__')
# if  __name__=='__main__':
# # unittest.main()
#     # 创建一个测试套件
#     suit=unittest.TestSuite()
#     # 将测试用例添加到测试套件
#     # suit.addTest(Denglu('test_1'))
#     # suit.addTest(Denglu('test_2'))
#     # 将Denglu类中所有的以test开头的函数都添加到测试套件里
#     suit.addTest(unittest.makeSuite(xuex))
#     ff = open('abd.html','wb')        # 打开一个空文件
#     runner = HTMLTestRunner.HTMLTestRunner(stream=ff, title='接口测试报告', tester='朱家豪', description='结果如下')     #定义测试报告的信息
#     #执行测试套件
#     runner.run(suit)
#     ff.close()



# import requests
# import unittest
# import xlrd
# from 学习 import HTMLTestRunner
# f = xlrd.open_workbook(r'C:\Users\zhujh\PycharmProjects\untitled1\a.xls')
# sheet = f.sheets()[0]
# row_1 = sheet.nrows
# class Denglu(unittest.TestCase):
#     def dizi(self,username,password):
#         url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
#         payload = '{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}' %(username,password)
#         headers = {
#                 'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#                 'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#                 'Language': "zh_CN",
#                 'APIVersion': "3.0",
#                 'Content-Type': "application/json",
#                 'cache-control': "no-cache",
#                 'Postman-Token': "c3e8a8e4-d355-49b2-93b8-b4f814eb148a"
#                 }
#
#         response = requests.request("POST", url, data=payload, headers=headers)
#
#         zhuye=response.json()
#         # print(zhuye)
#         return zhuye
#     def setUp(self): #  初始化测试环境
#         print('测试开始')
#     def tearDown(self): #清理测试环境
#         print('测试结束')
#     def test_1(self):    #有效
#         bbb=self.dizi(int(sheet.cell(1, 0).value),int(sheet.cell(1, 1).value))
#         self.assertEqual(bbb['code'],0)
#         print('__login successfully__')
#     def test_2(self):  #无效
#         for i in range(2,row_1):
#             ccc=self.dizi(int(sheet.cell(i, 0).value),int(sheet.cell(i, 1).value))
#             self.assertNotEqual(ccc['code'],0)
#             print('__This is an incorrect input__')
# if  __name__=='__main__':
#     # unittest.main()
#     # 创建一个测试套件
#     suit=unittest.TestSuite()
#     # 1、将测试用例添加到测试套件
#     #     suit.addTest(Denglu('test_1'))
#     #     suit.addTest(Denglu('test_2'))
#     # 2、将Denglu类中所有的以test开头的函数都添加到测试套件里
#          suit.addTest(unittest.makeSuite(Denglu))
#
#     ff = open('abc.html','wb')        # 打开一个空文件
#     runner = HTMLTestRunner.HTMLTestRunner(stream=ff,title='接口测试报告',tester='朱家豪',description='结果如下')     #定义测试报告的信息
#     #执行测试套件
#     runner.run(suit)
#     ff.close()




















# a=[1,[[2],3,3,4,2],5]
# cc=[]
# for i in a:
#     if type(i)==list:
#         for j in i:
#             if type(j) == list:
#                 for m in j:
#                     # print(m)
#                     cc.append(m)
#             else:
#                 # print(j)
#                cc.append(j)
#     else:
#         # print(i)
 # print(cc)
from time import sleep
import unittest
from appium import webdriver
class ce(unittest.TestCase):
    a = {
                  "platformName": "Android",
                  "platformVersion": "5.1.1",
                  "deviceName": "emulator-5554",
                  "appPackage": "com.qk.butterfly",
                  "appActivity": ".main.LauncherActivity"
            }
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.a)
    def join(self,name,password):
        sleep(10)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(10)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
        sleep(10.0)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        sleep(5.0)
        print('准备登陆')
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(10.0)
    def test_1(self):
        self.join('15103819460','13137246872zls')
        sleep(10.0)
        print('开始断言')
        text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
        self.assertEqual(text,'热门')
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
if __name__ == '__main__':
    unittest.main()