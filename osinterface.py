# import os
# # os.getcwd()
# dir(os)
# # help(os)

# import math
# import random
# print (random.random())
import socket
import sys

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('hello world')
host = socket.gethostname()
port = 59999

serversocket.bind((host,port))
serversocket.listen(5)
while True:
    clientsocket,addr = serversocket.accept()
    print("连接地址: %s" % str(addr))

    msg = '欢迎访问W3Cschool教程！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()