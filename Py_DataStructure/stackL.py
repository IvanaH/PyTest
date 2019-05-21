#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/5/21

@author:Ivana
'''

def canculation (n1,n2,op):
    r = -1
    if op == '+':
        r = n1 + n2
    elif op == '-':
        r = n1 - n2        
    elif op == '*':
        r = n1 * n2  
    r = n1 / n2
    return r

def canculate(equation):
    stackNum = []
    stackOperator = []
    
    for i in range (0,len(equation)):
        if equation[i] == '*' or equation[i] == '/':
            stackOperator.append(equation[i])
            stackNum.append(equation[i+1])
        elif equation[i] == '+' or equation[i] == '-':
            if stackOperator[-1]== '*' or stackOperator[-1] == '/':
                k = int(stackNum.pop())
            stackOperator.append(equation[i])
            stackNum.append(equation[i+1])
        
            