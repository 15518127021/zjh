#!/use/bin/python
# -*- coding:utf-8 -*-
import paramiko
#创建一个远程客户端
ssh123 =paramiko.SSHClient()
#跳过验证，
ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接主机
ssh123.connect(hostname='192.168.2.201',
               port=22,
               username='root',
               password='123456')
while True:
    resultful_order=input('>>>')

    if resultful_order == 'exit':
        break
    try:
        a,b,c=ssh123.exec_command('{}'.format(resultful_order))
        print(b.read().decode())
    # a  执行的命令
    # b  执行的结果
    # c  执行的报错
    # print(b.read().decode())

        # ssh123.close()
    except:
        print('There is an error in the syntax of the statement you entered')
        continue
