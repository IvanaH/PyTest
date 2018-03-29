#  Created by IvanaH on 28/03/18.
#  coding: UTF-8
from datetime import date 
from datetime import timedelta 
from random import random, randint
import re
import codeop

class generate():
    def __init__(self):
        self.idN = []
    
    def getDistrictCode(self):
        with open('districtCode.txt') as file:
            data = file.read()
        dLists = data.split('\n')
#         print(dLists)
#         global codelist
        codelist = []
        pattern = re.compile('\d+')
        for dlist in dLists:
#             print(dlist)
            if pattern.match(dlist) :
#                 print(pattern.match(dlist).group(0))
                codelist.append(pattern.match(dlist).group(0))
#         print(codelist)
        districtCode = codelist[randint(0,len(codelist))]
        return districtCode
        
    
    def getBirthDate(self):
        year = randint(1920,2000)
#         moth = randint(1,12)
#         day = randint(1,31)
        da = date.today()+timedelta(days=randint(1,366))
        da  = da.strftime('%m%d')
        return str(year)+da

    
    def getSerialNumber(self):
        sn = randint(100,300)
        return str(sn)
    
    def getCheckCode(self):
        idN = self.getDistrictCode()+self.getBirthDate()+self.getSerialNumber()
         
        i = 0
        count = 0
         
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        SIN = {'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'}
         
        for i in range(i,len(idN)):
            count = count + int(weight[i])*int(idN[i])
        count = count%11
         
        checkcode = SIN[str(count)]
         
        return checkcode
         
     
    def getNumber(self):
        return self.getDistrictCode()+self.getBirthDate()+self.getSerialNumber()+self.getCheckCode()    

def test():
    str = '654324 �½�ά���������������̩�������ͺ���'
    pattern = re.compile('\d+')
    if pattern.match(str):
        return pattern.match(str).group(0)
         
    
if __name__ == '__main__':
#     print (test())
    i = True
    h = generate()

    while(i):
        print(h.getNumber())
        a = raw_input("Do you want another number?(enter any character)")
        if a != '':
#         if a == 'Y':
            continue
        else:
            break

