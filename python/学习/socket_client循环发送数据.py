#!/usr/bin/env python
#_*_coding:UTF-8_*_
'''编写socket客户端'''

import socket
#声明协议（实例）类型，实例化阶段
client = socket.socket() #默认值：socket.socket(self,family=AF_INET,type=SOCK_STREAM,proto=0,fileno=None)
#family=AF_INET代表地址簇含义是IPV4，type=SOCK_STREAM代表协议类型为tcp，后面的两个参数很少用

#创建连接
client.connect(('192.168.2.119',6969)) #localhost为主机地址，如果是其它设备则填写IP地址，6969为端口号
while True:
    msg = input(">>:").strip()
    if len(msg):continue
    #发送数据
    #client.send(b"Hello World")#python3的新定义，只能传输比特流，不能传输字符串等数据
    client.send(msg.encode("UTF-8"))#如果要发送中文需要先将数据encode才可以
    #接收返回数据
    data = client.recv(1024)#定义接收数据的大小，单位：字节，这个例子表示只接受1024的字节数的数据
    print("Recv:",data.decode())#打印接收到的数据，如果是中文则需要.decode()
client.close()#关闭连接































































































































