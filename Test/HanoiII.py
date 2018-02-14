#  Created by IvanaH on 14/02/18.
#  coding: UTF-8

def hanoi(n,a,depend,c):
    if n==1:
        print (a,'-->',c)
        return
    else:
        hanoi(n-1,a,c,depend)
        hanoi(1,a,depend,c)
        hanoi(n-1,depend,a,c)
        

hanoi(15, "a", "b", "c")