#  Created by IvanaH on 04/02/19.
#  coding: UTF-8

import xlrd
import logging


def setOutput(loc):
#     LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_FORMAT = "%(message)s"
    if loc != "Console":
        logging.basicConfig(filename = loc,level=logging.INFO, format=LOG_FORMAT)
    else:
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)   


def open_excel(filepath):
    workbook = xlrd.open_workbook(filepath)
    return workbook

def get_rows(wb,i):
    rows = wb.sheet_by_index(i).nrows
    return rows

def get_cols(wb,i):
    cols = wb.sheet_by_index(i).ncols
    return cols

def get_row_content(wb,i,index):
    rowc = wb.sheet_by_index(i).row_values(index)
    return rowc

def get_col_content(wb,i,index,sindex,eindex):
    colc = wb.sheet_by_index(i).col_values(index,sindex,eindex)
    return colc

def genSql():
    setOutput('D:\Python36\sql.txt')
    
    wb = open_excel('D:\Python36\cupon.xlsx')
    itemList = get_col_content(wb,0,1,0,232)
    couponList = get_col_content(wb,0,0,0,13)
#     print(couponList)

    for i in range(1,len(couponList)):
        for j in range(1,len(itemList)):
#     for i in range(1,2):
#         for j in range(1,2):
#             ns = "insert into `coupon_item` set gmt_create = now(),gmt_modified = now(),biz_type = 139, coupon_id ="+str(int(couponList[i]))+" ,item_id = "+str(int(itemList[j]))+";"
            ns = "insert into `coupon_item` set gmt_create = now(),gmt_modified = now(),biz_type = 139, coupon_id ="+str(int(couponList[i]))+" ,item_id = "+str(int(itemList[j]))+";"
            logging.info (ns)         
    print("Done!")
        
if __name__ == '__main__':
    genSql()
    
    
