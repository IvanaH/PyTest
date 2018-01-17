# implementation of quick sort Version I

class qsort:    
    alist = [17,13,23,1,34,45,23,2,5,12,9,31,22,10]
    
#     def __init__(self,alist,p):
#         self.alists = alist
#         self.p = p


    def qsort(self):
        alists = qsort.alist         
        p = 0
        k = len(alists)-1
        j=k
        pivot = alists[p]
        for i in range(0,len(alists)-1):
            if i>=j:
                break
            elif alists[i] < pivot:
                continue
            else:
                alists[p] = alists[i]
                alists[i] = pivot
                p=i
                for j in range(k,0,-1):
                    if i>=j:
                        break
                    elif alists[j] > pivot:
                        continue
                    else:
                        alists[p] = alists[j]
                        alists[j] = pivot
                        p=j
                        k=j-1
                        print pivot, alists
                        break         
                
                    
qsort1=qsort()
qsort1.qsort()              
            