import xlrd
from pprint import pprint
import json
import requests

import xlutils
from xlutils.copy import copy  # 复制函数 xls xlsx,也可以用openpyxl

# 打开Excel表
worksheet = xlrd.open_workbook(u'C://Users//Administrator//Desktop//接口自动化1.xls')
workbookWr = copy(worksheet)
#返回表中所有工作表的名称
sheet_names = worksheet.sheet_names()
for sheet_name in sheet_names:
    #根据工作表的名称获取Excel中的工作表
    sheet = worksheet.sheet_by_name(sheet_name)
    rows = sheet.nrows # 获取行数
    cols = sheet.ncols # 获取列数
    for i in range(1,rows) :
        add_headers = sheet.cell_value(i, 5)# 取第六列数据（请求头）
        add_url = sheet.cell_value(i, 3)# 取第四列数据（url地址）
        cell = sheet.cell_value(i, 6)  # 取第七列数据（请求参数）
        # print(cell)
        # print(news_url)
        import requests
        # 查询历史上的今天
        addUser_url = add_url
        addUser_data = json.loads(cell)  # 字符串转成字典格式,loads方法中需要使用双引号，否则会报错
        str_json = json.dumps(addUser_data)  # 字典转成json格式
        #构建请求并发送
        addUser_resp = requests.get(url=addUser_url, params=json.loads(str_json))
        # pprint(addUser_resp.text)
        res = addUser_resp.json()["reason"]
        # print(res)
        if res == 'success':
            print('查询历史上的今天接口测试---------->成功，耗时：---------->', addUser_resp.elapsed.total_seconds())
            excel_res = 'pass'
        else:
            print('查询历史上的今天接口测试---------->失败')
            excel_res = 'fail'
        #测试结果写入Excel
        import xlutils
        from xlutils.copy import copy  # 复制函数 xls xlsx,也可以用openpyxl

        # 首先打开Excel，前面已经打开过了
        # 复制
        # workbookWr = copy(worksheet)
        # 获取第一个工作表
        wrSheet = workbookWr.get_sheet(0)
        for i in range(rows):
            if i != 0:
                wrSheet.write(i, 9, excel_res)

workbookWr.save(r"C://Users//Administrator//Desktop//接口自动化测试.xls")