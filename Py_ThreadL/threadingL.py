#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018/9/21

@author:Ivana
'''

import threading,time,random
from time import sleep

# def thread_fun(num):
#     for n in range(0,int(num)):
#         print ("I come from %s, num:%s" %(threading.current_thread().getName(),n))
# def testThread(thread_num):
#     thread_list = list()
#     # create thread
#     for i in range(0,thread_num):
#         thread_name="thread_%s"%i
#         thread_list.append(threading.Thread(target=thread_fun,name=thread_name,args=(20,)))
#     #start all threads
#     for thread in thread_list:
#         thread.start()
#     #wait for all threads stop
#     for thread in thread_list:
#         thread.join()
#         
# if __name__ == "__main__":
#     testThread(3)

                                                

# class myThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     
#     def run(self):
#         print("I am %s" %self.name)
# 
# if __name__ == "__main__":
#     for thread in range(0,5):
#         t = myThread()
#         t.start()



counter = 0

class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        global counter
        time.sleep(1)
        counter+=1
        print("I am %s, set counter: %s" %(self.name,counter))
        
if __name__ == "__main__":
    for i in range(0,50):
        my_thread = myThread()
        my_thread.start()
    time.sleep(10)
    print(counter)
    