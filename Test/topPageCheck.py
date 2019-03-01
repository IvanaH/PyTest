#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018/11/20

@author:Ivana
'''

import requests

def testCase(path, method, validation, code, args, **kwargs):
    resp = requests.request(method, path, params = args, data=kwargs.get('data'))

    if resp.status_code != code:
        print('\ntest %s\nstatus code %s' % (path, resp.status_code))
        if args is not None:
            print('\nparameters: %s' % (args)) 
        if kwargs.get('data') is not None:
            print('\ndata: %s' % (kwargs.get('data'))) 
        try:
            print(resp.json())
        except:
            pass
        return False
        
    try:
        resp.json()
    except:
        return False
    
    resp.request.params = args
    resp.request.data = kwargs.get('data')
    
#     need to get the name of testCase
    if validation(resp.request, resp.json()):
        print('\n%s: validate successfully !'%(validation.__name__))
    else:
        print('\n%s: test fail!' %(validation.__name__))
        print(path)
        if args is not None:
            print('parameters: %s' % (args)) 
        if kwargs.get('data') is not None:
            print('data: %s' % (kwargs.get('data'))) 
        print(resp.json())
    return True


class BSuite:
    def allCases(self):
        success = 0
        total = 0 
        for k in self:
            requests.session().cookies.clear()
            if type(k) == 'function' and k.startsWith('test'):
                total += 1
                success = success +  1 if self[k]() else 0
        print('success count %d/ total count %d', success, total)
            

if __name__ == "__main__":
    def validation1(request, resp):
            print (str(request.url))
            return True
    
    path = 'http://acl.jituancaiyun.net/power/qr/api/generate.do'
    method = 'GET'
            
    testCase(path, method, validation1, 200, args={'reqp':1})

