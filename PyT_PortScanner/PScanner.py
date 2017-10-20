#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017/10/03

@author:Ivana
'''

# import nmap
import socket, time, thread, sys
socket.setdefaulttimeout(3)

def socket_port(ip, port):
#     verify whether the port is open by the ip and port
    try:
        if port >= 65535:
            print u"The scan is over."
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        if result==0:
#             lock.acquire()
            print  ip,u':',port,u' is open.'
#             lock.release()

        s.close()
    except:
#         print u'Something wrong.'
        print "Unexcepted error: ",sys.exc_info()[0]
 
def ip_scan(ip):
#     scan port from 0 - 65534 with imported IP
 
#     try:
        print ('Scanning Start:%s' %(ip))
        start_time=time.time()
#         for i in range(0,65534):
        for i in range(8090,15534):
            print i;
            socket_port(ip,int(i))
#             thread.start_new_thread(socket_port,(ip,int(i)))
        print u'Total time ：%.2f' %(time.time()-start_time)
        raw_input("Press Enter to Exit")
#     except:
#         print u'Something wrong when scan IP'
#          
 
if __name__=='__main__':
#     url=raw_input('Input the ip you want to scan:\n')
#     lock=thread.allocate_lock()
#     socket_port('192.168.1.102',8090)
    socket_port('10.1.10.30', 8090)
#     ip_scan('192.168.1.102')
