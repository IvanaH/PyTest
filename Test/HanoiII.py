#  Created by IvanaH on 14/02/18.
#  coding: UTF-8

class hanoi():
     
    def __init__(self,n):
        self.n = n
        self.origin = []
        self.depend = []
        self.target = []
        for i in range(1,n+1):
            self.origin.append(i)
             
    def move(self, n, origin, depend, target):
        print("The start is ",origin)
         
        if n==1:
           target.append(origin.pop())
           print(target)
           return
        else:
           self.move(n-1,origin,target,depend)
           self.move(1,origin,depend,target)
           self.move(n-1,depend,origin,target)
        print(target)
         
hanoiTest = hanoi(3)
hanoiTest.move(hanoiTest.n,hanoiTest.origin,hanoiTest.depend,hanoiTest.target)


# implement in method 
# origin = [1,2,3,4]
# depend = []
# target = []
#             
# def move(n, origin, depend, target):       
#     if n==1:
#         target.append(origin.pop())
#         print(target)
#         return
#     else:
#         move(n-1,origin,target,depend)
#         move(1,origin,depend,target)
#         move(n-1,depend,origin,target)
#     
# 
# move(len(origin),origin,depend,target)
