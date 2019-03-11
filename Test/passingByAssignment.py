#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/03/06

@author:Ivana
'''
def try_to_change_string1(arg):
    print("got " + arg)
    arg = 'this is a new string'
    print("set " + arg)
    
def try_to_change_string2(arg):
    print("got " + arg)
    arg = 'this is a new string'
    print("set " + arg)
    return arg

arg = "this is original string"

print("before set is: " + arg+'\n')
try_to_change_string1(arg)
print("after set is: "+arg+'\n')
arg = try_to_change_string2(arg)          # rebind arg
print("after set is: "+arg+'\n')

def try_to_change_list1(list_arg):
    print("got " + str(list_arg))
    list_arg = [1,2,3,4]                  # rebind list_arg
    print("set " + str(list_arg))   
    
def try_to_change_list2(list_arg):
    print("got " + str(list_arg))
    list_arg.append('e')
    print("set " + str(list_arg))

list_arg = ['a','b','c','d']     

print("before set is: " + str(list_arg)+'\n')
try_to_change_list1(list_arg)
print("after change1 set is: "+str(list_arg)+'\n')
try_to_change_list2(list_arg)
print("after change2 set is: "+str(list_arg)+'\n')

if __name__ == '__main__':
    pass
    
    
