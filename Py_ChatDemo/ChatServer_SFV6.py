#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017/11/18

@author:Ivana
'''

# ECHO Server program

import socket,sys

HOST=None          #Sy,bolic name meaning all avaliable interfaces
PORT=50007           #Arbitrary non-privileged port 
s=None

for res in socket.getaddrinfo(HOST, PORT,socket.AF_UNSPEC,socket.SOCK_STREAM,0,socket.AI_PASSIVE):
    af,socktype,proto,canonname,sa=res
    try:
        s=socket.socket(af,socktype,proto)
    except socket.error as mgs:
        s=None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None 
        continue
    break
if s is None:
    print "Cloud not open socket"
    sys.exit(1)

coon,addr=s.accept()
print "Connected by: ",addr

while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()