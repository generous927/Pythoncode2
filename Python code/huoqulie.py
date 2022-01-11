# -*- coding: UTF-8 -*-
# import xlrd
#
# def extract(inpath):
#     data = xlrd.open_workbook(inpath, encoding_override='utf-8')
#     table = data.sheets()[1]  # 选定表
#     nrows = table.nrows  # 获取行号
#     ncols = table.ncols  # 获取列号
#
# for i in range(1, nrows):
#     alldata = table.row_valus(i)  # 循环输出Excel表中每一行，即所以数据
#     result = alldata[6]  # 取出表中第二列数据
#     print(result)
#
# inpath = 'C://Users//Administrator//Desktop//接口自动化1.xls'
# extract(inpath)

import xlrd
import json

worksheet = xlrd.open_workbook(u'C://Users//Administrator//Desktop//接口自动化1.xls')
sheet_names= worksheet.sheet_names()
print(sheet_names)

for sheet_name in sheet_names:
    sheet = worksheet.sheet_by_name(sheet_name)
    rows = sheet.nrows # 获取行数
    cols = sheet.ncols # 获取列数，尽管没用到
    for i in range(1,rows) :
        cell = sheet.cell_value(i, 6) # 取第六列数据
        print(cell)
