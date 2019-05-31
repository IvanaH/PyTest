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
    else:
        r = n1 / n2
    return int(r)

def canculate(equation):
    stackNum = []
    stackOperator = []
    loc = -1
    
    for i in range (0,len(equation)):
        if loc >= i:
            continue
        elif equation[i] == '*' or equation[i] == '/':
            k = float(stackNum.pop())
            r = canculation(k, float(equation[i+1]), equation[i])
            stackNum.append(r)
            loc  = i + 1
            continue
        elif equation[i] == '+' or equation[i] == '-':
            stackOperator.append(equation[i])
            continue            
        else:
            stackNum.append(equation[i])
    print(stackNum)
    print(stackOperator)
    
    for i in range(0,len(stackOperator)):
        j = float(stackNum.pop())
        k = float(stackNum.pop())
        r = canculation(k, j, stackOperator.pop())
        stackNum.append(r)
    print(stackNum.pop())

def doMated(str):
    leftBracket = []
#     rightBracket = []
    flag = True
    
    for i in str:
        if i == "(" or i == '[' or i == '{':
            leftBracket.append(i)
            continue
        elif i == ")" or i == ']' or i == '}':
            if len(leftBracket) == 0:
                print("Unmated")
                flag = False
                break
            else:
                j = leftBracket.pop()
                if i == "(" and j == ")":
                    continue
                elif i == "[" and j == "]":
                    continue
                elif i == "{" and j == "}":
                    continue
                else:
                    print("Unmated.")
                    break                    
                     
    if flag == True and len(leftBracket) == 0:
        print("Mated.")
    elif flag == False and len(leftBracket) > 0: 
        print("Unmated.")
    
    
if __name__ == '__main__':
#     eq = '5+6*4/3-8/2'
#     canculate(eq)
    str1 = '{([{}])}'
    str2 = '{[]}()'
    str3 = '{[{})]}'
    str4 = '{[{]}'
    str5 = '{([]))'

    doMated(str1)
#     doMated(str2)
#     doMated(str3)
#     doMated(str4)
#     doMated(str5)

        
            