#-*-coding:utf-8-*-
# ����pymysqlģ��
import pymysql
# ����database
conn = pymysql.connect(host="localhost", user="root",password="Tao123!",database="library",charset="utf8")
# �õ�һ������ִ��SQL���Ĺ�����
cursor = conn.cursor()
# ����Ҫִ�е�SQL���
sql = """
CREATE TABLE USER2 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
# ִ��SQL���
cursor.execute(sql)
# �رչ�����
cursor.close()
# �ر����ݿ�����
conn.close()