#! usr/bin/env python
# -*- coding: utf-8 -*-
'''
create 2019/11/12
@author Ivana
'''
import copy
import re

def dictMerge():
    dict1 = {'a':11,'b':22}
    dict2 = {'b':22222,'c':33333}
    
#     dictMerge1 = dict(dict1.items()+dict2.items()) # TypeError occurred in python3
    dictMerge2 = dict(dict1,**dict2)
    dictMerge3 = dict.copy(dict2)
    dictMerge3.update(dict1)
    
#     print("dictMerge1 is:%s " % dictMerge1)
    print("dictMerge2 is:%s " % dictMerge2)
    print("dictMerge3 is:%s " % dictMerge3)    

def diffCopy():
    a = [1,2,[1,2]] 
    b = copy.deepcopy(a) # get a new object and clone of the original object and all of its children.
    c = copy.copy(a)  # get a new object, Not clone the children themselves 
    d = a  #get a variable which share the reference
    
    print("Original a is: %s" %a)
    print("Original b is: %s" % b)
    print("Original c is: %s" % c)
    print("Original d is: %s \n" % d)    
    
    a.append(3)
    a[2][1] = 3
    print("New a is: %s  " % a)
    print("New b is: %s" % b)
    print("New c is: %s" % c)
    print("New d is: %s" % d)

def compOper():
    a = b = [1,2,3]
    c = [1,2,3]
    print("a is b? :%s" %(a is b))
    print("a is c? :%s" %(a is c))
    
    m = 1
    n = 1
    print("m is n?: %s" %(m is n))
    
    x = 'String'
    y = 'String'
    print("x is y?: %s" %(x is y))

def reEx():
    pattern = 'foo'
    pa = re.compile('foo$')
    str1 = 'foobar'
#     print(re.match(pattern, str1).group(0))
#     print(pa.match(str1).group(0))  
    
    p21 = '(?=(1[356789]\d{9}))'
    p22 = re.compile('1[356789]\d{9}')
    str2 = 'aaa1315123443210'
    r = re.findall(p21,str2)
    print(r)
    print(p22.findall(str2))

if __name__ == '__main__':
    reEx()
