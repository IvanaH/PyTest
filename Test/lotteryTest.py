#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/9/03
@author:Ivana
'''
import requests
import threading
# import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='/erest.log',
#                     filemode='w')


def getLottery(userInfo):
    url = 'http://10.0.10.158:7023/ygw/api/dispatch/activity/call-charge/user/lottery'
    headers = {'Cookie':'mToken=eyJ0aW1lc3RhbXAiOjE1Njc1ODIyMTA2NzQsInJvd1Rva2VuIjoiMjFjMGRkZmEwM2MwYTI2ZDkyYzViMDA1NmM1NjRiNTkiLCJ1aWQiOjc4NjY2MSwibW9iaWxlIjoiMTUwODg2MDMzNjQiLCJkZXZpY2VJZCI6Ijg2Njc3ODAzNTgzNjYwNCIsImNsaWVudFZlcnNpb24iOiI0LjEuMSIsImRldmljZU1vZGVsIjoiTWVpenUiLCJndWVzdCI6ZmFsc2V9'}
            
#     logger = logging.getLogger()
    r = requests.request('POST',url,headers=headers,json=userInfo)    
    if r.status_code == 200:
#         print(r)
        try:
            resp = r.json()['data']
            print('%s : %s : %s' %(resp['userMobile'],resp['prizeName'],resp['id']))
        except Exception:
            print("Exception occurred when to json.") 
            print(r.content)
    else:
        print(r.status_code)
        
def getUinfo(fpath):
    uInfoList = []
    with open(fpath, 'r') as f:
        for line in f.readlines():
            s = line.split()
            userInfo = {}
            userInfo['userId'] = s[0]
            userInfo['userMobile'] = s[1]  
            uInfoList.append(userInfo) 
    return uInfoList
    
if __name__ == '__main__':
#    uinfo = {"userInfo":{"userId":786661,"userMobile":"15088603364"}}
    uInfos = getUinfo("uInfos.txt")
    
    for i in range(10):
#         print(uInfos[i])    
        uInfo = {"userInfo":uInfos[59]}  
        t = threading.Thread(target=getLottery,args=(uInfo,))
        t.start()
       
#     for i in range(3,20):
#         uInfo = {"userInfo":uInfos[i]}
#         print(uInfo)
#         getLottery(uInfo)

#     uInfo = {"userInfo":uInfos[59]}
#     print(uInfo)
#     getLottery(uInfo)    
    
    
    