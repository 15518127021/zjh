#!/use/bin/python
# -*- coding:utf-8 -*-
import pymysql  # 导入 pymysql

# 打开数据库连接
conn=pymysql.Connect(
    host='192.168.2.201',
    port=3306,
    user='root',
    passwd='123456')
cur = conn.cursor()
while True:
    a = input('>>>')
    if a == 'exit':
        break
    try:
        cur.execute('{}'.format(a))
        print(cur.fetchall())
    except:
        print('There is an error in the syntax of the statement you entered')
        continue