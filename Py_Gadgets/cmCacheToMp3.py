#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2019/09/17

@author:Ivana
'''
import os
import requests
import sys

def getRName(id):
    url = 'https://api.imjad.cn/cloudmusic'
    args = {'type':'detail','id':id}
    name = str(id)
    ar = str(id)
    
    try:
        req = requests.get(url,params=args).json()
        name = req['songs'][0]['name']
        ar = req['songs'][0]['ar'][0]['name']
    except Exception as e:
        print(sys._getframe().f_code.co_name + ":"+ e)
        
    return name+'_'

def toMp(fname,fpath=None):
#     get real name of the mp3 file by id and the api: https://api.imjad.cn/cloudmusic/?type=detail&id=188878
    realname = getRName(fname.split('-')[0])
    newfileN = realname+'.mp3'
    if fpath != None:
        filename = fpath+fname
    else:
        filename = fname
    
    try:
        with open(filename,'rb') as f:
            barry = bytearray(f.read())
        with open(newfileN,'wb') as out:
            for i,j in enumerate(barry):
                barry[i] = j ^ 0xa3
            out.write(bytes(barry))
    except Exception as e:
        print(fname+ ":"+ str(sys._getframe().f_code.co_name) + ":"+ str(e))
        return False 
    print(realname + ": Done!")   
    return True

def toMpBatch(fnames,fpath=None):
    s = 0
    f = 0
    for file in fnames:
        if toMp(file,fpath) == True:
            s = s+1
        else:
            f = f+1
    print("total:%d success:%d fail:%d" %(len(fnames),s,f))

def getFileName(fdir,postfix=None):
    fnames = []
    os.walk(top, topdown, onerror, followlinks)
    for file in os.listdir(fdir):
        if postfix != None:
            if os.path.splitext(file)[1] == postfix:
                fnames.append(file)
        else:
            fnames.append(file)
    return fnames


if __name__ == "__main__":
    fpath = r'D:\JavaL\WorkSpace\PyTest\Py_Gadgets\cmCache\\'
#     for fname in getFileName(fpath,postfix='.uc!'):
#         print(fname)
#     filename = '64797-96000-e4441e04cf99ca2ca224d5ad1d787c05.mp3.uc!'
#     print(toMp(filename,fpath=fpath))
    fnames = getFileName(fpath,postfix='.uc!')
    toMpBatch(fnames ,fpath=fpath)
#     print(getName(188878))
