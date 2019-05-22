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
        if count[list[i]] is null:
            count[list[i]] = 1
        else:
            num = count[list[i]] + 1
            if num > half:
                result = list[i]
                break
            else:
                count[list[i]] = num
    print(result)
    
if __name__ == '__main__':
    list = [1,2,3,1,1,1,4]
    dic = {1:2,3:4}
    print(dic[2])
#     majority(list)