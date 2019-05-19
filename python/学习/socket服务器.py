#!/use/bin/python
# -*- coding:utf-8 -*-


# import socket
# # 创建一个有接受能力和发送能力的对象 （套接字）
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #默认使用tcp(SOCK_STREAM) udp(SOCK_DGRAM)
#                     #ipv4 ，ipv6(AF_INET)
# #绑定ip地址和端口
# s.bind(('192.168.2.117',523))
# #监听服务有没有开启
# s.listen(3) #最大等待个数
# while True:
#     # aa=input('>>>')
#     client,addr=s.accept()    #接受请求建立连接
#     #第一个变量:建立连接的信息
#     #第二个变量：客户端的IP地址和端口号
#
#     msg=client.recv(1024)  #接收客户端发送的请求,每次接收的最大1024个字节
#     print(msg.decode('utf-8'))
#     reg='{}'.format(input('>>>'))
#     # aa = input('>>>')
#     client.send(reg.encode('utf-8'))





import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #默认使用tcp(SOCK_STREAM) udp(SOCK_DGRAM)
                    #ipv4 ，ipv6(AF_INET)
#绑定ip地址和端口
s.bind(('192.168.2.117',523))
#监听服务有没有开启
# s.listen(3) #最大等待个数
while True:
   client,addr=s.recvfrom(1024)
   print(client.decode('utf-8'))
   msg='hello'
   s.sendto(msg.encode('utf-8'),addr)












