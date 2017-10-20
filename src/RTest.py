# -*- coding: UTF-8 -*-
'''
Created on 2017年3月19日
@author: IvanaHH
'''

import urllib,urllib2
import requests
import json

class SendRequest(object):
    def __init__(self,url):
        self.url = url
        
    #post request
    def post(self,value =None):
        params = urllib.urlencode(value)
        try:
            req = requests.post(self.url +"?%s"%params)
        except Exception,err:
            print err
        if req.status_code == 200:
            print("Send post request: %s, and get return: %s" %(req.url, req.status_code))
        else:
            print("Send post request: %s, and get return: %s\n error info: %s" %(req.url, req.status_code,req.text))
    
    
    def post_json(self, value):
        head = {'content-type': 'application/json'}
        try:
            req = requests.post(self.url, data = json.dump(value),headers=head)
            print req.url
        except Exception,err:
            print err
        if req.status_code == 200:
            print("Send post request: %s, and get return: %s" %(req.url, req.status_code))
        else:
            print("Send post request: %s, and get return: %s\n error info: %s" %(req.url, req.status_code,req.text))
    
    
    def get(self, value = None):
        try:
            req = requests.get(self.url,params = value)
        except Exception,err:
            print err
        if req.status_code == 200:
            print("Send post request: %s, and get return: %s" %(req.url, req.status_code))
        else:
            print("Send post request: %s, and get return: %s\n error info: %s" %(req.url, req.status_code,req.text))
        return req.text
    
