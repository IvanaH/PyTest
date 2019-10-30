#! usr/bin/env python
# -*- coding: utf-8 -*-

''' 
create 2019/10/18
@author: Ivana
'''

def variadicP(p1 = None,*args):
    print("Function name:%s" % variadicP.__name__)
    if p1 == None:
        print("positional paramter p1 is by default, and others is %s" %(args))
    else:
        print("p1 is by %s, and others is %s \n" % (p1,args))   

def defaultAndVariadicArgu(a,b=10,c=2,*args):  
    print("a = %s,b= %s,c=%s, and the variadic arguments are: %s\n" %(a,b,c,args))  
    
def keywordP(p1,*,kw1,kw2,**kw):
    print("Function name:%s, and param p1 is %s" % (keywordP.__name__,p1))
    print(" %s,%s are named keyword paramters." %(kw1,kw2))
    print("And kw, the keyword paramters are accepted as a dictionary: %s\n" % (kw))

def mixedP(p1,*args,kw1,kw2):
    print("Function name:%s, and param p1 is %s" % (mixedP.__name__,p1))
    print("%s are variadic paramters which accpeted as tuple, %s,%s are named keyword paramters.\n" %(args, kw1,kw2))
    
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

if __name__ == '__main__':
    p1V = 'positional paramter'
    kw1V, kw2V = 1,2
    dict0 = {'d1':11,'d2':22}
    list0 = list("this is a list")
    
#     variadicP()   #Cause: TypeError: not enough arguments for format string
    variadicP('args1','args2')
    variadicP(p1V,'args3')
      
    defaultAndVariadicArgu(0, 3)
    defaultAndVariadicArgu(0, *list0)   
    
    keywordP(p1V,kw1=kw1V,kw2=kw2V)
    keywordP(p1V,kw1=kw1V,kw2=kw2V,**dict0)
    keywordP(p1V,kw1=kw1V,kw2=kw2V,d3=33,d4=44)
      
    mixedP(p1V,*list0,kw1=kw1V,kw2=kw2V)
     


#     f1(1, 2, 3, 'a', 'b', x=99)  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
#     f1(1,2,x=99,y=98,c=97)    # a = 1 b = 2 c = 97 args = () kw = {'x': 99, 'y': 98}
#     f1(1,2,10,x=99,y=98,c=97)   # TypeError: f1() got multiple values for argument 'c'
#     

    
    