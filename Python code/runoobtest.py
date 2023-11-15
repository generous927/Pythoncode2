# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# list=[]
# for i in range(1,5):
#     # print(i)
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j or k!= i or k!=j:
#                 continue
#             else:
#                 list = list.append(str(i)+str(j)+str(k))
#                 print(list)

#
# L = []
# a = [1, 2, 3, 4]

# for i in range(len(a)):
#
# for val_1 in a:
#     for val_2 in a:
#         for val_3 in a:
#             if (val_1 == val_2 or val_1 == val_3 or val_2 == val_3):
#                 continue
#             else:
#                 L.append(str(val_1) + str(val_2) + str(val_3))
#
# print(len(L))
# print(L)


# sum = 0
# for i in range(101):
#     sum += i
#     # print(i,"+",i+1,end='')
# print(sum)

#
# i = int(input('输入1~7的整数：'))
# list = ['周一','周二','周三','周四','周五','周六','周日']
# date = list[i-1]
# print(date)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j ,"*",i,"=",i*j,end='\t')
#     print('')

# print(10**5)

# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         if year % 100!= 0:
#             leap = True
#     if year % 100 == 0:
#         if year % 400 == 0:
#             leap = True
#     # Write your logic here
#
#     return leap
#
# year = int(input())
# print(is_leap(year))

# l = 0
# s = input()
# d = s[0]
# for i in s:
#
#     if i == d:
#         l = d
#         break
#     else:
#         l = -1
#
# print(l)


# import re
# m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
# print(m.group(1) if m else -1)
#
# s = 'we-re-rt'
# print(s.split("-"))


# import random
# n = int(input())
# list1 = []
# for i in range(n):
#     ran = random.randint(1,500)
#     list1.append(ran)
#     # list1 = list1.sort()
#
# set1 = set(list1)
# print(set1)


# -*- coding: UTF-8 -*-

import xlrd
from pprint import pprint
import json
import requests

#1- 读取Excel测试用例
# excelDir = r"C://Users//Administrator//Desktop//接口自动化1.xls"
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
sheet_names = worksheet.sheet_names()
# print(sheet_names)
#
# # for sheet_name in sheet_names:
# #     sheet = worksheet.sheet_by_name(sheet_name)
# #     rows = sheet.nrows # 获取行数
# #     cols = sheet.ncols # 获取列数，尽管没用到
# #     for i in range(1,rows) :
# #         cell = sheet.cell_value(i, 6) # 取第六列数据
# #         print(cell)
#
# # print(cellData)
# # print(workSheet.cell(1,6).ctype)#返回单元格的数据类型 0 1:字符串 2 3 4 5
# # pprint(cellData,width=25)
# # pprint(rows,width=25)
# #2- -------------------------------------构建接口对应请求--------------------------------------
# # import requests
# #2- 查询历史上的今天
# # addUser_url = "http://api.juheapi.com/japi/toh"
# # addUser_data = json.loads(cell)#字符串转成字典格式,loads方法中需要使用双引号，否则会报错
# # str_json = json.dumps( addUser_data )#字典转成json格式
# # print(addUser_data)
#
#     # {
#     # "key":"062d368f257c4cdccb8d922ff1611dc3",
#     # "v":"1.0",
#     # "month":"10",
#     # "day":"10"
# # }#请求参数
# # addUser_headers = {"Content-Type": "application/json;charset=UTF-8"}
# # addUser_resp = requests.get(url=addUser_url,params=json.loads(str_json))
# # addUser_resp = requests.post(addUser_url,data=json.dumps(addUser_data),headers=addUser_headers)
# # pprint(addUser_resp.text)
#
for sheet_name in sheet_names:
    sheet = worksheet.sheet_by_name(sheet_name)
    rows = sheet.nrows # 获取行数
    cols = sheet.ncols # 获取列数，尽管没用到
    for i in range(1,rows) :
        add_headers = sheet.cell_value(i, 5)
        add_url = sheet.cell_value(i, 3)
        cell = sheet.cell_value(i, 6) # 取第七列数据
        print(cell)
        # print(news_url)
        import requests
        # 2- 查询历史上的今天
        addUser_url = add_url
        addUser_data = json.loads(cell)  # 字符串转成字典格式,loads方法中需要使用双引号，否则会报错
        str_json = json.dumps(addUser_data)  # 字典转成json格式
        # print(addUser_data)
        # print(add_headers)
        # # {
        # # "key":"062d368f257c4cdccb8d922ff1611dc3",
        # # "v":"1.0",
        # # "month":"10",
        # # "day":"10"
        # # }#请求参数
        # addUser_headers = add_headers
        addUser_resp = requests.get(url=addUser_url, params=json.loads(str_json))
        pprint(addUser_resp.text)
        res = addUser_resp.json()["reason"]
        print(res)
        if res == 'success':
            print('查询历史上的今天接口测试---------->成功，耗时：---------->',addUser_resp.elapsed.total_seconds())
            excel_res = 'pass'
        else:
            print('查询历史上的今天接口测试---------->失败')
            excel_res = 'fail'
#
        # #3- 测试结果写入Excel
        import xlutils
        from xlutils.copy import copy#复制函数 xls xlsx,也可以用openpyxl
        # 1- 首先打开Excel
        # workbookwr = xlrd.open_workbook(worksheet,formatting_info=True)
        # 2- 复制
        workbookWr = copy(worksheet)
        wrSheet = workbookWr.get_sheet(0)
        print(wrSheet)
        wrSheet.write(1, 9, excel_res)
        workbookWr.save(r"C://Users//Administrator//Desktop//接口自动化测试.xls")


import requests


#response 接口返回值
# r = requests.get('http://www.baidu.com')
# print(r)


'''
这是接口关键字驱动类，用于提供自动化接口测试的关键字方法
主要实现常用的关键字内容，并定义好所有的参数内容即可
接口中的常用关键字无非就是：
1.各种模拟请求方法：post/get/put/delete/header/...
2.设置入参的默认值时，设置的参数必须放在最后
'''

import requests

# class ApiKey:
    # def get(self,url,params=None,***kwargs):
