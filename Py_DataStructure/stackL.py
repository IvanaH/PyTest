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
    
    for i in range (0,len(equation)):
        print(equation[i])
        if equation[i] == '*' or equation[i] == '/':
            stackOperator.append(equation[i])
            print("push into sO")
        elif equation[i] == '+' or equation[i] == '-':
            if len(stackOperator) > 0:
                flag = True
                while flag:
                    if stackOperator[-1]== '*' or stackOperator[-1] == '/':
                        k = int(stackNum.pop())
                        j = int(stackNum.pop())
                        op = stackOperator.pop()
                        r = canculation(j, k, op)
                        stackNum.append(r)
                        print("change num %i,%i,%s,%i",j,k,op,r)
                        continue
                    flag = False
            stackOperator.append(equation[i])
            print("push into sO")
        else:
            stackNum.append(equation[i])
            print("push into sN")
    
    print(stackNum)
    print(stackOperator)

    for i in range(0,len(stackOperator)):
        k = int(stackNum.pop())
        j = int(stackNum.pop())
        op = stackOperator.pop()
        stackNum.append(canculation(j, k, op))
    print (stackNum.pop())
    
if __name__ == '__main__':
    eq = '5+6*4/2-8'
    canculate(eq)

        
            