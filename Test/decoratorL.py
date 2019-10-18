#! usr/bin/env python
# -*- coding: utf-8 -*-
'''
create 2019/10/15
@author:Ivana
'''

import logging

def use_log(func):
    def wrapper(*args,**kw):  #can recept any paramters, and adapte to any functions
        print("%s is runing." % func.__name__)
        return func(*args,**kw)
    return wrapper

def soph_log(level='None'):
    def decorator(func):
        def wrapper(*args,**kw):  
            if level == 'A':
                print("%s is runing on level A." % func.__name__)
            elif level == 'B':
                print("%s is runing on level B." % func.__name__)
            else:
                print("%s is runing on un unknown level." % func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

def a_log(func):
    print("use a_log")
    def wrapper():
        print("wrapper of a_log")
        return func()
    return wrapper

def b_log(func):
    print("use b_log")
    def wrapper():
        print("wrapper of b_log")
        return func()
    return wrapper

# @use_log  # means: func1 = use_log(func1)
# def func1():
#     print("work in func1.\n")
# 
# @use_log   
# def func2(name,city='HangZhou',mobile = None):
#     print("The name is %s , city is %s and mobile is %s.\n" %(name,city,mobile))
# 
# # @soph_log()  #use @soph_log, just get decorator(), then func3 will not excute 
# def func3(name,city='HangZhou',mobile = None):
#     print("The name is %s , city is %s and mobile is %s.\n" %(name,city,mobile))
# 
# @soph_log('A')
# def func4(name,city='HangZhou',mobile = None):
#     print("The name is %s , city is %s and mobile is %s.\n" %(name,city,mobile))
#    
# @a_log   
# @b_log
# def func5():
    print("work in func5")

class Test(object):
    def __init__(self,func):
        print("start init.")
        print("func name is %s." % func.__name__)
        self.__func = func
    def __call__ (self,*args,**kw):
        print("function in decorator.")
        self.__func(*args,**kw)

@Test
def test(msg):
    print('this is test func: %s' % msg)
            
@Test
def test2(msg,**kw):
    print('this is test func: %s' % msg)
    print('Other params are: %s' %kw)
    
if __name__ == '__main__':
    msg = "Let's test"
    toh = {'p1':1,'p2':2}
    test(msg)
    test2(msg,**toh)
# #     test = use_log(func)
# #     test()
#     func1()
# #     test = use_log(func2)
# #     test("Shinemo")
#     func2("Shinemo",mobile = '15010002000')
# #     test = soph_log(func3)
# #     print(test.__name__)
# #     test ('Ivana')
#     func3('Ivana')
# #     test = soph_log(level='A')(func4)
# #     test("Jean")
#     func4('Jean')
#     func5()    

