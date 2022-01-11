# -*- coding: UTF-8 -*-

import xlrd
from pprint import pprint
import json

#1- 读取Excel测试用例
excelDir = r"C://Users//Administrator//Desktop//接口自动化1.xls"
#1-1:打开Excel表
# workbook = xlrd.open_workbook(excelDir)
#查看所有的子表
# print(workbook.sheet_names())#返回是list
# workSheet = workbook.sheet_names()[1]
# workSheet = workbook.sheet_by_name("自动化")
#读取一行
# rows = workSheet.row_values(1)
#读取一列
# clos = workSheet.cell_value(1,6)
#读取指定单元格
# cellData = workSheet.cell_value(1,6)#行，列

#读取第六列表格的数据
worksheet = xlrd.open_workbook(u'C://Users//Administrator//Desktop//接口自动化1.xls')
sheet_names= worksheet.sheet_names()
print(sheet_names)

# for sheet_name in sheet_names:
#     sheet = worksheet.sheet_by_name(sheet_name)
#     rows = sheet.nrows # 获取行数
#     cols = sheet.ncols # 获取列数，尽管没用到
#     for i in range(1,rows) :
#         cell = sheet.cell_value(i, 6) # 取第六列数据
#         print(cell)

# print(cellData)
# print(workSheet.cell(1,6).ctype)#返回单元格的数据类型 0 1:字符串 2 3 4 5
# pprint(cellData,width=25)
# pprint(rows,width=25)
#2- -------------------------------------构建接口对应请求--------------------------------------
# import requests
#2- 查询历史上的今天
# addUser_url = "http://api.juheapi.com/japi/toh"
# addUser_data = json.loads(cell)#字符串转成字典格式,loads方法中需要使用双引号，否则会报错
# str_json = json.dumps( addUser_data )#字典转成json格式
# print(addUser_data)

    # {
    # "key":"062d368f257c4cdccb8d922ff1611dc3",
    # "v":"1.0",
    # "month":"10",
    # "day":"10"
# }#请求参数
# addUser_headers = {"Content-Type": "application/json;charset=UTF-8"}
# addUser_resp = requests.get(url=addUser_url,params=json.loads(str_json))
# addUser_resp = requests.post(addUser_url,data=json.dumps(addUser_data),headers=addUser_headers)
# pprint(addUser_resp.text)

for sheet_name in sheet_names:
    sheet = worksheet.sheet_by_name(sheet_name)
    rows = sheet.nrows # 获取行数
    cols = sheet.ncols # 获取列数，尽管没用到
    for i in range(1,rows) :
        cell = sheet.cell_value(i, 6) # 取第六列数据
        import requests
        # 2- 查询历史上的今天
        addUser_url = "http://api.juheapi.com/japi/toh"
        addUser_data = json.loads(cell)  # 字符串转成字典格式,loads方法中需要使用双引号，否则会报错
        str_json = json.dumps(addUser_data)  # 字典转成json格式
        # print(addUser_data)
        # {
        # "key":"062d368f257c4cdccb8d922ff1611dc3",
        # "v":"1.0",
        # "month":"10",
        # "day":"10"
        # }#请求参数
        addUser_headers = {"Content-Type": "application/json;charset=UTF-8"}
        addUser_resp = requests.get(url=addUser_url, params=json.loads(str_json))
        print(cell)
        res = addUser_resp.json()["reason"]
        print(res)
        if res == '请求成功！':
            print('查询历史上的今天接口测试---------->成功，耗时：---------->',addUser_resp.elapsed.total_seconds())
            excel_res = 'pass'
        else:
            print('查询历史上的今天接口测试---------->失败')
            excel_res = 'fail'

#3- 测试结果写入Excel
import xlutils
from xlutils.copy import copy#复制函数 xls xlsx,也可以用openpyxl
# 1- 首先打开Excel
workbookwr = xlrd.open_workbook(excelDir,formatting_info=True)
# 2- 复制
workbookWr = copy(workbookwr)
wrSheet = workbookWr.get_sheet(0)
# print(wrSheet)


for i in range(rows):
    if i != 0:
        wrSheet.write(i, 9, excel_res)

# for i in range(1,3):
#     wrSheet.write(i,9,excel_res)
# wrSheet.write(1,9,excel_res)#写单元格
workbookWr.save(r"C://Users//Administrator//Desktop//接口自动化测试.xls")


