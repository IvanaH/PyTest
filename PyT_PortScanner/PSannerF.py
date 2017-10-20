#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017/10/16

@author:Ivana
'''

import socket, sys, time

def scan_port(ip,port):
#   To verify whether the port is open   
    try:
        if port >= 65535:
            print "Scan is over."
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))

        if result==0:
            print"Port ",port," is open."
        s.close()
    except:
        print "Unexcepted error: ",sys.exc_info()[0]    
        

def scan_ports(ip,ports):
    for port in ports:
        scan_port(ip, port)
        

def scan_IP(ip):
#   Scan the given ip to verify whether the port is open
    try:
        print ('Scanning Start:%s' %(ip))
        start_time = time.time()
        for port in range(0,65534):
            scan_port(ip, port)
        print u'Total time ：%.2f' %(time.time()-start_time)
        raw_input("Press Enter to Exit")        
    except:
        print "Something wrong when scan the ip:", ip
        print "The error msg: ", sys.exc_info()[0] 
    
 
        
if __name__=='__main__':
    scan_port('10.1.10.30', 8090)
    scan_ports('10.1.10.30', [8090,8080])