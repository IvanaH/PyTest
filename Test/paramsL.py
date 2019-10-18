#! usr/bin/env python
# -*- coding: utf-8 -*-

''' 
create 2019/10/18
@author: Ivana
'''

def variadicP(p1 = None,*args):
    print("Function name:%s" % self.__name__)
    if p1 == None:
        print("positional paramter p1 is by default, and others is %s" % args)
    else:
        print("p1 is by %s, and others is %s" % (p1,args))   

def defaultAndVariadicArgu(a,b=1,*args):  
    print("a = %s,b= %s, and the variadic arguments are: %s" %(a,b,args))  
    
def keywordP(p1,*,kw1,kw2,**kw):
    print("Function name:%s, and param p1 is %s" % (self.__name__,p1))
    print("%s:%s and %s:%s are named keyword paramters." %(kw1.__name__,kw1,kw2.__name__,kw2))
    print("And kw, the keyword paramters are accepted as a dictionary, the keys are %s, and values are %s" % (kw.keys(),kw.values()))

def mixedP(p1,*args,kw1,kw2):
    print("Function name:%s, and param p1 is %s" % (self.__name__,p1))
    print("%s are variadic paramters which accpeted as tuple, %s:%s and %s:%s are named keyword paramters." %(args, kw1.__name__,kw1,kw2.__name__,kw2))
    
if __name__ == '__main__':
    p1V = 'fixed paramter'
    kw1V, kw2V = 1,2
    dict0 = {'d1':11,'d2':22}
    list0 = list("this is a list")
    
#     variadicP(p1 = p1V)
#     variadicP('args1','args2')
#     variadicP(p1 = p1V,'args3')
#     
# 
#      
#     keywordP(p1V,kw1=kw1V,kw2=kw2V)
#     keywordP(p1V,kw1=kw1V,kw2=kw2V,**dict0)
#     keywordP(p1V,kw1=kw1V,kw2=kw2V,d3=33,d4=44)
#      
#     mixedP(p1=p1V,*list0,kw1=kw1V,kw2=kw2V)
    
#     defaultAndPositionalArgu(0, 3)
    defaultAndPositionalArgu(0, b=3, 4, 5)    
    
    
    