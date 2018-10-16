#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018/9/29

@author:Ivana
'''

import requests
from code import args
from pathlib import Path
from certifi import __main__

class sendReqs:
    def __init__(self,count,path,method,args):
        threading.Thread.__init__(self)
        self.path = path
        self.method = method
        self.args = args
        self.count = count
        
    def sendReq(self):
        resp = requests.request(self.method, self.path, params = self.args, data=self.kwargs.get('data'))

        print('response status code: %s' % (resp.status_code))
        
        try:
            resp.json()
        except:
            return False
        #print(resp.json())
        return True
    

def myThreads(thread_num):
    thread_list = list()
    count = 5
    path = 'http://app.e.uban360.net/gateway/xiaojukeji/orderCreate'
    method = 'GET'
    arges = {'rule':301,'type':0,'city':5,
           'flat':30.282025,'flng':120.068662,
           'start_name':'%E8%A5%BF%E6%B9%96%E5%8C%BA%E6%96%87%E4%BA%8C%E8%A5%BF%E8%B7%AF798%E5%8F%B7',
           'start_address':'%E8%A5%BF%E6%B9%96%E5%8C%BA%E6%96%87%E4%BA%8C%E8%A5%BF%E8%B7%AF798%E5%8F%B7',
           'tlat':30.291119,'tlng':120.213064,
           'end_name':'%E6%9D%AD%E5%B7%9E%E4%B8%9C%E7%AB%99',
           'end_address':'%E5%A4%A9%E5%9F%8E%E8%B7%AF1%E5%8F%B7',
           'require_level':600,
           'dynamic_md5':'d3cc7bb731aefe19ab80b93df34daf5e','price':61.9,
           'app_time':appTime,
           'quotaType':1,'quotaId':2690,
           'payToken':'eyJhcHBJZCI6IjY1NjMxNDMiLCJvcmdJZCI6ODM4MTcsInNjb3BlSWQiOjk3LCJzaWduYXR1cmUiOiJlZTI5MmFiZDJhNTlhNTM5YmU3MjBhYzRkMjNjNmI2YSIsInNpdGVJZCI6MSwidGltZXN0YW1wIjoxNTM3ODQ3MTI2MjA4LCJ1aWQiOiIxMDEwMTAwMTc4ODY0OCJ9'
}
    
    sendRqs = sendReqs(count,path,method,args)
    
    for i in range(0,thread_num):
        thread_list.append(threading.Thread(target=sendRqs.sendReq,name=thread_name,args=())
    
    for thread in thread_list:
        thread.start()
        
    for thread in thread_list:
        thread.join()
    
     
if __name__ == "__main__":
    myThreads(5)
    