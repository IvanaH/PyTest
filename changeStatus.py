from telnetlib import STATUS
class change_status:
    status = ["created", "dispatched","arriving", "arrived", "serviceStarted", "serviceFinished", "feeSubmitted", "paid", "completed"]
    
    def __init__(self, url):
        self.url = url
        
    def setCookie(self,cookie):
        r = "http://app.e.uban360.net/gateway/shenzhou/getUserInfo.do?payToken="+cookie
        print(r)
        
    def setStatus(self,):
        if(statu in status):
            
        else:
            print("%s is an illegal status." %rstatus)