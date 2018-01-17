'''
Created on 2017.4.12
@author: Ivana_ShineMo
'''

# s = 'Hello World.'
# x = 3.224*10
# y = 4.5 * 1000
# 
# str(s)
# repr(s)
# s = "The value of x is: "+ repr(x)+", and y is "+repr(y)
# print(s)
# 
# str(x)
# repr(x)
# print(x)
# 
# str(y)
# repr(y)
# print(y)

def learnList():
    fruits = ['orange','apple','banana','kiwi','apple','watermelon','lemon']
    print(fruits)
    fruits.append('pear')
    print(fruits)
    print(fruits.count('banana'))
    print(fruits.index('apple',3))
    print("Sort the fruits list")
    fruits.sort()
    print(fruits)
    fruits.reverse()
    print(fruits)
    print(fruits.pop())
    
learnList()