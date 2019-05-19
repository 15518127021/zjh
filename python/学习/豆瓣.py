#!/use/bin/python
# -*- coding:utf-8 -*-
#豆瓣电影图片：
# import requests
# import re
# class Douban(object):
#     def qingqoiu(self,ab):
#         wz='https://movie.douban.com/top250?start={}&filter='.format((ab-1)*25)
#         fanpa= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#                 }
#         fs=requests.get(wz,headers=fanpa)
#         html=fs.content.decode('utf-8')
#         # print(html)
#         return html
#     def Gl(self,abc):
#         yname,dy=[],[]
#         tj=re.compile('<img width="100"(.*?)<div class="info">',re.S)
#         wenj=tj.findall(abc)
#         for i in wenj:
#             tj_a=re.compile('alt="(.*?)"',re.S)
#             name=tj_a.findall(i)
#             tj_b=re.compile('datas="(.*?)"',re.S)
#             tp=tj_b.findall(i)
#             yname.append(name[0])
#             dy.append(tp[0])
#         # print(len(yname))
#         return yname,dy
#         # print(yname)
#         # print(dy)
#     def Bc(self,bc,bd):
#         for m,j in enumerate(bd):
#
#             res =requests.get(j)
#     # #             #接受的相应结果只能用content
#             qq=res.content
#             mm=bc[m]
#             f=open('dian\{}.jpg'.format(mm),'wb')
#             f.write(qq)
# for i in range(1,6):
#     a=Douban()
#     b=a.qingqoiu(i)
#     c,d=a.Gl(b)
#     a.Bc(c,d)

# 爬取豆瓣电影介绍
# import requests
# import re
# import xlwt
# import xlrd
# from xlutils.copy import copy
# class Douban_movie_introduction(object):
#     def equest_to_send(self,ab):
#         wz='https://movie.douban.com/top250?start={}&filter='.format((ab-1)*25)
#         fanpa={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#                 }
#         send_l=requests.get(wz,headers=fanpa)
#         html=send_l.content.decode('utf-8')
#         return html
#     def word_filter(self,abc):
#         aa,bb=[],[]
#         word_condition_l=re.compile('<img width="100" alt="(.*?)" datas="https:',re.S)
#         word_name=word_condition_l.findall(abc)   #电影名
#
#         word_condition=re.compile('导演:(.*?)&nbsp;&nbsp',re.S)
#         word_director=word_condition.findall(abc)   #导演
#
#         word_condition_2=re.compile('<span class="rating_num" property=(.*?)<p class="quote">',re.S)
#         word_score=word_condition_2.findall(abc)   #评分
#         # print(word_name)
#
#         for i in word_score:
#             word_condition_3=re.compile('"v:average">(.*?)</span>\n',re.S)
#             word_score_l=word_condition_3.findall(i) #评分
#             aa.append(word_score_l[0])
#             word_condition_4=re.compile('<span>(.*?)</span>\n',re.S)
#             word_score_2=word_condition_4.findall(i)    #评论人数
#             bb.append(word_score_2[0])
#         # print(bb)
#         return word_name,word_director,aa,bb
#     def save_file(self,c,d,e,f):
#         try:
#             dd=xlrd.open_workbook('douban.xls')
#             sheet_l=dd.sheets()[0]
#             hang=sheet_l.nrows
#             dd_l=copy(dd)
#             sheet=dd_l.get_sheet(0)
#             for j,name_l in enumerate(c):
#                 sheet.write(hang+j,0,name_l)
#                 sheet.write(hang+j,1,d[j])
#                 sheet.write(hang+j,2,e[j])
#                 sheet.write(hang+j,3,f[j])
#             dd_l.save('douban.xls')
#             # sheet.wrute()
#
#
#         except:
#             ff = xlwt.Workbook()
#             sheet = ff.add_sheet('电影介绍')
#             sheet.write(0,0,'电影名称')
#             sheet.write(0,1,'导演')
#             sheet.write(0,2,'豆瓣评分')
#             sheet.write(0,3,'评论人数')
#             for j,name_l in enumerate(c):
#                 sheet.write(j+1,0,name_l)
#                 sheet.write(j+1,1,d[j])
#                 sheet.write(j+1,2,e[j])
#                 sheet.write(j+1,3,f[j])
#             ff.save('douban.xls')
#
#
# for hh in range(1,6):
#
#     a=Douban_movie_introduction()
#     b=a.equest_to_send(hh)
#     c,d,e,f=a.word_filter(b)
#     a.save_file(c,d,e,f)
import xlrd
f = xlrd.open_workbook('a.xls')
# ccc=f.nsheets
# print(ccc)
sheet = f.sheets()[0]
row_1 = sheet.nrows
print(row_1)
for i in range(1,row_1):
    b = sheet.cell(i,0).value
    print(int(b))
