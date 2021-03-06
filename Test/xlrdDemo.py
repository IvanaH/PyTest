import xlrd

class readContent:
    def __init__(self,filename):
        self.filename = filename
    
    def open_excel(file=self.filename):
        try:
            data = xlrd.open_workbook(self.filename)
            return data
        except Exception as e:
            print (e)
            
    #根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_index：表的索引
    def excel_table_byindex(colnameindex=0,by_index=0):
        data = open_excel(self.filename)
        table = data.sheets()[by_index]
        #行数
        nrows = table.nrows 
        #列数
        ncols = table.ncols 
        #某一行数据 
        colnames =  table.row_values(colnameindex) 
     
        list =[]

        for rownum in range(1,nrows):
            row = table.row_values(rownum)
            if row:
               app = {}
               for i in range(len(colnames)):
                   app[colnames[i]] = row[i] 
                   list.append(app)
        return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
    def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
        data = open_excel(file)
        table = data.sheet_by_name(by_name)

        nrows = table.nrows #行数 
        colnames =  table.row_values(colnameindex) #某一行数据 
        list =[]

        for rownum in range(1,nrows):
            row = table.row_values(rownum)
            if row:
               app = {}
               for i in range(len(colnames)):
                   app[colnames[i]] = row[i] 
                   list.append(app)
        return list
    

rc = readContent('D:\Python27\11.xls')
rc.excel_table_byindex(file, colnameindex, by_index)