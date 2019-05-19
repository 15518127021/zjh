#!/usr/bin/env python
#_*_coding:UTF-8_*_
'''编写socket服务端'''

import socket
#创建一个server对象
server = socket.socket()
#定义监听的IP以及端口号，如果有多张网卡localhost的位置可以用IP地址代替
server.bind(("192.168.2.119",6969))

server.listen(5)#开始监听,最多同时连接5个客户端，经过测试，python3.4中参数必须填写，否则会报错
print("开始等电话了")

while True:
    #server.accept()会返回两个值,conn代表当前连接的实例，addr代表客户端的地址和端口
    conn,addr = server.accept()#启动监听等待，等待连接进来
    print("电话进来了")
    while True:
        data = conn.recv(1024)#定义接收数据的大小，单位：字节
        print(len(data))
        if not data:
            print("This host is lost...")
            break
        print("Recv:",data.decode())   #如果想打印接收到的中文就需要将数据decode()一下
        conn.send(data.upper())#将接收到的结果转换为大写并返回客户端
server.close()