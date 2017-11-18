#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017/10/19

@author:Ivana
'''
# Echo client program

import socket,time

HOST = '10.1.80.209'
PORT = 43502

a = (HOST,PORT)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(a)

s.sendall("Hello World")

data = s.recv(1024)

s.close()

print"Recieve msg:",data