#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017/10/19

@author:Ivana
'''

import socket

s=socket.socket()

a=('127.0.0.1',8000)

s.connect(a)

msg = 'Hello'
s.sendall(msg)

print s.recv(1024)

s.close()