#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/09/16

@author:Ivana
'''

def getFileContent(addr):
    with open(addr) as f:
        fcontent = []
        lines = f.readlines()
        for line in lines:
            fcontent.append(line.split('\n')[0])
    return fcontent    


def toString(listC,joint,start=None,end=None):
    if start != None:
        rstr = start + str(listC[0])
    else:
        rstr = str(listC[0])
        
    for i in range(1,len(listC)):
        rstr = rstr + joint + str(listC[i]) 
    
    if end != None:
        rstr = rstr + end
    
    return rstr


if __name__ == '__main__':
    testList = [1,2,3]
#     print(toString(testList,joint="','"))
#     print(toString(testList,start="'",end="'",joint="','"))
#     print(getFileContent('toCSDemo.txt'))
    print(toString(getFileContent('toCSDemo.txt'),start="'",end="'",joint="','"))
    
