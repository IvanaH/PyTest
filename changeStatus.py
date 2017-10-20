<<<<<<< HEAD
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
=======
class change_Status:
    status = ['dispatched','arriving','arrived','serviceStarted','serviceFinished','feeSubmitted','completed']
    
    def __init__(self, link):
        self.link = link
        self.setCookie = False

    def setCookieC(self,token):
        print(self.link+'?%s'%token)
        self.setCookie = True

    def setStatusC(self,url,oid,value):
        self.link = url
        if self.setCookie:
            if value in change_Status.status:
                i = change_Status.status.index(value)+1
                print(i)
                for statu in change_Status.status[:i]:
                    print(self.link+'?driverId=43851&clat=30.273928&clng=120.159556&actualKiloLength=10&orderId=%s&status=%s'%(oid,statu))
            else:
                print('Status: %s is illegal.'%value)
        else:
            print("Please set cookie at first")        
            
url1 = "http://app.e.uban360.net/gateway/shenzhou/getUserInfo.do"
url2 = "http://app.e.uban360.net/gateway/shenzhou/orderChangeStatus"
cStatus = change_Status(url1)
cStatus.setCookieC("payToken=AQABAAAAAAAAADidAQAAAAAAQPnU3VgBAABjMTFmZWI4ZGRmMDQ4YWVlMGQ0OGU1NjQ3MGIyNmJkZQ==")
cStatus.setStatusC(url2,"6377142869826207747","arriving")
>>>>>>> cff1dd06a18954f952887e97450ba9ea1d5e6072
