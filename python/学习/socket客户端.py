#!/use/bin/python
# -*- coding:utf-8 -*-

# import socket
# #创建一个套接字
# # ss =socket.socket()
# # 客户端不需要绑定IP和端口号，只需要建立连接
# # ss.connect(('127.0.0.1',523))
# # # 发送请求
# while True:
#     ss = socket.socket()
#
#     ss.connect(('192.168.2.117', 523))
#
#     aa=input('>>>')
#     msg='{}'.format(aa)
#     ss.send(msg.encode('utf-8'))
#     reg =ss.recv(1024)
#     print(reg.decode('utf-8'))
#     # 断开连接
#     # ss.close()



import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=('192.168.2.117',523)
msg='sweytuk'
s.sendto(msg.encode('utf-8'),host)
reg =s.recv(1024)
print(reg.decode('utf-8'))
