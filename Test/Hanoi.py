#  Created by IvanaH on 02/02/18.
#  coding: UTF-8

def move(n, originSt, targetSt, dependSt):
#     while(len(target)<n):
        #n==1  1
#         target.append(originSt.pop())
        
        #n==2 2 1
#         cst.append(originSt.pop())
#         target.append(originSt.pop())
#         target.append(cst.pop())
        
#         #n ==3 2 1 1 2 1
#         target.append(originSt.pop())
#         cst.append(originSt.pop())
#         cst.append(target.pop())
#         target.append(originSt.pop())
#         originSt.append(cst.pop())
#         target.append(cst.pop())
#         target.append(originSt.pop())
#         
#         #n==4  2 1 1 2 2 2 1 1 2 1
#         cst.append(originSt.pop())
#         target.append(originSt.pop())
#         target.append(cst.pop())
#         cst.append(originSt.pop())
#         originSt.append(target.pop())
#         cst.append(target.pop())
#         cst.append(originSt.pop())
#         target.append(originSt.pop())
#         target.append(cst.pop())
#         originSt.append(cst.pop())
#         originSt.append(target.pop())
#         target.append(cst.pop())
#         cst.append(originSt.pop())
#         target.append(originSt.pop())
#         target.append(cst.pop())        
        if n==1:
            target.append(originSt.pop())
        else:
            move(n-1)
            target.append(originSt.pop())
        
        
    
    