#  Created by IvanaH on 14/02/18.
#  coding: UTF-8

class hanoi():
    depend = []
    target = []
    origin = []
    
    def __init__(self,n):
        self.n = n
        for i in range(1,n):
            self.origin.append(i)
            
    def move(n,origin,depend,target):
        print(origin)
        print(target)
        
        if n==1:
#         print (a,'-->',c)
           target.append(origin.pop())
#            print("From:"+self.origin)
#            print("To:"+self.target)
           return
        else:
           move(n-1,origin,target,depend)
           move(1,origin,depend,target)
           move(n-1,depend,origin,target)
        print(target)

        

hanoiTest = hanoi(4)
hanoiTest.move()