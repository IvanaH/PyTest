#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018/9/21

@author:Ivana
'''

import time,random,_thread
from time import sleep

count = 0

def threadTest():
    global count
    
    for i in range(1000):
        count = count+1
    
for i in range(10):  #create ten subthread in mainthread to call threadtest
    _thread.start_new_thread(threadTest,())

sleep(3)
print(count) #the output should not be 1000*10'
'''
Why is the result is 10000??
'''
