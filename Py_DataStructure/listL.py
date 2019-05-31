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
    
    
if __name__ == '__main__':
    list1 = [1,2,3,1,1,1,4]
    list2 = ['a','v','d','d','3','d','2','44','2sdf','d','3','d','d','d','d','d','d','d']
    majority(list2)