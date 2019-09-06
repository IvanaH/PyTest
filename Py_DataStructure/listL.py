#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/5/22

@author:Ivana
'''

def majority(list):
    count = {}
    half = len(list)/2
     
    for i in range(len(list)):
        if list[i] not in count.keys():
            count[list[i]] = 1
        else:
            num = count[list[i]] + 1
            if num > half:
                result = list[i]
                break
            else:
                count[list[i]] = num
    print("The majority element is %s" %(str(result)))
   

def nameSpace():
    def a1():
        i = 1
        
    def a2():
        nonlocal i
        i = 2
    
    def a3():
        global i
        i = 3
    i = 0
    
    a1()
    print("after a1(): " + str(i))
    a2() 
    print("after a2(): " + str(i))
    a3()
    print("after a3(): " + str(i))  
 
    
if __name__ == '__main__':
#     nameSpace()    
#     print("after nameSpace(): " + str(i)) 

    list1 = [1,2,3,1,1,1,4]
    list2 = ['a','v','d','d','3','d','2','44','2sdf','d','3','d','d','d','d','d','d','d']
    majority(list2)

