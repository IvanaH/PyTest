#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017/11/18

@author:Ivana
'''

# ECHO Client program

import socket,sys 

HOST ='daring.cwi.nl'  #the remote host 
PORT = 50007
s = None

for res in socket.getaddrinfo(HOST, PORT,socket.AF_UNSPEC,socket.SOCK_STREAM):
    af, socketype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socketype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print "Could not open socket"
    sys.exit(1)
    
s.sendall("Hello world")
data = s.recv(1024)
s.close()

print "Received: ", repr(data)