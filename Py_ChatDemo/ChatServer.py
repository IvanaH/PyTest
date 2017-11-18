#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017/10/19

@author:Ivana
'''

# ECHO Server program
import  socket,time

HOST = '10.1.80.209'
PORT = 43502

a = (HOST,PORT)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(a)

s.listen(1)

conn,addr=s.accept()

print "Connect by" ,addr

while 1:
#     conn.send("ECHO:")
    data = conn.recv(512)
    if not data:
        break
    conn.sendall("ECHO:"+data) 

conn.close()
