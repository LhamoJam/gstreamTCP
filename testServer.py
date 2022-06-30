# -*- coding:utf-8 -*-
import socket
import time
import cv2
import numpy as np
# 创建socket
tcp_server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# 本地信息  本机IP
address = ('127.0.0.1', 8088)
# 绑定
tcp_server_socket.bind(address)
# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
# listen里的数字表征同一时刻能连接客户端的程度.
tcp_server_socket.listen(128)
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
# clientAddr 是元组（ip，端口）
client_socket, clientAddr = tcp_server_socket.accept()

recv_data_whole = bytes()

while 1:
    # 接收对方发送过来的数据，和udp不同返回的只有数据
    recv_data = client_socket.recv(6220800)  # 接收n个字节

    if len(recv_data) == 0 :
        # 关闭socket
        client_socket.close()
        tcp_server_socket.close()
        print('客户端已断开连接,服务结束')
        break
        # client_socket, clientAddr = tcp_server_socket.accept() # 也可以等待重连
    else:
        recv_data_whole += recv_data
        # print('接收到的数据长度为:', recv_data_whole.__len__())

        if recv_data_whole.__len__() == 6220800 : # 720p RGB单张图像大小
            # 字节数据转回图片
            frame = np.frombuffer(recv_data_whole, dtype=np.uint8).reshape([1080,1920,3])
            recv_data_whole = bytes()
            cv2.imshow('camera_recevied',frame)
            cv2.waitKey(1)
            # 回传信息，很重要，具有同步功能
            client_socket.send("image has been received!".encode('gbk'))
