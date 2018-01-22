#coding: UTF-8

import xlrd

def read_excel():
    #打开文件
    workbook = xlrd.open_workbook(r'D:\Python27\11.xls')
    #获取所有sheet
    print workbook.sheet_names() 
    sheet1_name = workbook.sheet_names()[0]
    
    #get content from sheet by sheet index of sheet name
    sheet1 = workbook.sheet_by_index(0)
    sheet2 = workbook.sheet_by_name('train')
    
    #name,colnums,rownums
    print sheet1.name,sheet1.nrows,sheet1.ncols
    
    #get values(list) from certain column or row
    rows = sheet1.row_values(0)  
    cols = sheet1.col_values(1)
    print rows
    print cols
    
    #get content of CELL
    print sheet1.cell(1,0).value.encode('utf-8')
    print sheet1.cell_value(1,0).encode('utf-8')
    print sheet1.row(1)[0].value.encode('utf-8')
    
    #get type of content from certain CELL
    print sheet2.cell(1,1).ctype
    

if __name__ == '__main__':
    read_excel()