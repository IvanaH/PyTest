#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/6/17
@author:Ivana
'''

def bubbleS(list):
    if len(list) == 0:
        print("No elements need to sort.")
        return null

    for j in range(len(list)):
        flag = False  # if no exchange occurs, then the list is in order
        for i in range(len(list)-j-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                flag = True
            else:
                continue
        if flag is False:
            break

    return list

def insertionS(list):
    if len(list) == 0:
        print("No elements need to sort.")
        return null
            
    for i in range(len(list)):
        temp = list[i]
        for j in range(i,0,-1):
            if list[j] > temp:
                list[j+1] = list[j]
            else:
                list[j] = temp
                break
    return list   
        
def selectionS(list):
    if len(list) == 0:
        print("No elements need to sort.")
        return null
    
    for i in range(len(list)):
        temp = list[i]
        min = i
        for j in  range(i,len(list)):
            if list[min] > list[j]:
                min = j
        list[i] = list[min]
        list[min] = temp
    return list
        
def a():
    def a1():
        i = 1
    def a2():
        nonlocal i
        i = 2
    def a3():
        global i
        i = 3
    
#     i = 4
    a1()
    print(i)
    a2()
    print(i)
    a3()
    print(i)

if __name__ == '__main__':
#     list1 = [5,7,1,3,4,2,4,6,2,1]
#     list2 = ['a','d','w','g','d','p','l','e','o','m']
#     print(bubbleS(list1))
#     print(bubbleS(list2))
#     print(insertionS(list1))
#     print(selectionS(list1))
      a()
      print(i)
    