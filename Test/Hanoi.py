#  Created by IvanaH on 02/02/18.
#  coding: UTF-8
from test.test_threading_local import target

def move(originSt, targetSt, dependSt):
        if len(originSt)==1:
            target.append(originSt.pop())
        else:
            move(n-1)
            target.append(originSt.pop())
        
def hanoi(n):
    stack originSt=[]
    stack targetSt=[]
    stack dependSt=[]
    
    for i in range(1,n):
        originSt.append(i)

    move(originSt, targetSt, dependSt)
        
        
    
    