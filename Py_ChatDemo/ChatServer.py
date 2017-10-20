#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017/10/19

@author:Ivana
'''

import socket,time;

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

a=('127.0.0.1',8000)

s.bind(a)

s.listen(1)

while 1:
    conn,addr=s.accept()
    print time.time()
    print '['+addr[0]+':'+str(addr[1])+'] send a message to me:' + conn.rev(1024)
    conn.sendall('I received a message from [' + addr[0]+str(addr[1])+']')
s.close()