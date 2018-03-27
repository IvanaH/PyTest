#  Created by IvanaH on 14/02/18.
#  coding: UTF-8

# class hanoi():
    
#     def __init__(self,n):
#         self.n = n
#         self.origin = []
#         self.depend = []
#         self.target = []
#         for i in range(1,n):
#             self.origin.append(i)
#     origin = [1,2,3,4]
#     depend = []
#     target = []
#             
#     def move(n, origin, depend, target):
#         print(origin)
#         print(target)
#         
#         if n==1:
# #         print (a,'-->',c)
#            target.append(origin.pop())
# #            print("From:"+self.origin)
# #            print("To:"+self.target)
#            return
#         else:
#            move(n-1,origin,target,depend)
#            move(1,origin,depend,target)
#            move(n-1,depend,origin,target)
#         print(target)


# implement in method 
origin = [1,2,3,4]
depend = []
target = []
            
def move(n, origin, depend, target):       
    if n==1:
        target.append(origin.pop())
        print(target)
        return
    else:
        move(n-1,origin,target,depend)
        move(1,origin,depend,target)
        move(n-1,depend,origin,target)
        

        
# hanoiTest = hanoi(4)
# hanoiTest.test(hanoiTest.origin)

move(len(origin),origin,depend,target)
