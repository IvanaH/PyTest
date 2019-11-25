#! usr/bin/env python
# -*- coding: utf-8 -*-
'''
create 2019/10/31
@author Ivana
'''
import time
import threading

def draw_square(rest_s):
    print("Start to draw square.")
    time.sleep(rest_s)
    print("Has drew a square.\n")
    
def draw_circle(rest_s):
    print("Start to draw circle.")
    time.sleep(rest_s)
    print("Has drew a circle.\n")
    
def single_thread():
    draw_circle(5)
    draw_square(3)

def multi_threads():
    threadA = threading.Thread(target=draw_circle,args=(5,))
    threadB = threading.Thread(target=draw_square,args=(3,))
    threadA.start()
    threadB.start()
    threadA.join()  # without calling join(), the super_thread will end without waiting for the end of sub_thread
    '''
                    without threadA.join(), the output should be:
                    Has drew a square.
                    End thread: Fri Nov  1 19:24:20 2019
                    Has drew a circle.
                    '''
    threadB.join()
    
if __name__ == '__main__':
    print("Start thread: " + time.ctime())
#     single_thread()
    multi_threads()
    print("End thread: " + time.ctime())
    
    