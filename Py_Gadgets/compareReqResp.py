#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/09/16

@author:Ivana
'''
import requests
import json


def req(url,args,code, **kwargs):
    resp = requests.request('GET', url,params=args)
    
    if resp.status_code != code:
        return False
    else:
        print(resp.json())
    return True

# validVu is a list of dicts, k:v for expected k:v in json
def compResp(rspo,validVu):
   try:
       json.loads(resp)
   except Exception as ValueError:
        print("The response is not json.")
        
   for i in range(len(validVu)):
       if rspo(validVu[i].keys()[0]) == validVu[i].values()[0]:
           pass

if __name__ == '__main__':


    