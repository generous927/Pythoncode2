# -*- coding: UTF-8 -*-

import pandas
from sqlalchemy import create_engine

dabaname = 'library'

#连接数据库
con = create_engine("mysql+mysqldb://root:Tao123!@localhost:3306/" + dabaname, encoding='utf-8', echo=True)
path = 'C:/Users/Administrator/Documents/student.xlsx'
data = pandas.read_excel(path, encoding='gb18030')

data.rename(columns={'name': 'name', 'password': 'pwd'}, inplace=True)

tablename = 'user'

for e in data.values:
    sql = "INSERT INTO "+dabaname+"."+tablename+"(username, pwd) VALUES ('"+"','".join(str(i) for i in e) +"');"
    con.execute(sql)
    print(sql)
