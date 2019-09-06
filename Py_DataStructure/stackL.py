#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/5/21

@author:Ivana
'''
from inspect import stack

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
                if j == "(" and i == ")":
                    continue
                elif j == "[" and i == "]":
                    continue
                elif j == "{" and i == "}":
                    continue
                else:
                    print("Unmated.")
                    break                    
                     
    if flag == True and len(leftBracket) == 0:
        print("Mated.")
    elif flag == False and len(leftBracket) > 0: 
        print("Unmated.")

def isPair(a, b, A, B):
    idx = A.index(a)
    return B[idx] == b

def isLeagal(str):
    stack = []
    A = [ '[' , '(' , '{']
    B = [ ']', ')', '}']
    
    for s in str:
        if s in A:
            stack.append(s)
        else:
            if len(stack) > 0:
                a = stack.pop()
                if isPair(a, s, A, B):
                    continue
                else:
                    return False
            else:
                return False
    if len(stack) > 0:
        return False
    return True

def printLegal(str):
    if isLeagal(str):
        print("matched")
    else:
        print("unmatched")
    
if __name__ == '__main__':
#     eq = '5+6*4/3-8/2'
#     canculate(eq)
    str1 = '{([{}])}'  # mated
    str2 = '{[]}()'    # mated
    str3 = '{[{})]}'   # unmated
    str4 = '{[{]}'   # unmated
    str5 = '{([]))'   # unmated

    printLegal(str1)
    printLegal(str2)
    printLegal(str3)
    printLegal(str4)
    printLegal(str5)

        
            