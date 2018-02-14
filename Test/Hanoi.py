#  Created by IvanaH on 02/02/18.
#  coding: UTF-8

def move(n, originSt, targetSt, dependSt):
        ## if there is only one plate, move it from the start to the target 
        if n ==1:
            targetSt.append(originSt.pop())
            print (originSt,'-->', dependSt)
            return
        else:
        ## move n-1 plates from the start to the depend
            move(n-1, originSt, dependSt,targetSt)
        ## move the last plate to the target
            targetSt.append(originSt.pop())
        ## move the n-1 plates from the depend to the target
            move(n-1, dependSt, targetSt,originSt)
                    
def hanoi(n):
    # the start stack 
    stackA=[]
    # the target stacK
    stackB=[]
    stackC=[]
    
    
    for i in range(1,n+1):
        stackA.append(i)
 
    move(n,stackA,stackB,stackC)
        
        
hanoi(4)
    