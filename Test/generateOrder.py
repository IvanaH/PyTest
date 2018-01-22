#  Created by IvanaH on 01/22/18.
#  coding: UTF-8

import xlrd
 
def open_excel(filepath):
    workbook = xlrd.open_workbook(filepath)
    return workbook


def get_rows(wb):
    rows = wb.sheet_by_index(0).nrows
    return rows

def get_cols(wb):
    cols = wb.sheet_by_index(0).ncols
    return cols

def get_row_content(wb,index):
    rowc = wb.sheet_by_index(0).row_values(index)
    return rowc

def get_col_content(wb,index):
    colc = wb.sheet_by_index(0).col_values(index)
    return colc

def gen_sql(lists,uid,uname,quotaId,quotaType,scopeId):
    sConstant = 'insert in buy_order set quota_id= %d,quota_type= %d,create_user_id=%d,create_user_name=%d,scope_id=%d,update_user_id=%d,update_user_name=%d,gmt_create=now(),order_create_time=now(),gmt_pay=now()' %(quotaId, quotaType,uid,uname,scopeId,uid,uname)
#     sConstant = 'insert in buy_order set quota_id=%d, quota_type=%d' %(quotaId,quotaType)
#     print sConstant
    
    params = ['order_id','gmt_created']
#     params = ['order_id','biz_type','third_id','price','extend','pay_type','order_type','order_status','order_sub_status','version','channel_type','source_app','app_type','account_type','refund_price','sub_type','parent_order_id']
    sDyn =''
    
#     if len(params) != len(lists):
#         return False
    
    for i in range(0,len(lists)):
        for j in range(0,len(lists[i])):
            sDyn= sDyn+','+params[j]+'='+lists[i][j]
#         print sDyn
        iSql = sConstant+sDyn
        print iSql
        sDyn=''    
#         print sDyn


        

class read_excel:
    def __init__(self,filepath):
        self.filepath = filepath

     
    def get_rows_content(self):
        wb = open_excel(self.filepath)
        
        nrow = get_rows(wb)
        ncol = get_cols(wb)
        list = []
        
        for i in range(1,nrow):
            list.append(wb.sheet_by_index(0).row_values(i))
         
        return list
            

            
if __name__ == '__main__':
    re = read_excel(r'D:\Python27\11.xls')         
    values = re.get_rows_content()
    
#     for i in range(0,len(values)):
#         for j in range(0,2):
#             print values[i][j]
    
#     for i in range(0,len(values)):
#         print values[i]
    
    gen_sql(values, 1, 1, 1, 1, 1)
    
    
    
