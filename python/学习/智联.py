#!/use/bin/python
# -*- coding:utf-8 -*-

import requests
import re
import json
import xlrd
import xlwt
from xlutils.copy import copy
class Zlan(object):
    def equest_to_send(self,ab):
        wz='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize={}&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&=0&_v=0.56577906&x-zp-page-request-id=6c3624e824e64a59a50744578204c978-1554174454812-84580'.format(ab*90,ab*90)
        fanpa={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
                }
        send_l=requests.get(wz,headers=fanpa)
        html=send_l.content.decode('utf-8')
        return html
    def word_filter(self,abc):
        asd=json.loads(abc)
        nn=asd['data']['results']
        aaa,bbb,ccc,ddd,eee,fff=[],[],[],[],[],[] # 公司地址，薪资，公司地址，职位，学历，工作经验
        for i in range(len(nn)):
            gsname=asd['data']['results'][i]['company']['name']
            aaa.append(gsname)
            xizhi=asd['data']['results'][i]['salary']
            bbb.append(xizhi)
            gsdz=asd['data']['results'][i]['city']['display']
            ccc.append(gsdz)
            zw=asd['data']['results'][i]['jobName']
            ddd.append(zw)
            mmm=asd['data']['results'][i]['eduLevel']['name']
            eee.append(mmm)
            yaoqiu=asd['data']['results'][i]['workingExp']['name']
            fff.append(yaoqiu)
        # print(len(fff))
        return aaa,bbb,ccc,ddd,eee,fff
    def save_file(self,aa,bb,cc,dd,ee,ff):
        try:
            f=xlrd.open_workbook('智联.xls')
            sheetl = ff.sheets()[0]
            num = sheetl.nrows
            new_f=copy(f)
            sheet=new_f.get_sheet(0)
            for j, k in enumerate(aa):
                sheet.write(j + num, 0, k)
                sheet.write(j + num, 1,bb[j])
                sheet.write(j + num, 2, cc[j])
                sheet.write(j + num, 3, dd[j])
                sheet.write(j + num, 4, ee[j])
                sheet.write(j + num, 5, ff[j])
            new_f.save('智联.xls')
        except:
            f=xlwt.Workbook()
            sheet =f.add_sheet('智联招聘')
            sheet.write(0,0,'公司地址')
            sheet.write(0,1,'薪资')
            sheet.write(0,2,'公司地址')
            sheet.write(0,3,'职位')
            sheet.write(0,4,'学历')
            sheet.write(0,5,'工作经验')
            for j,k in enumerate(aa):
                sheet.write(j+1,0,k)
                sheet.write(j + 1, 1, bb[j])
                sheet.write(j + 1, 2, cc[j])
                sheet.write(j + 1, 3, dd[j])
                sheet.write(j + 1, 4, ee[j])
                sheet.write(j + 1, 5, ff[j])
            f.save('智联.xls')
for yy in range(1,4):
    a=Zlan()
    b=a.equest_to_send(yy)
    c,d,e,f,g,l=a.word_filter(b)
    a.save_file(c,d,e,f,g,l)