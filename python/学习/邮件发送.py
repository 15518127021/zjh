#!/use/bin/python
# -*- coding:utf-8 -*-

import smtplib
import email.mime.multipart
import email.mime.text
def Youjian():
    fr = '15518127021@163.com'    #发件人
    res='963891267@qq.com'      # 收件人
    server = 'smtp.163.com'     # 服务器
    passwd ='zjh520000'    # 授权码
    # 创建一个空邮件
    mm =email.mime.multipart.MIMEMultipart()
    mm['From']= fr   #添加一个发件人
    mm['To']=res      # 添加一个收件人
    mm['Subject']='日报'   # 添加一个主题
    nr='朱家豪你好!我是你'   # 正文
    # 处理正文文本
    txt=email.mime.text.MIMEText(nr)
    mm.attach(txt)
    # 添加附件
    att2 = email.mime.text.MIMEText(open(r'C:\Users\zhujh\PycharmProjects\untitled1\Src\report\diesheng.html', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="diesheng.html"'
    ## 头部字段
    mm.attach(att2)
    # 定义一个服务器
    smtp1=smtplib.SMTP_SSL(server,465)
    # 登录服务器
    smtp1.login(fr,passwd)
    # 发送邮件
    smtp1.sendmail(fr,res,mm.as_string())