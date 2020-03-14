#coding:utf-8

import  os
# 项目的更路径
root_path = os.path.abspath(os.path.dirname(__file__)).split('shippingSchedule')[0]

path = root_path +"/../data/"


# 读取excel文件的方法
import xlrd
def read_excel(excelPath="",tableName=None):
    # 打开excel表
    excelPath=path+excelPath
    book = xlrd.open_workbook(excelPath)
    # 找到sheet页
    table = book.sheet_by_name(tableName)
    # 获取总行数总列数
    row_Num = table.nrows
    col_Num = table.ncols
    s = []
    if row_Num <= 1:
        print("没数据")
    else:
        j = 1
        for i in range(row_Num - 1):

            d = [0]*col_Num
            values = table.row_values(j)
            for x in range(col_Num):
                d[x] = values[x]
            d =tuple(d)
            j += 1
            s.append(d)
        return s



# 读取 yaml文件的方法
def read_yaml():
    pass






